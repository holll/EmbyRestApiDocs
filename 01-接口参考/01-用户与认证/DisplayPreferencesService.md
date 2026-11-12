# DisplayPreferencesService 显示偏好服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/DisplayPreferencesService.html> ｜ 上级目录：[显示偏好服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

保存每个用户、每种客户端（如 emby、emby-theater）的界面偏好：首页分区顺序、列表视图/海报视图、排序字段等。键由 userId + client 组成。

- 接口数量：**5**
- 覆盖范围：官方参考站该服务下的全部 5 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/DisplayPreferences/{Id}` | 获取用户对条目的显示偏好 | 用户 |
| 2 | `GET` | `/UserSettings/{UserId}` | 获取用户设置 | 用户 |
| 3 | `POST` | `/DisplayPreferences/{DisplayPreferencesId}` | 更新用户对条目的显示偏好 | 用户 |
| 4 | `POST` | `/UserSettings/{UserId}` | 更新用户对条目的显示偏好 | 用户 |
| 5 | `POST` | `/UserSettings/{UserId}/Partial` | 更新用户对条目的显示偏好 | 用户 |

---

## 1. 获取用户对条目的显示偏好

`GET` `/DisplayPreferences/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `DisplayPreferences`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `Client` | query | string | 否 | 客户端名称。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `DisplayPreferences` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`DisplayPreferences`](../../02-数据模型/03-用户与账号.md#displaypreferences)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 2. 获取用户设置

`GET` `/UserSettings/{UserId}`

- **权限**：用户令牌
- **成功响应**：`200` → `object`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `object` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 3. 更新用户对条目的显示偏好

`POST` `/DisplayPreferences/{DisplayPreferencesId}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DisplayPreferencesId` | path | string | 是 | 显示偏好 ID。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `body` | body | DisplayPreferences | — | 请求体：`DisplayPreferences` 对象。 |

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

[`DisplayPreferences`](../../02-数据模型/03-用户与账号.md#displaypreferences)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 4. 更新用户对条目的显示偏好

`POST` `/UserSettings/{UserId}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `body` | body | array | — | 请求体：`UserSettings` 对象。 |

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

## 5. 更新用户对条目的显示偏好

`POST` `/UserSettings/{UserId}/Partial`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
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
