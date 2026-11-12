# -*- coding: utf-8 -*-
"""模型字段说明的中文转换。

官方模型说明高度模板化（The xxx. / A value indicating whether ...），
这里用「句式规则 + 词表构词」生成中文，未命中的条目保留原文并标记。
"""
import re

from zh_notes import NOTE, PNOTE_EMPTY

# 名词/形容词词表：英文小写 -> 中文
WORD = {
    "id": "ID", "identifier": "标识", "identifiers": "标识", "unique": "唯一",
    "name": "名称", "names": "名称", "title": "标题", "sort": "排序",
    "type": "类型", "types": "类型", "kind": "种类", "class": "类",
    "value": "值", "values": "值", "number": "编号", "count": "数量",
    "total": "总", "record": "记录", "records": "记录",
    "item": "条目", "items": "条目", "entry": "条目",
    "media": "媒体", "stream": "流", "streams": "流",
    "source": "源", "sources": "源", "version": "版本", "versions": "版本",
    "path": "路径", "paths": "路径", "filename": "文件名", "file": "文件",
    "url": "URL", "urls": "URL", "uri": "URI", "endpoint": "端点",
    "key": "键", "token": "令牌", "secret": "密钥", "guid": "GUID",
    "etag": "ETag", "hash": "哈希", "checksum": "校验值",
    "date": "日期", "time": "时间", "created": "创建", "modified": "修改",
    "last": "最后", "start": "开始", "end": "结束", "duration": "时长",
    "year": "年份", "month": "月", "day": "日", "days": "天",
    "hour": "小时", "minute": "分钟", "second": "秒", "seconds": "秒",
    "ticks": "tick", "tick": "tick", "utc": "UTC", "local": "本地",
    "timezone": "时区", "expiration": "过期", "interval": "间隔",
    "position": "位置", "progress": "进度", "percent": "百分比",
    "percentage": "百分比", "complete": "完成", "completion": "完成度",
    "status": "状态", "state": "状态", "result": "结果", "success": "成功",
    "error": "错误", "message": "消息", "level": "级别", "severity": "严重程度",
    "priority": "优先级", "order": "顺序", "index": "索引", "indices": "索引",
    "size": "大小", "width": "宽度", "height": "高度", "resolution": "分辨率",
    "aspect": "宽高比", "ratio": "比率", "rate": "速率", "bit": "位",
    "bitrate": "码率", "bitdepth": "位深", "depth": "深度",
    "frame": "帧", "framerate": "帧率", "sample": "采样", "channel": "声道",
    "channels": "声道", "layout": "布局", "codec": "编码", "codecs": "编码",
    "profile": "配置", "profiles": "配置", "level_": "级别",
    "language": "语言", "languages": "语言", "country": "国家/地区",
    "code": "代码", "codes": "代码", "locale": "区域设置",
    "region": "地区", "culture": "文化", "metadata": "元数据",
    "provider": "提供方", "providers": "提供方", "preferred": "首选",
    "image": "图片", "images": "图片", "tag": "标记", "tags": "标记",
    "backdrop": "背景图", "logo": "Logo", "thumb": "缩略图",
    "primary": "主", "parent": "父级", "child": "子级", "children": "子级",
    "album": "专辑", "albums": "专辑", "artist": "艺术家", "artists": "艺术家",
    "genre": "类型", "genres": "类型", "studio": "工作室", "studios": "工作室",
    "person": "人物", "people": "人物", "actor": "演员", "role": "角色",
    "series": "剧集", "season": "季", "seasons": "季", "episode": "集",
    "episodes": "集", "movie": "电影", "movies": "电影", "video": "视频",
    "audio": "音频", "subtitle": "字幕", "subtitles": "字幕", "trailer": "预告片",
    "chapter": "章节", "chapters": "章节", "part": "分段", "parts": "分段",
    "playlist": "播放列表", "collection": "合集", "library": "媒体库",
    "folder": "文件夹", "extension": "扩展名", "container": "封装格式",
    "cache": "缓存", "display": "显示", "view": "视图", "section": "分区",
    "sections": "分区", "page": "页面", "dashboard": "控制台",
    "server": "服务器", "client": "客户端", "device": "设备", "app": "应用",
    "application": "应用", "user": "用户", "users": "用户", "session": "会话",
    "play": "播放", "playback": "播放", "played": "播放", "player": "播放器",
    "record": "录制", "recording": "录制", "recordings": "录制",
    "program": "节目", "channel": "频道", "live": "直播", "timer": "定时器",
    "tuner": "调谐器", "listing": "节目单", "guide": "节目单",
    "direct": "直接", "transcoding": "转码", "transcode": "转码",
    "rule": "规则", "sub": "子", "description": "描述", "comment": "备注",
    "overview": "简介", "short": "简短", "summary": "摘要", "note": "备注",
    "category": "分类", "rating": "分级", "score": "评分", "vote": "投票",
    "community": "社区", "critic": "影评人", "official": "官方",
    "custom": "自定义", "parental": "家长", "max": "最大", "min": "最小",
    "maximum": "最大", "minimum": "最小", "average": "平均",
    "cpu": "CPU", "memory": "内存", "virtual": "虚拟", "working": "工作",
    "set": "集", "port": "端口", "http": "HTTP", "https": "HTTPS",
    "address": "地址", "wan": "广域网", "proxy": "代理", "prefix": "前缀",
    "public": "公开", "private": "私有", "internal": "内部",
    "external": "外部", "network": "网络", "share": "共享",
    "location": "位置", "locations": "位置", "marker": "标记",
    "logo": "Logo", "tile": "磁贴", "color": "颜色", "css": "CSS",
    "icon": "图标", "feature": "功能", "package": "包", "plugin": "插件",
    "assembly": "程序集", "installs": "安装次数", "install": "安装",
    "price": "价格", "premium": "高级", "registered": "已注册",
    "target": "目标", "trigger": "触发器", "triggers": "触发器",
    "task": "任务", "tasks": "任务", "log": "日志", "backup": "备份",
    "restore": "还原", "dlna": "DLNA", "event": "事件", "activity": "活动",
    "notification": "通知", "capabilities": "能力", "command": "命令",
    "request": "请求", "response": "响应", "query": "查询", "filter": "过滤",
    "filter_": "过滤", "search": "搜索", "condition": "条件",
    "conditions": "条件", "property": "属性", "properties": "属性",
    "data": "数据", "info": "信息", "information": "信息", "option": "选项",
    "options": "选项", "setting": "设置", "settings": "设置",
    "configuration": "配置", "config": "配置", "default": "默认",
    "enabled": "启用", "disabled": "禁用", "hidden": "隐藏", "visible": "可见",
    "locked": "锁定", "lockedfields": "锁定字段", "required": "必需",
    "repeat": "循环", "shuffle": "随机", "chapter": "章节",
    "movie": "电影", "series": "剧集", "news": "新闻", "kids": "儿童",
    "sports": "体育", "premiere": "首播", "isnew": "新增",
    "anamorphic": "变形宽银幕", "interlaced": "隔行扫描", "forced": "强制",
    "hearingimpaired": "听障", "muted": "静音", "paused": "暂停",
    "seek": "拖动进度", "administrator": "管理员", "firstrun": "首次运行",
    "restart": "重启", "update": "更新", "updates": "更新",
    "available": "可用", "pending": "待处理", "configured": "已配置",
    "password": "密码", "pin": "PIN", "authorized": "已授权",
    "padding": "缓冲", "pre": "前置", "post": "后置", "air": "播出",
    "broadcast": "播出", "studio": "工作室", "titles": "标题",
    "taglines": "宣传语", "credits": "演职人员", "imageurl": "图片 URL",
    "original": "原始", "extra": "额外", "presentation": "展示",
    "physical": "物理", "quality": "质量", "format": "格式",
    "encoding": "编码", "decoder": "解码器", "encoder": "编码器",
    "relative": "相对", "absolute": "绝对", "full": "完整",
    "primaryimage": "主图", "backdropimage": "背景图",
    "parentid": "父级 ID", "seriesid": "剧集 ID", "seasonid": "季 ID",
    "userid": "用户 ID", "itemid": "条目 ID", "deviceid": "设备 ID",
    "sessionid": "会话 ID", "serverid": "服务器 ID", "playlistid": "播放列表 ID",
    "channelid": "频道 ID", "timerid": "定时器 ID", "programid": "节目 ID",
    "mediasourceid": "媒体源 ID", "livesreamid": "直播流 ID",
    "baseurl": "基础 URL", "uri": "URI", "host": "主机",
    "port": "端口", "protocol": "协议", "subprotocol": "子协议",
    "apikey": "API 密钥", "accesstoken": "访问令牌",
    "datetime": "日期时间", "timestamp": "时间戳",
    "isactive": "是否活跃", "isdefault": "是否默认",
    "isofficial": "是否官方", "iscustom": "是否自定义",
    "supports": "是否支持", "allowed": "允许", "blocked": "禁止",
}

