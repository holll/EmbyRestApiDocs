# VideoHlsService 旧版 HLS 服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/VideoHlsService.html> ｜ 上级目录：[旧版 HLS 服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

较早的 HLS 接口路径（`/Videos/{Id}/hls/...`）。新客户端优先用 DynamicHlsService。

- 接口数量：**2**
- 覆盖范围：官方参考站该服务下的全部 2 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Audio/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}` | 获取 HLS 音频分片（旧版路径） | 用户 |
| 2 | `GET` | `/Videos/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}` | 获取 HLS 视频分片（旧版路径） | 用户 |

---

## 1. 获取 HLS 音频分片（旧版路径）

`GET` `/Audio/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `SegmentContainer` | path | string | 是 | 分片封装格式 |
| `SegmentId` | path | string | 是 | 分片序号 |
| `Id` | path | string | 是 | 条目 ID |
| `PlaylistId` | path | string | 是 | 播放列表 ID |

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

## 2. 获取 HLS 视频分片（旧版路径）

`GET` `/Videos/{Id}/hls/{PlaylistId}/{SegmentId}.{SegmentContainer}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `SegmentContainer` | path | string | 是 | 分片封装格式 |
| `SegmentId` | path | string | 是 | 分片序号 |
| `Id` | path | string | 是 | 条目 ID |
| `PlaylistId` | path | string | 是 | 播放列表 ID |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
