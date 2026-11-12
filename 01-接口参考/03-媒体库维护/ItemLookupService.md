# ItemLookupService 远程元数据检索服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/ItemLookupService.html> ｜ 上级目录：[远程元数据检索服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

按类型（电影、剧集、专辑、人物……）向外部元数据源检索候选项，再把选中的结果写回条目。做“识别/匹配元数据”功能时使用。

- 接口数量：**14**
- 覆盖范围：官方参考站该服务下的全部 14 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Items/{Id}/ExternalIdInfos` | 获取条目的外部 ID 信息 | 管理员 |
| 2 | `GET` | `/Items/RemoteSearch/Image` | 获取远程图片 | 管理员 |
| 3 | `POST` | `/Items/Metadata/Reset` | 重置条目的元数据 | 管理员 |
| 4 | `POST` | `/Items/RemoteSearch/Apply/{Id}` | 对条目应用搜索结果并刷新元数据 | 管理员 |
| 5 | `POST` | `/Items/RemoteSearch/Book` | 远程搜索书籍 | 用户 |
| 6 | `POST` | `/Items/RemoteSearch/BoxSet` | 远程搜索合集（BoxSet） | 用户 |
| 7 | `POST` | `/Items/RemoteSearch/Game` | 远程搜索游戏 | 用户 |
| 8 | `POST` | `/Items/RemoteSearch/Movie` | 远程搜索电影 | 用户 |
| 9 | `POST` | `/Items/RemoteSearch/MusicAlbum` | 远程搜索音乐专辑 | 用户 |
| 10 | `POST` | `/Items/RemoteSearch/MusicArtist` | 远程搜索音乐艺术家 | 用户 |
| 11 | `POST` | `/Items/RemoteSearch/MusicVideo` | 远程搜索音乐视频（MV） | 用户 |
| 12 | `POST` | `/Items/RemoteSearch/Person` | 远程搜索人物 | 管理员 |
| 13 | `POST` | `/Items/RemoteSearch/Series` | 远程搜索剧集 | 用户 |
| 14 | `POST` | `/Items/RemoteSearch/Trailer` | 远程搜索预告片 | 用户 |

---

## 1. 获取条目的外部 ID 信息

`GET` `/Items/{Id}/ExternalIdInfos`

- **权限**：管理员令牌
- **成功响应**：`200` → `ExternalIdInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ExternalIdInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ExternalIdInfo`](../../02-数据模型/02-媒体条目.md#externalidinfo)

---

## 2. 获取远程图片

`GET` `/Items/RemoteSearch/Image`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ImageUrl` | query | string | 否 | 图片 URL。 |
| `ProviderName` | query | string | 否 | 提供方名称。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 3. 重置条目的元数据

`POST` `/Items/Metadata/Reset`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ItemIds` | query | string | 否 | 条目 ID 列表。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 4. 对条目应用搜索结果并刷新元数据

`POST` `/Items/RemoteSearch/Apply/{Id}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ReplaceAllImages` | query | string | 否 | 是否替换全部图片。 |
| `body` | body | RemoteSearchResult | — | 请求体：`RemoteSearchResult` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchResult`](../../02-数据模型/02-媒体条目.md#remotesearchresult)

> 该接口在官方文档中还引用了 2 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 5. 远程搜索书籍

`POST` `/Items/RemoteSearch/Book`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_BookInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_BookInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_bookinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 6. 远程搜索合集（BoxSet）

`POST` `/Items/RemoteSearch/BoxSet`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_ItemLookupInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_ItemLookupInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_itemlookupinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 7. 远程搜索游戏

`POST` `/Items/RemoteSearch/Game`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_GameInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_GameInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_gameinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 8. 远程搜索电影

`POST` `/Items/RemoteSearch/Movie`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_MovieInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_MovieInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_movieinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 9. 远程搜索音乐专辑

`POST` `/Items/RemoteSearch/MusicAlbum`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_AlbumInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_AlbumInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_albuminfo)

> 该接口在官方文档中还引用了 6 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 10. 远程搜索音乐艺术家

`POST` `/Items/RemoteSearch/MusicArtist`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_ArtistInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_ArtistInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_artistinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 11. 远程搜索音乐视频（MV）

`POST` `/Items/RemoteSearch/MusicVideo`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_MusicVideoInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_MusicVideoInfo`](../../02-数据模型/04-播放与转码.md#remotesearchquery_musicvideoinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 12. 远程搜索人物

`POST` `/Items/RemoteSearch/Person`

- **权限**：管理员令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_PersonLookupInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_PersonLookupInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_personlookupinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 13. 远程搜索剧集

`POST` `/Items/RemoteSearch/Series`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_SeriesInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_SeriesInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_seriesinfo)

> 该接口在官方文档中还引用了 6 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 14. 远程搜索预告片

`POST` `/Items/RemoteSearch/Trailer`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSearchResult []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | RemoteSearchQuery_TrailerInfo | — | 请求体：`RemoteSearchQuery`1` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSearchResult []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSearchQuery_TrailerInfo`](../../02-数据模型/02-媒体条目.md#remotesearchquery_trailerinfo)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
