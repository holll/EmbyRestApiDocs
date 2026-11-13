# DlnaServerService DLNA 服务器服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/DlnaServerService.html> ｜ 上级目录：[DLNA 服务器服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

对外暴露的 DLNA/UPnP 端点（ConnectionManager、ContentDirectory、设备描述）。给第三方 DLNA 客户端或调试工具使用，普通 App 一般不需要。

- 接口数量：**16**
- 收录范围：当前官方文档快照中的 16 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Dlna/{UuId}/connectionmanager/connectionmanager` | 获取 DLNA ConnectionManager XML | 未标注 |
| 2 | `GET` | `/Dlna/{UuId}/connectionmanager/connectionmanager.xml` | 获取 DLNA ConnectionManager XML | 未标注 |
| 3 | `GET` | `/Dlna/{UuId}/contentdirectory/contentdirectory` | 获取 DLNA ContentDirectory XML | 未标注 |
| 4 | `GET` | `/Dlna/{UuId}/contentdirectory/contentdirectory.xml` | 获取 DLNA ContentDirectory XML | 未标注 |
| 5 | `GET` | `/Dlna/{UuId}/description` | 获取 DLNA 设备信息 | 未标注 |
| 6 | `GET` | `/Dlna/{UuId}/description.xml` | 获取 DLNA 设备信息 | 未标注 |
| 7 | `GET` | `/Dlna/{UuId}/icons/{Filename}` | 获取服务器图标 | 未标注 |
| 8 | `GET` | `/Dlna/icons/{Filename}` | 获取服务器图标 | 未标注 |
| 9 | `HEAD` | `/Dlna/{UuId}/connectionmanager/connectionmanager` | 获取 DLNA ConnectionManager XML | 未标注 |
| 10 | `HEAD` | `/Dlna/{UuId}/connectionmanager/connectionmanager.xml` | 获取 DLNA ConnectionManager XML | 未标注 |
| 11 | `HEAD` | `/Dlna/{UuId}/contentdirectory/contentdirectory` | 获取 DLNA ContentDirectory XML | 未标注 |
| 12 | `HEAD` | `/Dlna/{UuId}/contentdirectory/contentdirectory.xml` | 获取 DLNA ContentDirectory XML | 未标注 |
| 13 | `HEAD` | `/Dlna/{UuId}/description` | 获取 DLNA 设备信息 | 未标注 |
| 14 | `HEAD` | `/Dlna/{UuId}/description.xml` | 获取 DLNA 设备信息 | 未标注 |
| 15 | `POST` | `/Dlna/{UuId}/connectionmanager/control` | 处理控制请求 | 未标注 |
| 16 | `POST` | `/Dlna/{UuId}/contentdirectory/control` | 处理控制请求 | 未标注 |

---

## 1. 获取 DLNA ConnectionManager XML

`GET` `/Dlna/{UuId}/connectionmanager/connectionmanager`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 2. 获取 DLNA ConnectionManager XML

`GET` `/Dlna/{UuId}/connectionmanager/connectionmanager.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 3. 获取 DLNA ContentDirectory XML

`GET` `/Dlna/{UuId}/contentdirectory/contentdirectory`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 4. 获取 DLNA ContentDirectory XML

`GET` `/Dlna/{UuId}/contentdirectory/contentdirectory.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 5. 获取 DLNA 设备信息

`GET` `/Dlna/{UuId}/description`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 6. 获取 DLNA 设备信息

`GET` `/Dlna/{UuId}/description.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 7. 获取服务器图标

`GET` `/Dlna/{UuId}/icons/{Filename}`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |
| `Filename` | path | string | 是 | 图标文件名。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 8. 获取服务器图标

`GET` `/Dlna/icons/{Filename}`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | query | string | 未标注 | 服务器 UUID。 |
| `Filename` | path | string | 是 | 图标文件名。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 9. 获取 DLNA ConnectionManager XML

`HEAD` `/Dlna/{UuId}/connectionmanager/connectionmanager`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 10. 获取 DLNA ConnectionManager XML

`HEAD` `/Dlna/{UuId}/connectionmanager/connectionmanager.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 11. 获取 DLNA ContentDirectory XML

`HEAD` `/Dlna/{UuId}/contentdirectory/contentdirectory`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 12. 获取 DLNA ContentDirectory XML

`HEAD` `/Dlna/{UuId}/contentdirectory/contentdirectory.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 13. 获取 DLNA 设备信息

`HEAD` `/Dlna/{UuId}/description`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 14. 获取 DLNA 设备信息

`HEAD` `/Dlna/{UuId}/description.xml`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 15. 处理控制请求

`POST` `/Dlna/{UuId}/connectionmanager/control`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（无返回内容，动作类接口）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |
| `body` | body | string (binary) | 是 | 二进制流，请求体直接传文件内容。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 16. 处理控制请求

`POST` `/Dlna/{UuId}/contentdirectory/control`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200`（无返回内容，动作类接口）

> No authentication required

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UuId` | path | string | 是 | 服务器 UUID。 |
| `body` | body | string (binary) | 是 | 二进制流，请求体直接传文件内容。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