SPECIAL = {
    "a value indicating whether": "指示是否",
}

# 罕见但常见的整句说明
SENTENCE = {
    "A unique identifier.": "唯一标识。",
    "Class ThemeMediaResult": "类：ThemeMediaResult（主题媒体查询结果）。",
    "Deprecated, please use ProcessStatistics instead": "已弃用，请改用 ProcessStatistics。",
    "Used only by our Windows app. Not used by Emby Server.": "仅 Windows 客户端使用，服务器不使用。",
    "This is for webhooks since this will cause xml serialization to fail": "供 Webhook 使用（该字段会导致 XML 序列化失败，故单独处理）。",
    "This is strictly used as a data transfer object from the api layer. This holds information about a BaseItem in a format that is convenient for the client.":
        "纯 API 传输对象：以方便客户端消费的形式承载媒体条目的信息。",
    "Use language instead to return the language specified by the subtitle provider":
        "请改用 language 字段返回字幕提供方给出的语言。",
    "ItemId came first, so that is left for compatability purposes": "ItemId 出现更早，保留仅为兼容。",
    "If the item does not have a logo, this will hold the Id of the Parent that has one.":
        "若条目自身没有 Logo，此字段保存拥有 Logo 的父级条目 ID。",
    "If the item does not have any backdrops, this will hold the Id of the Parent that has one.":
        "若条目自身没有背景图，此字段保存拥有背景图的父级条目 ID。",
    "Notification intended for a specific user": "面向单个用户的通知。",
    "Differentiate internet url vs local network": "用于区分外网地址与局域网地址。",
    "Enable automatically and silently updating of the application": "是否自动静默更新应用。",
    "Limit events based on user ids, for admin notifications": "按用户 ID 过滤事件（管理员通知用）。",
    "Words to be removed from strings to create a sort name": "生成排序名时需要从名称中剔除的词。",
    "Whether or not this package is registered.": "该包是否已注册。",
    "Id of the page controller": "页面控制器 ID。",
    "Id of the recording.": "录制项 ID。",
    "ChannelId of the recording.": "录制项的频道 ID。",
    "ChannelName of the recording.": "录制项的频道名称。",
    "Description of the recording.": "录制项的描述。",
    "The start date of the recording, in UTC.": "录制开始时间（UTC）。",
    "The end date of the recording, in UTC.": "录制结束时间（UTC）。",
    "A single string from the Emby.Media.Model.Types.LevelInformation.ResolutionRateStrings list.":
        "取自 LevelInformation.ResolutionRateStrings 的单个字符串。",
    "A display value of the Emby.Media.Model.Types.LevelInformation.MaxBitRate property.":
        "LevelInformation.MaxBitRate 的展示用文本。",
    "Examples for the maximum supported combinations of resolution and rate for this level.":
        "该级别支持的最大分辨率与帧率组合示例。",
    "Examples for the maximum supported combinations of resolution and rate for this level as string values.":
        "该级别支持的最大分辨率与帧率组合示例（字符串形式）。",
    "Enum defining the kind of media a codec is processing.": "枚举：编码器处理的媒体种类。",
    "Enum for indicating the processing direction of a codec.": "枚举：编码器的处理方向（编码/解码）。",
    "Enum defining secondary frameworks for encoding and decoding. While most of these are hardware acceleration frameworks, this is not a necessity (e.g. Android MediaCodec offers software codecs as well).":
        "枚举：编解码所用的次级框架，多为硬件加速框架，也包含软件实现（如 Android MediaCodec）。",
    "Enum listing video media types. The enum member names are matching exactly those that are used by ffmpeg. Exception: Items that are starting with a number are prefixed with an underscore here.":
        "枚举：视频媒体类型，取值与 ffmpeg 一致；以数字开头的项在此以 `_` 前缀表示。",
    "Conditions for comparing with a target value.": "与目标值比较的条件。",
    "Conditions on the source value.": "针对源值的条件。",
    "Class for unified presentation of all information associated with a specific codec level.":
        "类：统一描述某个编码级别的全部信息。",
    "Class for unified presentation of all information associated with a specific codec profile.":
        "类：统一描述某个编码配置的全部信息。",
    "Class SessionInfo": "类：SessionInfo（会话信息）。",
    "Class TaskExecutionInfo": "类：TaskExecutionInfo（任务执行信息）。",
    "Class UserConfiguration": "类：UserConfiguration（用户配置）。",
    "Class UserDto": "类：UserDto（用户）。",
    "Class UserItemDataDto": "类：UserItemDataDto（条目的用户数据）。",
    "Interface IPlugin": "接口：IPlugin（插件）。",
    "Enum ConfigurationPageType": "枚举：配置页面类型。",
    "Enum ImageType": "枚举：图片类型。",
    "Enum LocationType": "枚举：位置类型。",
    "Enum LogSeverity": "枚举：日志级别。",
    "Enum PackageType": "枚举：包类型。",
    "Enum PackageVersionClass": "枚举：包版本通道。",
    "Enum PlaystateCommand": "枚举：播放状态命令。",
    "Enum SortOrder": "枚举：排序方向。",
    "Enum SystemEvent": "枚举：系统事件。",
    "Enum TaskCompletionStatus": "枚举：任务完成状态。",
    "Enum TaskState": "枚举：任务状态。",
    "A value indicating whether this instance is anamorphic.": "指示该视频是否为变形宽银幕。",
    "A value indicating whether this instance has configured password.": "指示是否已设置密码。",
    "A value indicating whether this instance has password.": "指示是否存在密码。",
    "A value indicating whether this instance can self restart.": "指示是否支持自重启。",
    "A value indicating whether this instance can self update.": "指示是否支持自更新。",
    "A value indicating whether this instance has pending restart.": "指示是否有待执行的重启。",
    "A value indicating whether this instance has update available.": "指示是否有可用更新。",
    "The maximum percentage of an item that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched.":
        "允许保留播放进度时最多可播放的比例；超过此比例会把进度重置为开头，并把条目标记为已观看。",
    "The minimum percentage of an item that must be played in order for playstate to be updated.":
        "更新播放进度前必须至少播放的比例。",
    "The minimum duration that an item must have in order to be eligible for playstate updates..":
        "条目参与播放进度更新的最小时长。",
    "The delay in seconds that we will wait after a file system change to try and discover what has been added/removed Some delay is necessary with some items because their creation is not atomic. It involves the creation of several different directories and files.":
        "文件系统变化后等待的秒数，用于识别新增/删除内容。部分条目创建过程非原子（涉及多个目录和文件），因此需要延迟。",
    "The number of days we should retain log files": "日志文件保留天数。",
    "The full path to the data folder, where the plugin can store any miscellaneous files needed":
        "插件存放杂项文件的数据目录完整路径。",
    "The value pointing to the file system where the ssl certiifcate is located..": "SSL 证书所在路径。",
    "The path to the assembly file": "程序集文件路径。",
}


