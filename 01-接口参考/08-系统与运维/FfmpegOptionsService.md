# FfmpegOptionsService FFmpeg 选项服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/FfmpegOptionsService.html> ｜ 上级目录：[FFmpeg 选项服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

读取/更新 FFmpeg 相关选项（编码器路径、线程数等）。

- 接口数量：**2**
- 覆盖范围：官方参考站该服务下的全部 2 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Encoding/FfmpegOptions` | 获取 FFmpeg 选项 | 用户 |
| 2 | `POST` | `/Encoding/FfmpegOptions` | 更新 FFmpeg 选项 | 管理员 |

---

## 1. 获取 FFmpeg 选项

`GET` `/Encoding/FfmpegOptions`

- **权限**：用户令牌
- **成功响应**：`200` → `EditObjectContainer`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `EditObjectContainer` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`EditObjectContainer`](../../02-数据模型/06-系统与配置.md#editobjectcontainer)

> 该接口在官方文档中还引用了 9 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 2. 更新 FFmpeg 选项

`POST` `/Encoding/FfmpegOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | string (binary) | — | 二进制流，请求体直接传文件内容。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
