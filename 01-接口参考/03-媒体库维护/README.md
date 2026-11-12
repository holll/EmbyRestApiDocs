# 媒体库维护

> [返回总目录](../../README.md)

| 服务 | 中文名 | 接口数 | 说明 |
|---|---|---|---|
| [ItemLookupService](ItemLookupService.md) | 远程元数据检索服务 | 14 | 按类型（电影、剧集、专辑、人物……）向外部元数据源检索候选项，再把选中的结果写回 |
| [ItemRefreshService](ItemRefreshService.md) | 条目刷新服务 | 1 | 触发条目元数据刷新 |
| [ItemUpdateService](ItemUpdateService.md) | 条目更新服务 | 2 | 以“元数据编辑器”的方式读取和写回条目字段（标题、简介、年份、评分等），并可指定 |
| [LibraryStructureService](LibraryStructureService.md) | 媒体库结构维护服务 | 10 | 管理员接口 |
