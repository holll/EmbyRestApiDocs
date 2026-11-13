# OpenApiService OpenAPI 规范服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/OpenApiService.html> ｜ 上级目录：[OpenAPI 规范服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

直接输出服务器的 OpenAPI/Swagger 规范，可用于自动生成客户端 SDK。

- 接口数量：**4**
- 收录范围：当前官方文档快照中的 4 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/openapi` | 获取 OpenAPI 3 规范 | 未标注 |
| 2 | `GET` | `/openapi.json` | 获取 OpenAPI 3 规范 | 未标注 |
| 3 | `GET` | `/swagger` | 获取 Swagger 规范 | 未标注 |
| 4 | `GET` | `/swagger.json` | 获取 Swagger 规范 | 未标注 |

---

## 1. 获取 OpenAPI 3 规范

`GET` `/openapi`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200` → `string`

> No authentication required

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `string` |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 2. 获取 OpenAPI 3 规范

`GET` `/openapi.json`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200` → `string`

> No authentication required

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `string` |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 3. 获取 Swagger 规范

`GET` `/swagger`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200` → `string`

> No authentication required

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `string` |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 4. 获取 Swagger 规范

`GET` `/swagger.json`

- **权限**：未标注（按接口语义判断）
- **成功响应**：`200` → `string`

> No authentication required

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `string` |
| 400 | 请求无法被服务器处理 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
