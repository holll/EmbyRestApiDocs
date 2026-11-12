# 流媒体协议

> [返回总目录](../../README.md)

| 服务 | 中文名 | 接口数 | 说明 |
|---|---|---|---|
| [AudioService](AudioService.md) | 音频流服务 | 6 | 直接以 HTTP 流输出音频 |
| [DynamicHlsService](DynamicHlsService.md) | 动态 HLS 服务 | 14 | 按需切片的自适应 HLS |
| [HlsSegmentService](HlsSegmentService.md) | HLS 编码任务服务 | 2 | 管理正在进行的 HLS 编码任务 |
| [UniversalAudioService](UniversalAudioService.md) | 通用音频服务 | 4 | 按“通用音频”路径输出音频流，常用于有声书、播客等场景。 |
| [VideoHlsService](VideoHlsService.md) | 旧版 HLS 服务 | 2 | 较早的 HLS 接口路径（`/Videos/{Id}/hls/...`）。新客户 |
| [VideoService](VideoService.md) | 视频流服务 | 6 | 直接以 HTTP 流输出视频 |
