# UserViewsService 用户视图服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/UserViewsService.html> ｜ 上级目录：[用户视图服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

返回某用户首页应显示的顶级视图（电影、电视节目、音乐、文件夹等）。客户端启动后通常先调 `/Users/{UserId}/Views` 建立首页导航。

- 接口数量：**1**
- 覆盖范围：官方参考站该服务下的全部 1 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Users/{UserId}/Views` | 获取用户的媒体库视图列表 | 用户 |

---

## 1. 获取用户的媒体库视图列表

`GET` `/Users/{UserId}/Views`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID。 |
| `IncludeExternalContent` | query | string | 否 | 是否包含频道、直播电视等外部视图。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
