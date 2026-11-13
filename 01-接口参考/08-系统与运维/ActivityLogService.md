# ActivityLogService 活动日志服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/ActivityLogService.html> ｜ 上级目录：[活动日志服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

读取服务器活动日志（登录、播放、扫描等事件），支持按时间与分页过滤。

- 接口数量：**1**
- 收录范围：当前官方文档快照中的 1 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/System/ActivityLog/Entries` | 获取活动日志 | 管理员 |

---

## 1. 获取活动日志

`GET` `/System/ActivityLog/Entries`

- **权限**：管理员令牌
- **成功响应**：`200` → `QueryResult_ActivityLogEntry`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `MinDate` | query | string | 否 | 可选。最小日期，格式为 ISO 8601。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_ActivityLogEntry` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_ActivityLogEntry`](../../02-数据模型/01-通用结构.md#queryresult_activitylogentry)

> 该接口在官方文档中还引用了 2 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
