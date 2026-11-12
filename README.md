# Emby REST API 中文速查手册

面向第三方客户端开发者的 Emby Server REST API 中文参考。内容依据官方文档 <https://dev.emby.media/reference/RestAPI.html> 整理，按服务分组逐条编写，覆盖官方参考站列出的全部接口。

## 这份手册怎么用

1. **第一次接入**：先读 [快速开始](00-基础/01-快速开始.md)，照着跑通登录与拉取媒体库。
2. **写代码前**：查 [常用接口速查表](00-基础/05-常用接口速查表.md)，那里是按场景组织的“最短路径”。
3. **查具体接口**：从下面的服务目录进入，每个接口都有方法、路径、权限、参数表与响应码。
4. **对不上的字段**：去 [数据模型索引](02-数据模型/00-模型索引.md) 查字段含义。

## 给 AI / 脚本的入口

本 README 面向人类读者（目录 + 说明）。如果读者是 AI 助手或脚本，先读这两个文件，别从头啃目录：

| 文件 | 用途 | 怎么用 |
|---|---|---|
| [llms.txt](llms.txt) | 一屏索引（约 18 KB）：关键约定 + 5 篇入门 + 3 篇实战 + 70 个服务入口 + 边界说明 | 直接整篇读入，按需打开对应服务页 |
| [index.json](index.json) | 机器可读目录（约 190 KB）：服务 → 文件路径，逐接口 method / path / 标题 / 权限 / 参数数 / 小节序号 | 用脚本按 path 检索，再打开对应 md 搜索「## <小节序号>. 」 |

> 单个服务页是「一个服务一篇」的自包含文档，按需读取即可，不必整库加载；接口量大的服务（LiveTv 61、Image 49、Library 31）也只读其中一节。

## 覆盖情况

| 项目 | 数量 |
|---|---|
| 服务（Controller） | 70 |
| 接口（端点） | 548 |
| 请求参数条目 | 7708 |
| 数据模型（含枚举） | 321 |
| 模型字段 | 1916 |

## 约定

- 所有接口前缀为 `http://<服务器地址>:8096`（HTTPS 默认 8920）。
- 路径中的 `{Id}`、`{UserId}` 等为占位符，实际调用需替换为真实值。
- 标注“管理员令牌”的接口需要管理员账号的 AccessToken；标注“用户令牌”的接口普通已登录用户即可。
- 返回体均为 JSON（流媒体、图片类接口除外），字段名 PascalCase，解析时请按原样大小写匹配。
- 布尔值用 `true` / `false`，时间为 ISO 8601 字符串，播放位置用 tick（1 毫秒 = 10000 ticks）。
- 参数表“类型”列以官方文档为准；官方未给出类型时按命名惯例推断（`Is*`/`Has*`/`Can*` 判为布尔，`Limit`/`StartIndex` 等判为整数），仅供参考。
- 参数表“必填”列：路径参数一律为“是”；查询参数官方未逐一标注，除说明中明确写 Required 外按“否”处理；请求体字段标“—”，表示整体以模型定义为准。
- 模型表“说明”列的 `—` 表示官方未提供该字段说明，`（原文）` 开头表示保留官方英文原文以便对照。

## 目录

### 00 基础

| 文档 | 内容 |
|---|---|
| [快速开始](00-基础/01-快速开始.md) | 地址、认证头、第一个请求、最小可运行示例 |
| [认证与鉴权](00-基础/02-认证与鉴权.md) | 登录流程、令牌传递、API Key、权限模型、常见踩坑 |
| [通用约定与响应格式](00-基础/03-通用约定与响应格式.md) | 分页、排序、Fields、图片 URL、tick 与时间 |
| [错误与排查](00-基础/04-错误与排查.md) | 状态码含义、典型报错对照表 |
| [常用接口速查表](00-基础/05-常用接口速查表.md) | 按场景列出要调哪几个接口 |

### 01 接口参考

#### 用户与认证

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [ConnectService](01-接口参考/01-用户与认证/ConnectService.md) | Emby Connect 服务 | 5 |
| [DeviceService](01-接口参考/01-用户与认证/DeviceService.md) | 设备服务 | 8 |
| [DisplayPreferencesService](01-接口参考/01-用户与认证/DisplayPreferencesService.md) | 显示偏好服务 | 5 |
| [UserNotificationsService](01-接口参考/01-用户与认证/UserNotificationsService.md) | 用户通知服务 | 2 |
| [UserService](01-接口参考/01-用户与认证/UserService.md) | 用户服务 | 25 |