def _words():
    return WORD


# 高频字段的固定中文名（官方未给说明时使用，保证核心模型表的可读性）
FIELDS = {
    "Id": "唯一标识",
    "Name": "名称",
    "ServerId": "所属服务器 ID",
    "Etag": "缓存标记（内容变化时会变）",
    "Prefix": "名称前缀（用于排序）",
    "Guid": "GUID",
    "DateCreated": "入库时间",
    "DateModified": "最后修改时间",
    "Path": "文件路径",
    "Overview": "简介",
    "OfficialRating": "官方分级",
    "CustomRating": "自定义分级",
    "CommunityRating": "社区评分",
    "CriticRating": "影评人评分",
    "ProductionYear": "制作年份",
    "PremiereDate": "首播日期",
    "EndDate": "结束日期",
    "RunTimeTicks": "时长（tick）",
    "IndexNumber": "集数/序号",
    "ParentIndexNumber": "季数/父级序号",
    "IndexNumberEnd": "结束集数",
    "ParentId": "父级 ID",
    "SeriesId": "所属剧集 ID",
    "SeriesName": "所属剧集名称",
    "SeasonId": "所属季 ID",
    "SeasonName": "所属季名称",
    "AlbumId": "所属专辑 ID",
    "Album": "专辑名",
    "AlbumArtist": "专辑艺术家",
    "AlbumArtists": "专辑艺术家列表",
    "Artists": "艺术家列表",
    "ArtistItems": "艺术家（带 ID）",
    "Genres": "类型列表",
    "GenreItems": "类型（带 ID）",
    "Tags": "标签列表",
    "TagItems": "标签（带 ID）",
    "Studios": "工作室列表",
    "People": "演职人员列表",
    "Chapters": "章节列表",
    "MediaSources": "媒体源列表",
    "MediaStreams": "媒体流列表",
    "MediaSourceId": "媒体源 ID",
    "MediaType": "媒体类型（Video / Audio / Photo…）",
    "Type": "条目类型（Movie / Series / Episode…）",
    "CollectionType": "媒体库类型（movies / tvshows / music…）",
    "IsFolder": "是否为文件夹",
    "IsFavorite": "是否已收藏",
    "Played": "是否已播放",
    "PlayCount": "播放次数",
    "LastPlayedDate": "最后播放时间",
    "UserData": "该用户的用户数据",
    "PrimaryImageTag": "主图标记（有值表示有主图）",
    "PrimaryImageItemId": "主图所属条目 ID",
    "PrimaryImageAspectRatio": "主图宽高比",
    "BackdropImageTags": "背景图标记列表",
    "ParentBackdropImageTags": "父级背景图标记列表",
    "ParentBackdropItemId": "父级背景图所属条目 ID",
    "ImageTags": "图片标记表（类型 → 标记）",
    "SeriesPrimaryImageTag": "剧集主图标记",
    "ParentLogoImageTag": "父级 Logo 标记",
    "ParentThumbItemId": "父级缩略图所属条目 ID",
    "ParentThumbImageTag": "父级缩略图标记",
    "ParentLogoItemId": "父级 Logo 所属条目 ID",
    "ChildCount": "子条目数量",
    "RecursiveItemCount": "含子级的条目总数",
    "SpecialFeatureCount": "特别收录数量",
    "LocalTrailerCount": "本地预告片数量",
    "MovieCount": "电影数量",
    "SeriesCount": "剧集数量",
    "EpisodeCount": "集数",
    "SeasonCount": "季数",
    "SongCount": "歌曲数量",
    "AlbumCount": "专辑数量",
    "ArtistCount": "艺术家数量",
    "GameCount": "游戏数量",
    "GameSystemCount": "游戏平台数量",
    "AlbumArtistCount": "专辑艺术家数量",
    "BookCount": "书籍数量",
    "BoxSetCount": "合集数量",
    "MusicVideoCount": "音乐视频数量",
    "PartCount": "分段数量",
    "ProviderIds": "外部 ID 表（Imdb / Tmdb / Tvdb…）",
    "ExternalUrls": "外部链接列表",
    "Taglines": "宣传语列表",
    "RemoteTrailers": "远程预告片列表",
    "LockedFields": "被锁定的元数据字段",
    "LockData": "是否锁定元数据",
    "CanDelete": "是否允许删除",
    "CanDownload": "是否允许下载",
    "CanEditItems": "是否允许编辑子条目",
    "SupportsSync": "是否支持离线同步",
    "SyncStatus": "同步状态",
    "LocationType": "存储位置类型（FileSystem / Remote / Virtual…）",
    "MediaStreams ": "媒体流列表",
    "VideoType": "视频来源类型（Dvd / BluRay / Iso…）",
    "Video3DFormat": "3D 格式",
    "Container": "封装格式",
    "Bitrate": "码率",
    "Size": "文件大小（字节）",
    "Width": "宽度",
    "Height": "高度",
    "VideoCodec": "视频编码",
    "AudioCodec": "音频编码",
    "AverageFrameRate": "平均帧率",
    "RealFrameRate": "实际帧率",
    "IsHD": "是否高清",
    "IsAnamorphic": "是否变形宽银幕",
    "IsInterlaced": "是否隔行扫描",
    "IsDefault": "是否默认轨道",
    "IsForced": "是否强制字幕",
    "IsExternal": "是否外部资源",
    "IsExternalUrl": "是否为外部 URL",
    "IsTextSubtitleStream": "是否为文本字幕",
    "SupportsExternalStream": "是否支持外部流",
    "DisplayTitle": "展示标题（客户端可直接显示）",
    "DisplayLanguage": "展示语言",
    "Language": "语言",
    "Codec": "编码",
    "CodecTag": "编码标记",
    "Profile": "编码配置（Profile）",
    "Level": "编码级别（Level）",
    "ChannelLayout": "声道布局",
    "Channels": "声道数",
    "SampleRate": "采样率",
    "BitDepth": "位深",
    "ColorSpace": "色彩空间",
    "ColorTransfer": "色彩传递特性",
    "ColorPrimaries": "色彩原色",
    "PixelFormat": "像素格式",
    "RefFrames": "参考帧数",
    "TimeBase": "时间基准",
    "StartTime": "流开始时间",
    "AttachmentSize": "附件大小",
    "Comment": "备注",
    "Title": "标题",
    "UserName": "用户名",
    "UserPrimaryImageTag": "用户头像标记",
    "ConnectUserName": "Connect 用户名",
    "HasPassword": "是否设置了密码",
    "HasConfiguredPassword": "是否已配置密码",
    "IsAdministrator": "是否为管理员",
    "IsDisabled": "是否已禁用",
    "IsHidden": "是否隐藏",
    "IsGuest": "是否为访客",
    "IsPremium": "是否为高级会员",
    "LastLoginDate": "最后登录时间",
    "LastActivityDate": "最后活动时间",
    "Policy": "权限策略",
    "Configuration": "用户配置",
    "DeviceName": "设备名称",
    "AppName": "应用名称",
    "AppVersion": "应用版本",
    "Client": "客户端标识",
    "DeviceId": "设备 ID",
    "DeviceType": "设备类型",
    "NowPlayingItem": "当前播放条目",
    "PlayState": "播放状态",
    "PlayableMediaTypes": "可播放的媒体类型",
    "SupportedCommands": "支持的远程控制命令",
    "SupportsMediaControl": "是否支持远程控制",
    "SupportsRemoteControl": "是否支持被远程控制",
    "Capabilities": "客户端能力",
    "TranscodingInfo": "转码信息",
    "PlaySessionId": "播放会话 ID",
    "PlayMethod": "播放方式",
    "RepeatMode": "循环模式",
    "PlaybackRate": "播放速率",
    "VolumeLevel": "音量（0–100）",
    "PositionTicks": "当前位置（tick）",
    "IsPaused": "是否暂停",
    "IsMuted": "是否静音",
    "CanSeek": "是否可拖动进度",
    "ItemId": "条目 ID",
    "ItemName": "条目名称",
    "ItemType": "条目类型",
    "MediaVersionId": "媒体版本 ID",
    "MediaVersions": "媒体版本列表",
    "NowPlayingPositionTicks": "当前播放位置（tick）",
    "NowPlayingMediaVersionId": "当前播放的媒体版本 ID",
    "ControllingUserId": "控制方用户 ID",
}


