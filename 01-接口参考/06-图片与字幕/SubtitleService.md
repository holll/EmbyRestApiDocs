# SubtitleService 字幕服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/SubtitleService.html> ｜ 上级目录：[字幕服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

字幕全链路：远程搜索字幕、下载字幕、按格式获取字幕流（SRT/VTT/ASS）、上传外挂字幕、删除字幕、获取字幕播放列表。

- 接口数量：**16**
- 收录范围：当前官方文档快照中的 16 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Items/{Id}/Subtitles/{Index}` | 删除外挂字幕文件 | 用户 |
| 2 | `DELETE` | `/Videos/{Id}/Subtitles/{Index}` | 删除外挂字幕文件 | 用户 |
| 3 | `GET` | `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 4 | `GET` | `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 5 | `GET` | `/Items/{Id}/RemoteSearch/Subtitles/{Language}` | 按语言远程搜索字幕 | 用户 |
| 6 | `GET` | `/Providers/Subtitles/Subtitles/{Id}` | 获取字幕提供方下载的字幕内容 | 用户 |
| 7 | `GET` | `/Videos/{Id}/{MediaSourceId}/Attachments/{Index}/Stream` | 按指定格式获取字幕 | 用户 |
| 8 | `GET` | `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 9 | `GET` | `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 10 | `HEAD` | `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 11 | `HEAD` | `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 12 | `HEAD` | `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 13 | `HEAD` | `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}` | 按指定格式获取字幕 | 用户 |
| 14 | `POST` | `/Items/{Id}/RemoteSearch/Subtitles/{SubtitleId}` | 下载指定的远程字幕 | 用户 |
| 15 | `POST` | `/Items/{Id}/Subtitles/{Index}/Delete` | 删除外挂字幕文件 | 用户 |
| 16 | `POST` | `/Videos/{Id}/Subtitles/{Index}/Delete` | 删除外挂字幕文件 | 用户 |

---

## 1. 删除外挂字幕文件

`DELETE` `/Items/{Id}/Subtitles/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |

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

## 2. 删除外挂字幕文件

`DELETE` `/Videos/{Id}/Subtitles/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |

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

## 3. 按指定格式获取字幕

`GET` `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | path | integer | 是 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 4. 按指定格式获取字幕

`GET` `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | query | integer | 未标注 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 5. 按语言远程搜索字幕

`GET` `/Items/{Id}/RemoteSearch/Subtitles/{Language}`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteSubtitleInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `Language` | path | string | 是 | 语言。 |
| `IsPerfectMatch` | query | boolean | 未标注 | 是否为完全匹配。 |
| `IsForced` | query | boolean | 未标注 | 是否为强制字幕（forced）。 |
| `IsHearingImpaired` | query | boolean | 未标注 | 是否为听障字幕（SDH）。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteSubtitleInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteSubtitleInfo`](../../02-数据模型/04-播放与转码.md#remotesubtitleinfo)

---

## 6. 获取字幕提供方下载的字幕内容

`GET` `/Providers/Subtitles/Subtitles/{Id}`

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

## 7. 按指定格式获取字幕

`GET` `/Videos/{Id}/{MediaSourceId}/Attachments/{Index}/Stream`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |

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

## 8. 按指定格式获取字幕

`GET` `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | path | integer | 是 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 9. 按指定格式获取字幕

`GET` `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | query | integer | 未标注 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 10. 按指定格式获取字幕

`HEAD` `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | path | integer | 是 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 11. 按指定格式获取字幕

`HEAD` `/Items/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | query | integer | 未标注 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 12. 按指定格式获取字幕

`HEAD` `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/{StartPositionTicks}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | path | integer | 是 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 13. 按指定格式获取字幕

`HEAD` `/Videos/{Id}/{MediaSourceId}/Subtitles/{Index}/Stream.{Format}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | path | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |
| `Format` | path | string | 是 | 格式。 |
| `StartPositionTicks` | query | integer | 未标注 | 起始位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `EndPositionTicks` | query | integer | 未标注 | 结束位置，单位 tick（1 毫秒 = 10000 ticks）。 |
| `CopyTimestamps` | query | string | 未标注 | 是否复制时间戳。 |

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

## 14. 下载指定的远程字幕

`POST` `/Items/{Id}/RemoteSearch/Subtitles/{SubtitleId}`

- **权限**：用户令牌
- **成功响应**：`200` → `SubtitleDownloadResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `SubtitleId` | path | string | 是 | 字幕 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `SubtitleDownloadResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SubtitleDownloadResult`](../../02-数据模型/04-播放与转码.md#subtitledownloadresult)

---

## 15. 删除外挂字幕文件

`POST` `/Items/{Id}/Subtitles/{Index}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |

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

## 16. 删除外挂字幕文件

`POST` `/Videos/{Id}/Subtitles/{Index}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MediaSourceId` | query | string | 是 | 媒体源 ID。 |
| `Index` | path | integer | 是 | 字幕流序号。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