#### 媒体库浏览

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [ArtistsService](01-接口参考/02-媒体库浏览/ArtistsService.md) | 艺术家服务 | 3 |
| [ChannelService](01-接口参考/02-媒体库浏览/ChannelService.md) | 频道服务 | 1 |
| [CollectionService](01-接口参考/02-媒体库浏览/CollectionService.md) | 合集（BoxSet）服务 | 6 |
| [ContentService](01-接口参考/02-媒体库浏览/ContentService.md) | 首页内容服务 | 5 |
| [GameGenresService](01-接口参考/02-媒体库浏览/GameGenresService.md) | 游戏类型服务 | 2 |
| [GenresService](01-接口参考/02-媒体库浏览/GenresService.md) | 类型（Genre）服务 | 2 |
| [InstantMixService](01-接口参考/02-媒体库浏览/InstantMixService.md) | 即时混播服务 | 8 |
| [ItemsService](01-接口参考/02-媒体库浏览/ItemsService.md) | 媒体条目查询服务 | 3 |
| [LibraryService](01-接口参考/02-媒体库浏览/LibraryService.md) | 媒体库服务 | 31 |
| [MoviesService](01-接口参考/02-媒体库浏览/MoviesService.md) | 电影服务 | 1 |
| [MusicGenresService](01-接口参考/02-媒体库浏览/MusicGenresService.md) | 音乐类型服务 | 2 |
| [PersonsService](01-接口参考/02-媒体库浏览/PersonsService.md) | 人物服务 | 3 |
| [PlaylistService](01-接口参考/02-媒体库浏览/PlaylistService.md) | 播放列表服务 | 7 |
| [StudiosService](01-接口参考/02-媒体库浏览/StudiosService.md) | 工作室服务 | 2 |
| [SuggestionsService](01-接口参考/02-媒体库浏览/SuggestionsService.md) | 推荐服务 | 1 |
| [TagService](01-接口参考/02-媒体库浏览/TagService.md) | 标签服务 | 14 |
| [TrailersService](01-接口参考/02-媒体库浏览/TrailersService.md) | 预告片服务 | 1 |
| [TvShowsService](01-接口参考/02-媒体库浏览/TvShowsService.md) | 剧集服务 | 5 |
| [UserLibraryService](01-接口参考/02-媒体库浏览/UserLibraryService.md) | 用户媒体库服务 | 20 |
| [UserViewsService](01-接口参考/02-媒体库浏览/UserViewsService.md) | 用户视图服务 | 1 |
| [VideosService](01-接口参考/02-媒体库浏览/VideosService.md) | 视频条目服务 | 3 |

#### 媒体库维护

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [ItemLookupService](01-接口参考/03-媒体库维护/ItemLookupService.md) | 远程元数据检索服务 | 14 |
| [ItemRefreshService](01-接口参考/03-媒体库维护/ItemRefreshService.md) | 条目刷新服务 | 1 |
| [ItemUpdateService](01-接口参考/03-媒体库维护/ItemUpdateService.md) | 条目更新服务 | 2 |
| [LibraryStructureService](01-接口参考/03-媒体库维护/LibraryStructureService.md) | 媒体库结构维护服务 | 10 |

#### 播放与同步

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [MediaInfoService](01-接口参考/04-播放与同步/MediaInfoService.md) | 播放信息与媒体源服务 | 6 |
| [PartyService](01-接口参考/04-播放与同步/PartyService.md) | 派对（一起看）服务 | 7 |
| [PlaystateService](01-接口参考/04-播放与同步/PlaystateService.md) | 播放状态上报服务 | 12 |
| [SessionsService](01-接口参考/04-播放与同步/SessionsService.md) | 会话与远程控制服务 | 20 |
| [SyncService](01-接口参考/04-播放与同步/SyncService.md) | 离线同步服务 | 25 |

#### 流媒体协议

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [AudioService](01-接口参考/05-流媒体协议/AudioService.md) | 音频流服务 | 6 |
| [DynamicHlsService](01-接口参考/05-流媒体协议/DynamicHlsService.md) | 动态 HLS 服务 | 14 |
| [HlsSegmentService](01-接口参考/05-流媒体协议/HlsSegmentService.md) | HLS 编码任务服务 | 2 |
| [UniversalAudioService](01-接口参考/05-流媒体协议/UniversalAudioService.md) | 通用音频服务 | 4 |
| [VideoHlsService](01-接口参考/05-流媒体协议/VideoHlsService.md) | 旧版 HLS 服务 | 2 |
| [VideoService](01-接口参考/05-流媒体协议/VideoService.md) | 视频流服务 | 6 |

#### 图片与字幕

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [BifService](01-接口参考/06-图片与字幕/BifService.md) | BIF 缩略图服务 | 2 |
| [BrandingService](01-接口参考/06-图片与字幕/BrandingService.md) | 品牌配置服务 | 3 |
| [ImageService](01-接口参考/06-图片与字幕/ImageService.md) | 图片服务 | 49 |
| [RemoteImageService](01-接口参考/06-图片与字幕/RemoteImageService.md) | 远程图片服务 | 4 |
| [SubtitleOptionsService](01-接口参考/06-图片与字幕/SubtitleOptionsService.md) | 字幕选项服务 | 2 |
| [SubtitleService](01-接口参考/06-图片与字幕/SubtitleService.md) | 字幕服务 | 16 |

#### 直播电视

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [LiveStreamService](01-接口参考/07-直播电视/LiveStreamService.md) | 直播流服务 | 14 |
| [LiveTvService](01-接口参考/07-直播电视/LiveTvService.md) | 直播电视服务 | 61 |

