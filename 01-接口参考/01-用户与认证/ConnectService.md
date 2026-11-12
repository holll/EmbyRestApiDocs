# ConnectService Emby Connect 服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/ConnectService.html> ｜ 上级目录：[Emby Connect 服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

Emby Connect 是官方的“账号云”登录方式：用户用邮箱注册 Connect 账号，客户端凭 Connect 换取本地服务器用户。本服务负责发起/解除 Connect 绑定，以及用 Connect 用户 ID 反查本地用户。

- 接口数量：**5**
- 覆盖范围：官方参考站该服务下的全部 5 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Users/{Id}/Connect/Link` | 解除用户的 Connect 绑定 | 管理员 |
| 2 | `GET` | `/Connect/Exchange` | 用 Connect 用户 ID 换取本地用户 | 用户 |
| 3 | `GET` | `/Connect/Pending` | 为用户创建 Connect 绑定 | 管理员 |
| 4 | `POST` | `/Users/{Id}/Connect/Link` | 为用户创建 Connect 绑定 | 管理员 |
| 5 | `POST` | `/Users/{Id}/Connect/Link/Delete` | 解除用户的 Connect 绑定 | 管理员 |

---

## 1. 解除用户的 Connect 绑定

`DELETE` `/Users/{Id}/Connect/Link`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |

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

## 2. 用 Connect 用户 ID 换取本地用户

`GET` `/Connect/Exchange`

- **权限**：用户令牌
- **成功响应**：`200` → `ConnectAuthenticationExchangeResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ConnectUserId` | query | string | 否 | Connect 用户 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ConnectAuthenticationExchangeResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ConnectAuthenticationExchangeResult`](../../02-数据模型/03-用户与账号.md#connectauthenticationexchangeresult)

---

## 3. 为用户创建 Connect 绑定

`GET` `/Connect/Pending`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

该接口无请求参数。

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

## 4. 为用户创建 Connect 绑定

`POST` `/Users/{Id}/Connect/Link`

- **权限**：管理员令牌
- **成功响应**：`200` → `UserLinkResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `ConnectUsername` | query | string | 否 | Connect 用户名。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserLinkResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserLinkResult`](../../02-数据模型/03-用户与账号.md#userlinkresult)

---

## 5. 解除用户的 Connect 绑定

`POST` `/Users/{Id}/Connect/Link/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
