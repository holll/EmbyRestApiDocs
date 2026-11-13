"""Pure, offline model normalization; never merges unrelated short-name models.

normalize_services(services) -> (deep-copied services, canonical model dict).
Conflicting scalar/array source declarations remain explicit, not guessed.
"""
from collections import defaultdict
from copy import deepcopy
import re


class ModelConflictError(ValueError):
    """Incompatible definitions share a supposedly identical model identity."""


def model_identity(definition):
    description = definition.get('description', '').removeprefix('see also ').strip()
    if re.fullmatch(r'[\w]+(?:\.[\w]+)+', description):
        return description
    return definition.get('identity') or definition['name']


def _wrapper_name(identity):
    if identity.startswith('QueryResult_'):
        return 'QueryResult_' + identity.rsplit('.', 1)[-1] if '.' in identity else identity
    return None


def normalize_services(services):
    normalized = deepcopy(services)
    groups = defaultdict(list)
    for svc in normalized:
        for op in svc['operations']:
            for definition in op.get('definitions', []):
                source = {'service': svc['service'], 'method': op.get('method', ''),
                          'path': op.get('path', ''), 'url': op.get('doc_url', '')}
                sources = definition.setdefault('sources', [])
                if source not in sources:
                    sources.append(source)
                groups[model_identity(definition)].append(definition)
    short_ids = defaultdict(set)
    for identity, definitions in groups.items():
        short_ids[_wrapper_name(identity) or definitions[0]['name']].add(identity)
    names = {}
    for identity, definitions in groups.items():
        short = _wrapper_name(identity) or definitions[0]['name']
        names[identity] = short if len(short_ids[short]) == 1 else identity.replace('.', '_')
    if len(set(names.values())) != len(names):
        raise ModelConflictError('Canonical model name collision')

    # Types in an operation refer to that operation's definitions. QueryResult
    # pseudo-names must be resolved before their nested entity's short name.
    for svc in normalized:
        for op in svc['operations']:
            aliases = {}
            for definition in op.get('definitions', []):
                identity = model_identity(definition)
                aliases[identity] = names[identity]
                if not _wrapper_name(identity):
                    previous = aliases.get(definition['name'])
                    if previous and previous != names[identity]:
                        raise ModelConflictError('Ambiguous local reference: ' + definition['name'])
                    aliases[definition['name']] = names[identity]
            def resolve(value):
                for old in sorted(aliases, key=len, reverse=True):
                    value = re.sub(r'(?<![\w.])' + re.escape(old) + r'(?![\w.])', aliases[old], value)
                return value
            for definition in op.get('definitions', []):
                identity = model_identity(definition)
                definition['identity'] = identity
                definition['name'] = names[identity]
                for field in definition.get('fields', []):
                    field['type'] = resolve(field.get('type', ''))
            for item in op.get('params', []) + op.get('responses', []):
                item['type'] = resolve(item.get('type', ''))

    registry = {}
    for identity, definitions in groups.items():
        name = names[identity]
        result = deepcopy(definitions[0])
        sources = {tuple(sorted(source.items())) for d in definitions for source in d.get('sources', [])}
        result['sources'] = [dict(source) for source in sorted(sources)]
        enums = [d.get('enum', []) for d in definitions if d.get('enum')]
        if enums:
            if any(set(e) != set(enums[0]) for e in enums[1:]):
                raise ModelConflictError('Conflicting enum values: ' + identity)
            result['enum'] = enums[0]
        populated = [d for d in definitions if d.get('fields')]
        if populated:
            fields = {f['name']: f for f in populated[0]['fields']}
            expected = set(fields)
            if any({f['name'] for f in d['fields']} != expected for d in populated[1:]):
                raise ModelConflictError('Conflicting field sets: ' + identity)
            merged = []
            for field_name, field in fields.items():
                variants = [next(f for f in d['fields'] if f['name'] == field_name) for d in populated]
                types = sorted({f.get('type', '') for f in variants})
                target = deepcopy(field)
                if len(types) > 1:
                    if len({t.removesuffix('[]') for t in types}) != 1:
                        raise ModelConflictError('Conflicting field types: ' + identity + '.' + field_name)
                    target.update(type=' | '.join(types), type_candidates=types,
                                  type_status='source_conflict')
                notes = sorted({f.get('notes', '') for f in variants if f.get('notes')})
                if notes:
                    target['notes'] = max(notes, key=lambda n: (len(n), n))
                merged.append(target)
            result['fields'] = merged
        registry[name] = result
    # Every occurrence now contains the richest same-identity declaration, so
    # downstream consumers cannot accidentally choose an earlier empty enum.
    for svc in normalized:
        for op in svc['operations']:
            enriched = []
            for definition in op.get('definitions', []):
                canonical = deepcopy({key: value for key, value in registry[definition['name']].items()
                                      if key != 'sources'})
                canonical['sources'] = definition.get('sources', [])
                enriched.append(canonical)
            op['definitions'] = enriched
    return normalized, dict(sorted(registry.items()))


def build_model_registry(services):
    """Return the canonical model dictionary without mutating services."""
    return normalize_services(services)[1]
