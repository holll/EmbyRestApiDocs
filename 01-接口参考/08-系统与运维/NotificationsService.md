# NotificationsService 管理员通知服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/NotificationsService.html> ｜ 上级目录：[管理员通知服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

管理员群发通知：通知类型列表、向所有管理员发送通知。

- 接口数量：**2**
- 覆盖范围：官方参考站该服务下的全部 2 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Notifications/Types` | 获取通知类型 | 用户 |
| 2 | `POST` | `/Notifications/Admin` | 向所有管理员发送通知 | 用户 |

---

## 1. 获取通知类型

`GET` `/Notifications/Types`

- **权限**：用户令牌
- **成功响应**：`200` → `NotificationCategoryInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `NotificationCategoryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`NotificationCategoryInfo`](../../02-数据模型/03-用户与账号.md#notificationcategoryinfo)、[`NotificationTypeInfo`](../../02-数据模型/03-用户与账号.md#notificationtypeinfo)

---

## 2. 向所有管理员发送通知

`POST` `/Notifications/Admin`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | query | string | 否 | 通知名称。 |
| `Description` | query | string | 否 | 通知描述。 |
| `ImageUrl` | query | string | 否 | 通知图片 URL。 |
| `Url` | query | string | 否 | 通知详情 URL。 |
| `Level` | query | integer | 否 | 通知级别（Normal、Warning、Error）。 |
| `body` | body | AddAdminNotification | — | 请求体：`AddAdminNotification` 对象。 |

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

[`AddAdminNotification`](../../02-数据模型/03-用户与账号.md#addadminnotification)
