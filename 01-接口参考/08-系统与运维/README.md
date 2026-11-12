# 系统与运维

> [返回总目录](../../README.md)

| 服务 | 中文名 | 接口数 | 说明 |
|---|---|---|---|
| [ActivityLogService](ActivityLogService.md) | 活动日志服务 | 1 | 读取服务器活动日志（登录、播放、扫描等事件），支持按时间与分页过滤。 |
| [BackupApi](BackupApi.md) | 备份还原接口 | 3 | 服务器配置备份与还原。官方参考站未提供该组接口的详情页，本文档按标签页信息整理， |
| [CodecParameterService](CodecParameterService.md) | 编码参数服务 | 2 | 读取/更新指定编码器的参数（如 H.264 的预设、CRF）。 |
| [ConfigurationService](ConfigurationService.md) | 配置服务 | 5 | 读写服务器配置 |
| [EncodingInfoService](EncodingInfoService.md) | 编码信息服务 | 3 | 查询服务器可用的视频编解码器与色调映射能力，决定客户端能请求哪些转码参数。 |
| [EnvironmentService](EnvironmentService.md) | 环境服务 | 8 | 服务器运行环境 |
| [FeatureService](FeatureService.md) | 功能特性服务 | 1 | 返回服务器已启用的功能特性列表（如是否支持 HLS、Sync 等）。 |
| [FfmpegOptionsService](FfmpegOptionsService.md) | FFmpeg 选项服务 | 2 | 读取/更新 FFmpeg 相关选项（编码器路径、线程数等）。 |
| [GenericUIApiService](GenericUIApiService.md) | 通用 UI 接口服务 | 2 | 为 Web 端 UI 提供聚合数据与命令执行（如电视设置向导中的命令）。 |
| [LocalizationService](LocalizationService.md) | 本地化服务 | 4 | 获取国家/地区、区域文化、家长分级、本地化选项，用于语言与分级下拉框。 |
| [NotificationsService](NotificationsService.md) | 管理员通知服务 | 2 | 管理员群发通知 |
| [OfficialRatingService](OfficialRatingService.md) | 分级服务 | 1 | 获取服务器已知的官方分级（PG、R、TV-MA 等），用于筛选器。 |
| [OpenApiService](OpenApiService.md) | OpenAPI 规范服务 | 4 | 直接输出服务器的 OpenAPI/Swagger 规范，可用于自动生成客户端 S |
| [PackageService](PackageService.md) | 插件包服务 | 6 | 插件市场 |
| [PluginService](PluginService.md) | 插件服务 | 6 | 已安装插件的配置读取/写入、插件缩略图、卸载插件。 |
| [ScheduledTaskService](ScheduledTaskService.md) | 计划任务服务 | 6 | 服务器内置计划任务 |
| [SystemService](SystemService.md) | 系统服务 | 14 | 服务器级信息与运维 |
| [ToneMapOptionsService](ToneMapOptionsService.md) | 色调映射选项服务 | 4 | 读取/更新 HDR→SDR 的色调映射选项。 |
| [WebAppService](WebAppService.md) | Web 前端资源服务 | 4 | Web 管理界面用的配置页面与界面文案接口。第三方客户端一般不需要。 |