def split_camel(name):
    return re.findall(r"[A-Z]+(?![a-z])|[A-Z][a-z0-9]*|[a-z0-9]+", name)


def gloss_from_name(name):
    if name in FIELDS:
        return FIELDS[name]
    parts = split_camel(name)
    if not parts:
        return None
    trans = []
    for p in parts:
        t = tr_word(p)
        if t is None:
            return None
        trans.append(t)
    if parts[0] in ("Is", "Has", "Can", "Supports", "Enable", "Enabled", "Allow"):
        return "是否" + "".join(trans[1:])
    return "".join(trans)



def tr_word(w):
    w = w.strip()
    low = w.lower()
    if low in WORD:
        return WORD[low]
    if low.endswith("s") and low[:-1] in WORD:
        return WORD[low[:-1]]
    if low.endswith("es") and low[:-2] in WORD:
        return WORD[low[:-2]]
    if w.isupper() and len(w) <= 6:
        return w
    return None


def tr_phrase(phrase):
    """把英文名词短语按词表拼成中文，词序保持。"""
    phrase = re.sub(r"\s+", " ", phrase.strip())
    # A of B -> B 的 A
    m = re.match(r"^(.*?)\s+of\s+(?:the\s+)?(.*)$", phrase, re.I)
    if m:
        a, b = m.group(1), m.group(2)
        tb = tr_phrase(b)
        ta = tr_phrase(a)
        if tb and ta:
            return "%s的%s" % (tb, ta)
    parts = []
    unknown = []
    for w in phrase.split(" "):
        if w.lower() in ("the", "a", "an"):
            continue
        if w.lower() == "in":
            parts.append("（单位：")
            continue
        t = tr_word(w)
        if t is None:
            unknown.append(w)
            parts.append(w)
        else:
            parts.append(t)
    out = "".join(parts).replace("（单位：", "")
    if parts and parts[-1].startswith("（单位："):
        out += "）"
    if unknown:
        return None
    return out


