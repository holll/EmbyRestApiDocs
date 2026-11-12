# AudioService 音频流服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/AudioService.html> ｜ 上级目录：[音频流服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

直接以 HTTP 流输出音频：`/Audio/{Id}/stream` 系列支持直出、转码、按时间偏移起播。做纯音频播放时使用。

- 接口数量：**6**
- 覆盖范围：官方参考站该服务下的全部 6 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Audio/{Id}/{StreamFileName}` | 获取音频流 | 用户 |
| 2 | `GET` | `/Audio/{Id}/stream` | 获取音频流 | 用户 |
| 3 | `GET` | `/Audio/{Id}/stream.{Container}` | 获取音频流 | 用户 |
| 4 | `HEAD` | `/Audio/{Id}/{StreamFileName}` | 获取音频流 | 用户 |
| 5 | `HEAD` | `/Audio/{Id}/stream` | 获取音频流 | 用户 |
| 6 | `HEAD` | `/Audio/{Id}/stream.{Container}` | 获取音频流 | 用户 |

---

## 1. 获取音频流

`GET` `/Audio/{Id}/{StreamFileName}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `StreamFileName` | path | string | 是 | 路径参数 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | query | string | 否 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

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

## 2. 获取音频流

`GET` `/Audio/{Id}/stream`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | query | string | 否 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

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

## 3. 获取音频流

`GET` `/Audio/{Id}/stream.{Container}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | path | string | 是 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

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

## 4. 获取音频流

`HEAD` `/Audio/{Id}/{StreamFileName}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `StreamFileName` | path | string | 是 | 路径参数 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | query | string | 否 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

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

## 5. 获取音频流

`HEAD` `/Audio/{Id}/stream`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | query | string | 否 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

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

## 6. 获取音频流

`HEAD` `/Audio/{Id}/stream.{Container}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `DeviceProfileId` | query | string | 否 | 可选。要使用的 DLNA 设备配置文件 ID。 |
| `Id` | path | string | 是 | 条目 ID。 |
| `DeviceId` | query | string | 否 | 请求方客户端的设备 ID，用于在需要时终止转码进程。 |
| `Container` | path | string | 是 | 封装格式（如 mkv、mp4、ts）。 |
| `AudioCodec` | query | string | 否 | 可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。 |
| `EnableAutoStreamCopy` | query | boolean | 否 | 请求参数与原片一致时是否允许自动直接流复制，默认 true。 |
| `AudioSampleRate` | query | string | 否 | 可选。指定音频采样率，如 44100。 |
| `AudioBitRate` | query | integer | 否 | 可选。目标音频码率，如 128000；省略时使用编码器默认值。 |
| `AudioChannels` | query | integer | 否 | 可选。指定音频声道数，如 2。 |
| `MaxAudioChannels` | query | integer | 否 | 可选。指定最大音频声道数，如 2。 |
| `Static` | query | boolean | 否 | 可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。 |
| `CopyTimestamps` | query | string | 否 | 带偏移转码时是否复制时间戳，默认 false。 |
| `StartTimeTicks` | query | integer | 否 | 可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。 |
| `Width` | query | integer | 否 | 可选。编码视频的固定水平分辨率（宽）。 |
| `Height` | query | integer | 否 | 可选。编码视频的固定垂直分辨率（高）。 |
| `MaxWidth` | query | integer | 否 | 可选。编码视频的最大水平分辨率（宽）。 |
| `MaxHeight` | query | integer | 否 | 可选。编码视频的最大垂直分辨率（高）。 |
| `VideoBitRate` | query | integer | 否 | 可选。目标视频码率，如 500000；省略时使用编码器默认值。 |
| `SubtitleStreamIndex` | query | integer | 否 | 可选。要使用的字幕流序号；省略则不输出字幕。 |
| `SubtitleMethod` | query | string | 否 | 可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。 |
| `MaxVideoBitDepth` | query | string | 否 | 可选。 |
| `VideoCodec` | query | string | 否 | 可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。 |
| `AudioStreamIndex` | query | integer | 否 | 可选。要使用的音频流序号；省略则用第一条音频流。 |
| `VideoStreamIndex` | query | integer | 否 | 可选。要使用的视频流序号；省略则用第一条视频流。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
