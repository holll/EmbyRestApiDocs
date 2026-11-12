# MoviesService 电影服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/MoviesService.html> ｜ 上级目录：[电影服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

电影推荐与相似电影查询。接口很少，通常配合 ItemsService 使用。

- 接口数量：**1**
- 覆盖范围：官方参考站该服务下的全部 1 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Movies/Recommendations` | 获取电影推荐 | 用户 |

---

## 1. 获取电影推荐

`GET` `/Movies/Recommendations`

- **权限**：用户令牌
- **成功响应**：`200` → `RecommendationDto []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `CategoryLimit` | query | integer | 否 | 最多返回的分类数。 |
| `ItemLimit` | query | integer | 否 | 每个分类下最多返回的条目数。 |
| `UserId` | query | string | 否 | 可选。按用户 ID 过滤，并在结果中附带该用户的用户数据。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `RecommendationDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`RecommendationDto`](../../02-数据模型/06-系统与配置.md#recommendationdto)、[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
