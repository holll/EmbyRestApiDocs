# RemoteImageService 远程图片服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/RemoteImageService.html> ｜ 上级目录：[远程图片服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

从外部图片源（TMDB 等）搜索候选图片并下载为条目图片。做“更换封面”功能时使用。

- 接口数量：**4**
- 覆盖范围：官方参考站该服务下的全部 4 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Images/Remote` | 获取远程图片 | 管理员 |
| 2 | `GET` | `/Items/{Id}/RemoteImages` | 获取条目可用的远程图片 | 用户 |
| 3 | `GET` | `/Items/{Id}/RemoteImages/Providers` | 获取条目可用的远程图片来源 | 用户 |
| 4 | `POST` | `/Items/{Id}/RemoteImages/Download` | 下载条目的远程图片 | 管理员 |

---

## 1. 获取远程图片

`GET` `/Images/Remote`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ImageUrl` | query | string | 否 | 图片 URL。 |

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

## 2. 获取条目可用的远程图片

`GET` `/Items/{Id}/RemoteImages`

- **权限**：用户令牌
- **成功响应**：`200` → `RemoteImageResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `ProviderName` | query | string | 否 | 可选。要使用的图片提供方。 |
| `IncludeAllLanguages` | query | string | 否 | 可选。 |
| `EnableSeriesImages` | query | boolean | 否 | 可选。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RemoteImageResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RemoteImageResult`](../../02-数据模型/02-媒体条目.md#remoteimageresult)

> 该接口在官方文档中还引用了 3 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 3. 获取条目可用的远程图片来源

`GET` `/Items/{Id}/RemoteImages/Providers`

- **权限**：用户令牌
- **成功响应**：`200` → `ImageProviderInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ImageProviderInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ImageProviderInfo`](../../02-数据模型/02-媒体条目.md#imageproviderinfo)、[`ImageType`](../../02-数据模型/02-媒体条目.md#imagetype)

---

## 4. 下载条目的远程图片

`POST` `/Items/{Id}/RemoteImages/Download`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Type` | query | string | 否 | 图片类型（Primary / Backdrop / Logo / Thumb 等）。 |
| `ProviderName` | query | string | 否 | 提供方名称。 |
| `ImageUrl` | query | string | 否 | 图片 URL。 |
| `body` | body | BaseDownloadRemoteImage | — | 请求体：`BaseDownloadRemoteImage` 对象。 |

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

[`BaseDownloadRemoteImage`](../../02-数据模型/02-媒体条目.md#basedownloadremoteimage)
