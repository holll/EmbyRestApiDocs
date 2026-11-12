# UserNotificationsService 用户通知服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/UserNotificationsService.html> ｜ 上级目录：[用户通知服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

面向单个用户的通知：读取通知摘要、把通知标记为已读。与 NotificationsService（管理员群发）不同，这里是“用户收件箱”。

- 接口数量：**2**
- 覆盖范围：官方参考站该服务下的全部 2 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Notifications/Services/Defaults` | 获取默认通知信息 | 用户 |
| 2 | `POST` | `/Notifications/Services/Test` | 发送测试通知 | 用户 |

---

## 1. 获取默认通知信息

`GET` `/Notifications/Services/Defaults`

- **权限**：用户令牌
- **成功响应**：`200` → `UserNotificationInfo`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserNotificationInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserNotificationInfo`](../../02-数据模型/03-用户与账号.md#usernotificationinfo)

---

## 2. 发送测试通知

`POST` `/Notifications/Services/Test`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | UserNotificationInfo | — | 请求体：`UserNotificationInfo` 对象。 |

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

[`UserNotificationInfo`](../../02-数据模型/03-用户与账号.md#usernotificationinfo)
