# PlaystateService 播放状态上报服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/PlaystateService.html> ｜ 上级目录：[播放状态上报服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

播放进度三件套：开始播放、进度上报、停止播放；另有已播放标记、收藏、评分、用户数据更新。进度上报决定“继续观看”是否正确。

- 接口数量：**12**
- 覆盖范围：官方参考站该服务下的全部 12 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Users/{UserId}/PlayedItems/{Id}` | 标记条目为未播放 | 用户 |
| 2 | `DELETE` | `/Users/{UserId}/PlayingItems/{Id}` | 上报用户已停止播放 | 用户 |
| 3 | `POST` | `/Sessions/Playing` | 上报会话开始播放 | 用户 |
| 4 | `POST` | `/Sessions/Playing/Ping` | 播放会话心跳 | 用户 |
| 5 | `POST` | `/Sessions/Playing/Progress` | 上报会话播放进度 | 用户 |
| 6 | `POST` | `/Sessions/Playing/Stopped` | 上报会话停止播放 | 用户 |
| 7 | `POST` | `/Users/{UserId}/Items/{ItemId}/UserData` | 更新条目的用户数据 | 用户 |
| 8 | `POST` | `/Users/{UserId}/PlayedItems/{Id}` | 标记条目为已播放 | 用户 |
| 9 | `POST` | `/Users/{UserId}/PlayedItems/{Id}/Delete` | 标记条目为未播放 | 用户 |
| 10 | `POST` | `/Users/{UserId}/PlayingItems/{Id}` | 上报用户开始播放 | 用户 |
| 11 | `POST` | `/Users/{UserId}/PlayingItems/{Id}/Delete` | 上报用户已停止播放 | 用户 |
| 12 | `POST` | `/Users/{UserId}/PlayingItems/{Id}/Progress` | 上报用户播放进度 | 用户 |

---

## 1. 标记条目为未播放

`DELETE` `/Users/{UserId}/PlayedItems/{Id}`

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

## 2. 上报用户已停止播放

`DELETE` `/Users/{UserId}/PlayingItems/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 否 | 媒体源 ID。 |
| `NextMediaType` | query | string | 否 | 接下来要播放的媒体类型。 |
| `PositionTicks` | query | integer | 否 | 可选。播放停止时的位置，单位 tick，1 毫秒 = 10000 ticks。 |
| `LiveStreamId` | query | string | 否 | — |
| `PlaySessionId` | query | string | 否 | — |

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

## 3. 上报会话开始播放

`POST` `/Sessions/Playing`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | PlaybackStartInfo | — | 请求体：`PlaybackStartInfo` 对象。 |

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

[`PlaybackStartInfo`](../../02-数据模型/04-播放与转码.md#playbackstartinfo)

> 该接口在官方文档中还引用了 33 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 4. 播放会话心跳

`POST` `/Sessions/Playing/Ping`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `PlaySessionId` | query | string | 否 | — |

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

## 5. 上报会话播放进度

`POST` `/Sessions/Playing/Progress`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | PlaybackProgressInfo | — | 请求体：`PlaybackProgressInfo` 对象。 |

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

[`PlaybackProgressInfo`](../../02-数据模型/04-播放与转码.md#playbackprogressinfo)

> 该接口在官方文档中还引用了 33 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 6. 上报会话停止播放

`POST` `/Sessions/Playing/Stopped`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | PlaybackStopInfo | — | 请求体：`PlaybackStopInfo` 对象。 |

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

[`PlaybackStopInfo`](../../02-数据模型/04-播放与转码.md#playbackstopinfo)

> 该接口在官方文档中还引用了 29 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 7. 更新条目的用户数据

`POST` `/Users/{UserId}/Items/{ItemId}/UserData`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `ItemId` | path | string | 是 | 条目 ID |
| `body` | body | UserItemDataDto | — | 请求体：`UserItemDataDto` 对象。 |

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

[`UserItemDataDto`](../../02-数据模型/03-用户与账号.md#useritemdatadto)

---

## 8. 标记条目为已播放

`POST` `/Users/{UserId}/PlayedItems/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `UserItemDataDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `DatePlayed` | query | string | 否 | 条目最后播放时间（若有），格式 yyyyMMddHHmmss。 |
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

## 9. 标记条目为未播放

`POST` `/Users/{UserId}/PlayedItems/{Id}/Delete`

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

## 10. 上报用户开始播放

`POST` `/Users/{UserId}/PlayingItems/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 否 | 媒体源 ID。 |
| `CanSeek` | query | boolean | 否 | 指示客户端是否支持拖动进度。 |
| `AudioStreamIndex` | query | integer | 否 | — |
| `SubtitleStreamIndex` | query | integer | 否 | 字幕流序号。 |
| `PlayMethod` | query | string | 否 | 播放方式（DirectPlay 直连、DirectStream 直转封装、Transcode 转码）。 |
| `LiveStreamId` | query | string | 否 | — |
| `PlaySessionId` | query | string | 否 | — |

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

## 11. 上报用户已停止播放

`POST` `/Users/{UserId}/PlayingItems/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 否 | 媒体源 ID。 |
| `NextMediaType` | query | string | 否 | 接下来要播放的媒体类型。 |
| `PositionTicks` | query | integer | 否 | 可选。播放停止时的位置，单位 tick，1 毫秒 = 10000 ticks。 |
| `LiveStreamId` | query | string | 否 | — |
| `PlaySessionId` | query | string | 否 | — |

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

## 12. 上报用户播放进度

`POST` `/Users/{UserId}/PlayingItems/{Id}/Progress`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 否 | 媒体源 ID。 |
| `PositionTicks` | query | integer | 否 | 可选。当前位置，单位 tick，1 毫秒 = 10000 ticks。 |
| `IsPaused` | query | boolean | 否 | 指示播放器是否已暂停。 |
| `IsMuted` | query | boolean | 否 | 指示播放器是否已静音。 |
| `AudioStreamIndex` | query | integer | 否 | — |
| `SubtitleStreamIndex` | query | integer | 否 | 字幕流序号。 |
| `VolumeLevel` | query | integer | 否 | 取值范围 0–100。 |
| `PlayMethod` | query | string | 否 | 播放方式（DirectPlay 直连、DirectStream 直转封装、Transcode 转码）。 |
| `LiveStreamId` | query | string | 否 | — |
| `PlaySessionId` | query | string | 否 | — |
| `RepeatMode` | query | string | 否 | 循环模式（RepeatNone、RepeatAll、RepeatOne）。 |
| `SubtitleOffset` | query | string | 否 | 字幕时间偏移，单位 tick。 |
| `PlaybackRate` | query | string | 否 | 播放速率（如 1.0 表示正常速度）。 |
| `body` | body | OnPlaybackProgress | — | 请求体：`OnPlaybackProgress` 对象。 |

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

[`OnPlaybackProgress`](../../02-数据模型/04-播放与转码.md#onplaybackprogress)

> 该接口在官方文档中还引用了 2 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