#### 系统与运维

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [ActivityLogService](01-接口参考/08-系统与运维/ActivityLogService.md) | 活动日志服务 | 1 |
| [BackupApi](01-接口参考/08-系统与运维/BackupApi.md) | 备份还原接口 | 3 |
| [CodecParameterService](01-接口参考/08-系统与运维/CodecParameterService.md) | 编码参数服务 | 2 |
| [ConfigurationService](01-接口参考/08-系统与运维/ConfigurationService.md) | 配置服务 | 5 |
| [EncodingInfoService](01-接口参考/08-系统与运维/EncodingInfoService.md) | 编码信息服务 | 3 |
| [EnvironmentService](01-接口参考/08-系统与运维/EnvironmentService.md) | 环境服务 | 8 |
| [FeatureService](01-接口参考/08-系统与运维/FeatureService.md) | 功能特性服务 | 1 |
| [FfmpegOptionsService](01-接口参考/08-系统与运维/FfmpegOptionsService.md) | FFmpeg 选项服务 | 2 |
| [GenericUIApiService](01-接口参考/08-系统与运维/GenericUIApiService.md) | 通用 UI 接口服务 | 2 |
| [LocalizationService](01-接口参考/08-系统与运维/LocalizationService.md) | 本地化服务 | 4 |
| [NotificationsService](01-接口参考/08-系统与运维/NotificationsService.md) | 管理员通知服务 | 2 |
| [OfficialRatingService](01-接口参考/08-系统与运维/OfficialRatingService.md) | 分级服务 | 1 |
| [OpenApiService](01-接口参考/08-系统与运维/OpenApiService.md) | OpenAPI 规范服务 | 4 |
| [PackageService](01-接口参考/08-系统与运维/PackageService.md) | 插件包服务 | 6 |
| [PluginService](01-接口参考/08-系统与运维/PluginService.md) | 插件服务 | 6 |
| [ScheduledTaskService](01-接口参考/08-系统与运维/ScheduledTaskService.md) | 计划任务服务 | 6 |
| [SystemService](01-接口参考/08-系统与运维/SystemService.md) | 系统服务 | 14 |
| [ToneMapOptionsService](01-接口参考/08-系统与运维/ToneMapOptionsService.md) | 色调映射选项服务 | 4 |
| [WebAppService](01-接口参考/08-系统与运维/WebAppService.md) | Web 前端资源服务 | 4 |

#### DLNA

| 服务 | 中文名 | 接口数 |
|---|---|---|
| [DlnaServerService](01-接口参考/09-DLNA/DlnaServerService.md) | DLNA 服务器服务 | 16 |
| [DlnaService](01-接口参考/09-DLNA/DlnaService.md) | DLNA 管理服务 | 6 |

### 02 数据模型

| 文档 | 内容 |
|---|---|
| [模型索引](02-数据模型/00-模型索引.md) | 全部 321 个模型的总索引 |
| [通用结构](02-数据模型/01-通用结构.md) | 通用结构 |
| [媒体条目](02-数据模型/02-媒体条目.md) | 媒体条目 |
| [用户与账号](02-数据模型/03-用户与账号.md) | 用户与账号 |
| [播放与转码](02-数据模型/04-播放与转码.md) | 播放与转码 |
| [直播电视](02-数据模型/05-直播电视.md) | 直播电视 |
| [系统与配置](02-数据模型/06-系统与配置.md) | 系统与配置 |

### 03 实战示例

| 文档 | 内容 |
|---|---|
| [从登录到播放](03-实战示例/01-从登录到播放.md) | 完整链路：认证 → 视图 → 列表 → 详情 → 播放地址 → 进度上报 |
| [图片与列表页优化](03-实战示例/02-图片与列表页优化.md) | 图片 URL 拼装、尺寸与缓存策略 |
| [远程控制与投屏](03-实战示例/03-远程控制与投屏.md) | 会话发现、下发播放命令、轮询状态 |

## 生成与校验

接口清单由 `tools/crawl_emby_api.py` 从官方参考站抓取（结果落在 `tools/_data/`），`tools/build_docs.py` 依据数据与中文词表生成全部 Markdown，`tools/check_docs.py` 做交付校验。

```text
python tools\crawl_emby_api.py   # 重新抓取官方接口（可选）
python tools\build_docs.py      # 重新生成文档（会覆盖自动生成的文件）
python tools\build_ai_index.py  # 生成 llms.txt 与 index.json（AI / 脚本入口）
python tools\check_docs.py      # 校验：接口数/参数表/模型/断链/未打钩项/AI 入口
```

最近一次校验结果：服务 70、接口 548、参数条目 7708、模型 321、Markdown 96 个文件，另有 `llms.txt`（约 18 KB）与 `index.json`（约 190 KB）两个机器入口；无断链、无未打钩项。

> 手写文档（`00-基础/`、`03-实战示例/`）不会被 `build_docs.py` 覆盖；`进度清单.md` 会在每次生成时按文件是否存在自动打钩。

> 本手册为社区整理的中文参考资料，官方文档为唯一权威来源。接口行为随服务器版本变化，以实际请求结果为准。