def tr_field(note, pname=""):
    n = (note or "").strip()
    if pname in FIELDS and (not n or (n.startswith("The ") and len(n) <= 46)):
        return FIELDS[pname]
    if not n:
        g = gloss_from_name(pname)
        return g if g else "—"
    if n in NOTE:
        return NOTE[n]
    if n in SENTENCE:
        return SENTENCE[n]
    if n.endswith(":") and re.match(r"^[\w`\.]+:$", n):
        return "请求体：%s 对象。" % n[:-1]
    if re.match(r"^Class\s+", n):
        return "类：%s。" % n[6:].strip()
    if re.match(r"^Enum\s+", n):
        return "枚举：%s。" % n[5:].strip()
    if re.match(r"^Interface\s+", n):
        return "接口：%s。" % n[10:].strip()
    if n.startswith("Deprecated"):
        return "已弃用。" + n
    if n.startswith("Optional filter"):
        return "可选。筛选条件，见参数说明。"

    # 去掉 ffprobe 技术注记，保留关键字段名
    probe = ""
    m = re.search(r"Probe Field:\s*([^\s,]+)", n)
    if m:
        probe = "（ffprobe 字段 `%s`）" % m.group(1).strip('.,')
        n = n[:m.start()].rstrip()
    n = re.sub(r"\s*Actual type:.*$", "", n)
    n = re.sub(r"\s*Related Enums?:.*$", "", n)
    n = re.sub(r"\s*Related Enum:.*$", "", n)
    n = re.sub(r"\s*Applies to:.*$", "", n)
    n = re.sub(r"\s+", " ", n).strip()

    if n.endswith(".") and n[0].isupper() and n.startswith("A value indicating whether"):
        body = n[len("A value indicating whether"):].strip().rstrip(".")
        body = re.sub(r"^this instance (is|has)\s+", "", body, flags=re.I)
        body = re.sub(r"^\[(.*)\]$", r"\1", body)
        t = tr_phrase(body)
        if t:
            return "指示是否%s。%s" % (t, probe)

    if n.startswith("The ") and n.endswith("."):
        body = n[4:].rstrip(".")
        t = tr_phrase(body)
        if t:
            return "%s。%s" % (t, probe)
    if n.endswith("."):
        t = tr_phrase(n.rstrip("."))
        if t:
            return "%s。%s" % (t, probe)
    return "（原文）" + n
