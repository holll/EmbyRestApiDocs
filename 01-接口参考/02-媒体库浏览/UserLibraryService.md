# UserLibraryService 用户媒体库服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/UserLibraryService.html> ｜ 上级目录：[用户媒体库服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

以“用户视角”访问媒体库：某用户可见的媒体文件夹、某文件夹下的条目、以及条目的可见性设置（私有/公开/共享）。做权限敏感的浏览时优先用它。

- 接口数量：**20**
- 收录范围：当前官方文档快照中的 20 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Users/{UserId}/FavoriteItems/{Id}` | 取消收藏 | 用户 |
| 2 | `DELETE` | `/Users/{UserId}/Items/{Id}/Rating` | 删除用户对条目的个人评分 | 用户 |
| 3 | `GET` | `/LiveTv/Programs/{Id}` | 获取直播节目详情 | 用户 |
| 4 | `GET` | `/Users/{UserId}/Items/{Id}` | 从用户媒体库获取条目 | 用户 |
| 5 | `GET` | `/Users/{UserId}/Items/{Id}/Intros` | 获取正片播放前的片头/预告 | 用户 |
| 6 | `GET` | `/Users/{UserId}/Items/{Id}/LocalTrailers` | 获取条目的本地预告片 | 用户 |
| 7 | `GET` | `/Users/{UserId}/Items/{Id}/SpecialFeatures` | 获取条目的特别收录 | 用户 |
| 8 | `GET` | `/Users/{UserId}/Items/Latest` | 获取最新媒体 | 用户 |
| 9 | `GET` | `/Users/{UserId}/Items/Root` | 获取用户媒体库根目录 | 用户 |
| 10 | `GET` | `/Videos/{Id}/AdditionalParts` | 获取视频的附加分段 | 用户 |
| 11 | `POST` | `/Items/Access` | 更新用户条目访问权限 | 用户 |
| 12 | `POST` | `/Items/{Id}/MakePrivate` | 将条目设为私有 | 用户 |
| 13 | `POST` | `/Items/{Id}/MakePublic` | 将条目对全部用户公开 | 用户 |
| 14 | `POST` | `/Items/Shared/Leave` | 退出共享条目 | 用户 |
| 15 | `POST` | `/Users/{UserId}/FavoriteItems/{Id}` | 标记为收藏 | 用户 |
| 16 | `POST` | `/Users/{UserId}/FavoriteItems/{Id}/Delete` | 取消收藏 | 用户 |
| 17 | `POST` | `/Users/{UserId}/Items/{Id}/HideFromResume` | 更新条目在“继续观看”中的隐藏状态 | 用户 |
| 18 | `POST` | `/Users/{UserId}/Items/{Id}/Rating` | 更新用户对条目的评分 | 用户 |
| 19 | `POST` | `/Users/{UserId}/Items/{Id}/Rating/Delete` | 删除用户对条目的个人评分 | 用户 |
| 20 | `POST` | `/Users/{UserId}/SearchedItems/` | 标记为收藏 | 用户 |

---

## 1. 取消收藏

`DELETE` `/Users/{UserId}/FavoriteItems/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 2. 删除用户对条目的个人评分

`DELETE` `/Users/{UserId}/Items/{Id}/Rating`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 3. 获取直播节目详情

`GET` `/LiveTv/Programs/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 4. 从用户媒体库获取条目

`GET` `/Users/{UserId}/Items/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 5. 获取正片播放前的片头/预告

`GET` `/Users/{UserId}/Items/{Id}/Intros`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines、TrailerUrls。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |

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

## 6. 获取条目的本地预告片

`GET` `/Users/{UserId}/Items/{Id}/LocalTrailers`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines、TrailerUrls。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)、[`SyncJobItemStatus`](../../02-数据模型/04-播放与转码.md#syncjobitemstatus)

> 该接口在官方文档中还引用了 26 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 7. 获取条目的特别收录

`GET` `/Users/{UserId}/Items/{Id}/SpecialFeatures`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines、TrailerUrls。 |
| `Id` | path | string | 是 | 电影 ID。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)、[`SyncJobItemStatus`](../../02-数据模型/04-播放与转码.md#syncjobitemstatus)

> 该接口在官方文档中还引用了 26 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 8. 获取最新媒体

`GET` `/Users/{UserId}/Items/Latest`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Limit` | query | integer | 未标注 | 请求体：`Limit` 对象。 |
| `ParentId` | query | string | 未标注 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、SortName、Studios、Taglines。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `IsFolder` | query | boolean | 未标注 | 按是否为文件夹过滤。 |
| `IsPlayed` | query | boolean | 未标注 | 按是否已播放过滤。 |
| `GroupItems` | query | string | 未标注 | 是否把条目归组到父容器中。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)、[`SyncJobItemStatus`](../../02-数据模型/04-播放与转码.md#syncjobitemstatus)

> 该接口在官方文档中还引用了 26 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 9. 获取用户媒体库根目录

`GET` `/Users/{UserId}/Items/Root`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 10. 获取视频的附加分段

`GET` `/Videos/{Id}/AdditionalParts`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | query | string | 否 | 可选。按用户 ID 过滤，并在结果中附带该用户的用户数据。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines、TrailerUrls。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |

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

## 11. 更新用户条目访问权限

`POST` `/Items/Access`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | UpdateUserItemAccess | 是 | 请求体：`UpdateUserItemAccess` 对象。 |

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

[`UpdateUserItemAccess`](../../02-数据模型/03-用户与账号.md#updateuseritemaccess)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 12. 将条目设为私有

`POST` `/Items/{Id}/MakePrivate`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

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

## 13. 将条目对全部用户公开

`POST` `/Items/{Id}/MakePublic`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

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

## 14. 退出共享条目

`POST` `/Items/Shared/Leave`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | LeaveSharedItems | 是 | 请求体：`LeaveSharedItems` 对象。 |

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

[`LeaveSharedItems`](../../02-数据模型/02-媒体条目.md#leaveshareditems)

---

## 15. 标记为收藏

`POST` `/Users/{UserId}/FavoriteItems/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 16. 取消收藏

`POST` `/Users/{UserId}/FavoriteItems/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 17. 更新条目在“继续观看”中的隐藏状态

`POST` `/Users/{UserId}/Items/{Id}/HideFromResume`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `Hide` | query | string | 是 | 是否把该条目从“继续观看”中隐藏，true/false。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 18. 更新用户对条目的评分

`POST` `/Users/{UserId}/Items/{Id}/Rating`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `Likes` | query | string | 是 | 用户是否喜欢该条目，true/false。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 19. 删除用户对条目的个人评分

`POST` `/Users/{UserId}/Items/{Id}/Rating/Delete`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserItemDataDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 20. 标记为收藏

`POST` `/Users/{UserId}/SearchedItems/`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `body` | body | ReportItemsSearched | 是 | 请求体：`ReportItemsSearched` 对象。 |

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

[`ReportItemsSearched`](../../02-数据模型/02-媒体条目.md#reportitemssearched)
