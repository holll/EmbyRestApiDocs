# PlaylistService 播放列表服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/PlaylistService.html> ｜ 上级目录：[播放列表服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

管理播放列表：新建、查看条目、增删条目、移动条目顺序、取播放列表的原始条目。

- 接口数量：**7**
- 收录范围：当前官方文档快照中的 7 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Playlists/{Id}/Items` | 从播放列表移除条目 | 用户 |
| 2 | `GET` | `/Playlists/{Id}/AddToPlaylistInfo` | 获取“加入播放列表”的可用目标 | 用户 |
| 3 | `GET` | `/Playlists/{Id}/Items` | 获取播放列表的原始条目 | 用户 |
| 4 | `POST` | `/Playlists` | 新建播放列表 | 用户 |
| 5 | `POST` | `/Playlists/{Id}/Items` | 向播放列表添加条目 | 用户 |
| 6 | `POST` | `/Playlists/{Id}/Items/{ItemId}/Move/{NewIndex}` | 移动播放列表条目 | 用户 |
| 7 | `POST` | `/Playlists/{Id}/Items/Delete` | 从播放列表移除条目 | 用户 |

---

## 1. 从播放列表移除条目

`DELETE` `/Playlists/{Id}/Items`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `EntryIds` | query | string | 是 | 活动日志条目 ID 列表。 |

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

## 2. 获取“加入播放列表”的可用目标

`GET` `/Playlists/{Id}/AddToPlaylistInfo`

- **权限**：用户令牌
- **成功响应**：`200` → `AddToPlaylistInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | query | string | 未标注 | 用户 ID。 |
| `Ids` | query | string | 是 | 条目 ID，英文逗号分隔。 |
| `Id` | path | string | 是 | 条目 ID |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AddToPlaylistInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AddToPlaylistInfo`](../../02-数据模型/04-播放与转码.md#addtoplaylistinfo)

---

## 3. 获取播放列表的原始条目

`GET` `/Playlists/{Id}/Items`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `UserId` | query | string | 未标注 | 用户 ID。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 4. 新建播放列表

`POST` `/Playlists`

- **权限**：用户令牌
- **成功响应**：`200` → `PlaylistCreationResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Ids` | query | string | 未标注 | 要加入播放列表的条目 ID。 |
| `MediaType` | query | string | 未标注 | 播放列表媒体类型。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `PlaylistCreationResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`PlaylistCreationResult`](../../02-数据模型/04-播放与转码.md#playlistcreationresult)

---

## 5. 向播放列表添加条目

`POST` `/Playlists/{Id}/Items`

- **权限**：用户令牌
- **成功响应**：`200` → `AddToPlaylistResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | query | string | 未标注 | 用户 ID。 |
| `Ids` | query | string | 是 | 条目 ID，英文逗号分隔。 |
| `Id` | path | string | 是 | 条目 ID |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AddToPlaylistResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AddToPlaylistResult`](../../02-数据模型/04-播放与转码.md#addtoplaylistresult)

---

## 6. 移动播放列表条目

`POST` `/Playlists/{Id}/Items/{ItemId}/Move/{NewIndex}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ItemId` | path | string | 是 | 请求体：`ItemId` 对象。 |
| `Id` | path | string | 是 | 条目 ID |
| `NewIndex` | path | integer | 是 | 新序号。 |

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

## 7. 从播放列表移除条目

`POST` `/Playlists/{Id}/Items/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `EntryIds` | query | string | 是 | 活动日志条目 ID 列表。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
