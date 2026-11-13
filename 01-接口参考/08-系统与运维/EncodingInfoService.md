# EncodingInfoService 编码信息服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/EncodingInfoService.html> ｜ 上级目录：[编码信息服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

查询服务器可用的视频编解码器与色调映射能力，决定客户端能请求哪些转码参数。

- 接口数量：**3**
- 收录范围：当前官方文档快照中的 3 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Encoding/CodecConfiguration/Defaults` | 获取默认编码配置 | 管理员 |
| 2 | `GET` | `/Encoding/CodecInformation/Video` | 获取可用的视频编解码器信息 | 管理员 |
| 3 | `GET` | `/Encoding/ToneMapOptions` | 获取可用的色调映射选项 | 管理员 |

---

## 1. 获取默认编码配置

`GET` `/Encoding/CodecConfiguration/Defaults`

- **权限**：管理员令牌
- **成功响应**：`200` → `CodecConfiguration []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `CodecConfiguration []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`CodecConfiguration`](../../02-数据模型/04-播放与转码.md#codecconfiguration)

---

## 2. 获取可用的视频编解码器信息

`GET` `/Encoding/CodecInformation/Video`

- **权限**：管理员令牌
- **成功响应**：`200` → `VideoCodecBase []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `VideoCodecBase []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`VideoCodecBase`](../../02-数据模型/04-播放与转码.md#videocodecbase)、[`ICodecDeviceInfo`](../../02-数据模型/03-用户与账号.md#icodecdeviceinfo)

> 该接口在官方文档中还引用了 13 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 3. 获取可用的色调映射选项

`GET` `/Encoding/ToneMapOptions`

- **权限**：管理员令牌
- **成功响应**：`200` → `ToneMapOptionsVisibility`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ToneMapOptionsVisibility` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ToneMapOptionsVisibility`](../../02-数据模型/04-播放与转码.md#tonemapoptionsvisibility)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
