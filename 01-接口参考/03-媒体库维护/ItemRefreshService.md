# ItemRefreshService 条目刷新服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/ItemRefreshService.html> ｜ 上级目录：[条目刷新服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

触发条目元数据刷新：全量刷新、仅刷新缺失字段、按外部 ID 重新匹配。

- 接口数量：**1**
- 收录范围：当前官方文档快照中的 1 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `POST` | `/Items/{Id}/Refresh` | 刷新条目元数据 | 用户 |

---

## 1. 刷新条目元数据

`POST` `/Items/{Id}/Refresh`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Recursive` | query | boolean | 未标注 | 指示是否递归刷新。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MetadataRefreshMode` | query | string | 未标注 | 指定元数据刷新模式。 |
| `ImageRefreshMode` | query | string | 未标注 | 指定图片刷新模式。 |
| `ReplaceAllMetadata` | query | string | 未标注 | 是否替换元数据，仅在刷新模式为 FullRefresh 时有效。 |
| `ReplaceAllImages` | query | string | 未标注 | 是否替换图片，仅在刷新模式为 FullRefresh 时有效。 |
| `body` | body | BaseRefreshRequest | 是 | 请求体：`BaseRefreshRequest` 对象。 |

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

[`BaseRefreshRequest`](../../02-数据模型/06-系统与配置.md#baserefreshrequest)
