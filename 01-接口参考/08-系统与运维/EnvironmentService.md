# EnvironmentService 环境服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/EnvironmentService.html> ｜ 上级目录：[环境服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

服务器运行环境：可用磁盘、网络设备与共享、目录浏览、路径校验、默认编解码配置。配置媒体库路径时常用。

- 接口数量：**8**
- 覆盖范围：官方参考站该服务下的全部 8 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Environment/DefaultDirectoryBrowser` | 获取给定路径的父目录 | 管理员 |
| 2 | `GET` | `/Environment/DirectoryContents` | 获取指定目录的文件列表 | 管理员 |
| 3 | `GET` | `/Environment/Drives` | 获取服务器可用磁盘 | 管理员 |
| 4 | `GET` | `/Environment/NetworkDevices` | 获取网络中的设备列表 | 管理员 |
| 5 | `GET` | `/Environment/NetworkShares` | 获取网络设备的共享目录 | 管理员 |
| 6 | `GET` | `/Environment/ParentPath` | 获取给定路径的父目录 | 管理员 |
| 7 | `POST` | `/Environment/DirectoryContents` | 获取指定目录的文件列表 | 管理员 |
| 8 | `POST` | `/Environment/ValidatePath` | 获取指定目录的文件列表 | 管理员 |

---

## 1. 获取给定路径的父目录

`GET` `/Environment/DefaultDirectoryBrowser`

- **权限**：管理员令牌
- **成功响应**：`200` → `DefaultDirectoryBrowserInfo`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `DefaultDirectoryBrowserInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`DefaultDirectoryBrowserInfo`](../../02-数据模型/06-系统与配置.md#defaultdirectorybrowserinfo)

---

## 2. 获取指定目录的文件列表

`GET` `/Environment/DirectoryContents`

- **权限**：管理员令牌
- **成功响应**：`200` → `FileSystemEntryInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Path` | query | string | 否 | — |
| `IncludeFiles` | query | string | 否 | 可选。结果中是否包含文件，true/false。 |
| `IncludeDirectories` | query | string | 否 | 可选。结果中是否包含文件夹，true/false。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FileSystemEntryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`FileSystemEntryInfo`](../../02-数据模型/06-系统与配置.md#filesystementryinfo)、[`FileSystemEntryType`](../../02-数据模型/06-系统与配置.md#filesystementrytype)

---

## 3. 获取服务器可用磁盘

`GET` `/Environment/Drives`

- **权限**：管理员令牌
- **成功响应**：`200` → `FileSystemEntryInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FileSystemEntryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`FileSystemEntryInfo`](../../02-数据模型/06-系统与配置.md#filesystementryinfo)、[`FileSystemEntryType`](../../02-数据模型/06-系统与配置.md#filesystementrytype)

---

## 4. 获取网络中的设备列表

`GET` `/Environment/NetworkDevices`

- **权限**：管理员令牌
- **成功响应**：`200` → `FileSystemEntryInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FileSystemEntryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`FileSystemEntryInfo`](../../02-数据模型/06-系统与配置.md#filesystementryinfo)、[`FileSystemEntryType`](../../02-数据模型/06-系统与配置.md#filesystementrytype)

---

## 5. 获取网络设备的共享目录

`GET` `/Environment/NetworkShares`

- **权限**：管理员令牌
- **成功响应**：`200` → `FileSystemEntryInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Path` | query | string | 否 | — |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FileSystemEntryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`FileSystemEntryInfo`](../../02-数据模型/06-系统与配置.md#filesystementryinfo)、[`FileSystemEntryType`](../../02-数据模型/06-系统与配置.md#filesystementrytype)

---

## 6. 获取给定路径的父目录

`GET` `/Environment/ParentPath`

- **权限**：管理员令牌
- **成功响应**：`200` → `string`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Path` | query | string | 否 | — |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `string` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 7. 获取指定目录的文件列表

`POST` `/Environment/DirectoryContents`

- **权限**：管理员令牌
- **成功响应**：`200` → `FileSystemEntryInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Path` | query | string | 否 | — |
| `IncludeFiles` | query | string | 否 | 可选。结果中是否包含文件，true/false。 |
| `IncludeDirectories` | query | string | 否 | 可选。结果中是否包含文件夹，true/false。 |
| `body` | body | GetDirectoryContents | — | 请求体：`GetDirectoryContents` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FileSystemEntryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`GetDirectoryContents`](../../02-数据模型/02-媒体条目.md#getdirectorycontents)

> 该接口在官方文档中还引用了 2 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 8. 获取指定目录的文件列表

`POST` `/Environment/ValidatePath`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Path` | query | string | 否 | — |
| `body` | body | ValidatePath | — | 请求体：`ValidatePath` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ValidatePath`](../../02-数据模型/06-系统与配置.md#validatepath)
