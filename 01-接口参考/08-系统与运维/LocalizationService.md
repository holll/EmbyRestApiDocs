# LocalizationService 本地化服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/LocalizationService.html> ｜ 上级目录：[本地化服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

获取国家/地区、区域文化、家长分级、本地化选项，用于语言与分级下拉框。

- 接口数量：**4**
- 覆盖范围：官方参考站该服务下的全部 4 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Localization/Countries` | 获取已知国家/地区 | 用户 |
| 2 | `GET` | `/Localization/Cultures` | 获取已知区域文化 | 用户 |
| 3 | `GET` | `/Localization/Options` | 获取本地化选项 | 用户 |
| 4 | `GET` | `/Localization/ParentalRatings` | 获取已知家长分级 | 用户 |

---

## 1. 获取已知国家/地区

`GET` `/Localization/Countries`

- **权限**：用户令牌
- **成功响应**：`200` → `CountryInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `CountryInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`CountryInfo`](../../02-数据模型/06-系统与配置.md#countryinfo)

---

## 2. 获取已知区域文化

`GET` `/Localization/Cultures`

- **权限**：用户令牌
- **成功响应**：`200` → `CultureDto []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `CultureDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`CultureDto`](../../02-数据模型/06-系统与配置.md#culturedto)

---

## 3. 获取本地化选项

`GET` `/Localization/Options`

- **权限**：用户令牌
- **成功响应**：`200` → `LocalizatonOption []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `LocalizatonOption []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`LocalizatonOption`](../../02-数据模型/06-系统与配置.md#localizatonoption)

---

## 4. 获取已知家长分级

`GET` `/Localization/ParentalRatings`

- **权限**：用户令牌
- **成功响应**：`200` → `ParentalRating []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ParentalRating []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ParentalRating`](../../02-数据模型/06-系统与配置.md#parentalrating)
