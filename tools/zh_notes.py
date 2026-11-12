# -*- coding: utf-8 -*-
"""参数 / 模型字段说明的中文对照表。

键 = 官方文档中的原始说明文字（必须逐字一致），值 = 中文说明。
_gaps.py 会在构建时报告未命中的条目，便于补齐。
"""

NOTE_A = {
    # ── 查询过滤类参数 ──────────────────────────────────────────────
    "Optional. The record index to start at. All items with a lower index will be dropped from the results.":
        "可选。开始返回的记录序号，序号更小的记录会被丢弃。",
    "Optional. The maximum number of records to return":
        "可选。最多返回的记录条数。",
    "Optional. The minimum date. Format = ISO":
        "可选。最小日期，格式为 ISO 8601。",
    "Optional. The minimum premiere date. Format = ISO":
        "可选。首播日期下限，格式为 ISO 8601。",
    "Optional. The maximum premiere date. Format = ISO":
        "可选。首播日期上限，格式为 ISO 8601。",
    "Artist or AlbumArtist":
        "艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。",
    "Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).":
        "可选。按最高分级过滤（如 PG、PG-13、TV-MA）。",
    "Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).":
        "可选。按最低分级过滤（如 PG、PG-13、TV-MA）。",
    "Optional filter by items with theme songs.":
        "可选。筛选含主题曲的条目。",
    "Optional filter by items with theme videos.":
        "可选。筛选含主题视频的条目。",
    "Optional filter by items with subtitles.":
        "可选。筛选含字幕的条目。",
    "Optional filter by items with special features.":
        "可选。筛选含特别收录（花絮）的条目。",
    "Optional filter by items with trailers.":
        "可选。筛选含预告片的条目。",
    "Optional. Filter by special season.":
        "可选。筛选特别季。",
    "Optional. Return items that are siblings of a supplied item.":
        "可选。返回与指定条目同级的条目（同季/同专辑内）。",
    "Optional. Skip through the list until a given item is found.":
        "可选。跳过列表直到找到指定条目。",
    "Optional filter by minimum index number.":
        "可选。按最小集数（序号）过滤。",
    "Optional filter by maximum number of game players.":
        "可选。按最大玩家人数过滤。",
    "Optional filter by minimum number of game players.":
        "可选。按最小玩家人数过滤。",
    "Optional filter by parent index number.":
        "可选。按父级序号（季号）过滤。",
    "Optional filter by items that have or do not have a parental rating":
        "可选。筛选有/无家长分级的条目。",
    "Optional filter by items that are HD or not.":
        "可选。筛选高清（HD）或非高清条目。",
    "Optional filter by items that are unaired episodes or not.":
        "可选。筛选未播出集或非未播出集。",
    "Optional filter by minimum community rating.":
        "可选。按最低社区评分过滤。",
    "Optional filter by minimum critic rating.":
        "可选。按最低影评人评分过滤。",
    "Gets all episodes that aired during a season, including specials.":
        "获取某一季期间播出的全部集，含特别篇。",
    "Optional. The minimum premiere date. Format = ISO (MinStartDate)":
        "可选。首播日期下限，格式为 ISO 8601。",
    "Optional filter by items that have an overview or not.":
        "可选。筛选有/无简介的条目。",
    "Optional filter by items that have an imdb id or not.":
        "可选。筛选有/无 IMDb ID 的条目。",
    "Optional filter by items that have a tmdb id or not.":
        "可选。筛选有/无 TMDB ID 的条目。",
    "Optional filter by items that have a tvdb id or not.":
        "可选。筛选有/无 TVDB ID 的条目。",
    "Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted.":
        "可选。排除指定条目 ID，可用英文逗号分隔多个。",
    "When searching within folders, this determines whether or not the search will be recursive. true/false":
        "在文件夹内搜索时是否递归查找子文件夹，true/false。",
    "Enter a search term to perform a search request":
        "搜索关键词。",
    "Sort Order - Ascending,Descending":
        "排序方向：Ascending（升序）/ Descending（降序）。",
    "Specify this to localize the search to a specific item or folder. Omit to use the root":
        "指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。",
    "Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted.":
        "可选。按条目类型过滤结果，可用英文逗号分隔多个值。",
    "Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.":
        "可选。按包含的图片类型过滤，可用英文逗号分隔多个值。",
    "Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines":
        "可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。",
    "Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls":
        "可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines、TrailerUrls。",
    "Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, SortName, Studios, Taglines":
        "可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、SortName、Studios、Taglines。",
    "Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime":
        "可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。",
    "Optional. Specify one or more sort orders, comma delimeted. Options: Name, StartDate":
        "可选。排序字段，英文逗号分隔。可选值：Name、StartDate。",
    "Optional. If specified, result will be filtered to contain only items which match at least one of the specified IDs. Each provider ID must be in the form 'prov.id', e.g. 'imdb.tt123456'. This allows multiple, comma delimeted value pairs.":
        "可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。",
    "Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes":
        "可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。",
    "Optional filter by items that are marked as favorite, or not.":
        "可选。筛选已收藏 / 未收藏的条目。",
    "Optional filter for movies.":
        "可选。只筛选电影。",
    "Optional filter for series.":
        "可选。只筛选剧集。",
    "Optional filter for folders.":
        "可选。只筛选文件夹。",
    "Optional filter for news.":
        "可选。只筛选新闻。",
    "Optional filter for kids.":
        "可选。只筛选儿童内容。",
    "Optional filter for sports.":
        "可选。只筛选体育内容。",
    "Optional filter for IsNew.":
        "可选。按“新增”标记筛选。",
    "Optional filter for IsPremiere.":
        "可选。按“首播”标记筛选。",
    "Optional filter for IsNewOrPremiere.":
        "可选。按“新增或首播”标记筛选。",
    "Optional filter for IsRepeat.":
        "可选。按“重播”标记筛选。",
    "ProjectToMedia":
        "把结果投影为媒体条目（仅返回媒体相关字段）。",
    "Optional filter by MediaType. Allows multiple, comma delimited.":
        "可选。按媒体类型过滤，英文逗号分隔多个。",
    "Optional filter by items that are played, or not.":
        "可选。筛选已播放 / 未播放的条目。",
    "Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted.":
        "可选。按类型（genre）过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted.":
        "可选。按分級（OfficialRating）过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted.":
        "可选。按标签过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted.":
        "可选。按制作年份过滤，可用英文逗号分隔多个。",
    "Optional, include image information in output":
        "可选。输出中包含图片信息。",
    "Optional, include user data":
        "可选。输出中包含用户数据。",
    "Optional, the max number of images to return, per image type":
        "可选。每种图片类型最多返回的图片数量。",
    "Optional. The image types to include in the output.":
        "可选。输出中要包含的图片类型。",
    "Optional. If specified, results will be filtered to include only those containing the specified person.":
        "可选。只保留包含指定人物的结果。",
    "Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited":
        "可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。",
    "Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted.":
        "可选。按工作室过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specified, results will be filtered based on artist. This allows multiple, pipe delimeted.":
        "可选。按艺术家过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted.":
        "可选。按专辑过滤，可用英文竖线 | 分隔多个。",
    "Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited.":
        "可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。",
    "Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted.":
        "可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。",
    "Optional filter by Container. Allows multiple, comma delimeted.":
        "可选。按封装格式（Container）过滤，英文逗号分隔多个。",
    "Optional filter by AudioCodec. Allows multiple, comma delimeted.":
        "可选。按音频编码过滤，英文逗号分隔多个。",
    "Optional filter by AudioLayout. Allows multiple, comma delimeted.":
        "可选。按音频声道布局过滤，英文逗号分隔多个。",
    "Optional filter by VideoCodec. Allows multiple, comma delimeted.":
        "可选。按视频编码过滤，英文逗号分隔多个。",
    "Optional filter by ExtendedVideoType. Allows multiple, comma delimeted.":
        "可选。按扩展视频类型过滤，英文逗号分隔多个。",
    "Optional filter by SubtitleCodec. Allows multiple, comma delimeted.":
        "可选。按字幕编码过滤，英文逗号分隔多个。",
    "Optional filter by Path.":
        "可选。按文件路径过滤。",
    "Optional filter by items that are locked.":
        "可选。筛选已锁定的条目。",
    "Optional filter by items that are placeholders":
        "可选。筛选占位条目（无实际文件）。",
    "Optional filter by items that have official ratings":
        "可选。筛选带分级信息的条目。",
    "Whether or not to hide items behind their boxsets.":
        "是否把条目折叠进其所属合集（套装）后再返回。",
    "Optional filter by items that are 3D, or not.":
        "可选。筛选 3D 或非 3D 条目。",
    "Optional filter by Series Status. Allows multiple, comma delimeted.":
        "可选。按剧集状态过滤，英文逗号分隔多个。",
    "Optional filter by items whose name is sorted equally or greater than a given input string.":
        "可选。筛选排序名大于等于给定字符串的条目。",
    "Optional filter by items whose name is sorted equally than a given input string.":
        "可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。",
    "Optional filter by items whose name is equally or lesser than a given input string.":
        "可选。筛选排序名小于等于给定字符串的条目。",
    "Optional filter by season number.":
        "可选。按季号过滤。",
    "Optional. Filter by season id":
        "可选。按季 ID 过滤。",
    "Optional. Filter by series id":
        "可选。按剧集 ID 过滤。",
    "Optional. Filter by folders that are marked hidden, or not.":
        "可选。筛选标记为隐藏（或未隐藏）的文件夹。",
    "Optional filter by IsHidden=true or false":
        "可选。按 IsHidden=true/false 过滤。",
    "Optional filter by IsDisabled=true or false":
        "可选。按 IsDisabled=true/false 过滤。",
    "Optional filter by tasks that are hidden, or not.":
        "可选。筛选隐藏 / 非隐藏的任务。",
    "Optional filter by tasks that are enabled, or not.":
        "可选。筛选启用 / 禁用的任务。",
    "Optional. Filter by sessions that a given user is allowed to remote control.":
        "可选。筛选指定用户有权远程控制的会话。",
    "Optional. Filter by user id, and attach user data":
        "可选。按用户 ID 过滤，并在结果中附带该用户的用户数据。",
    "Optional. Filter by device id.":
        "可选。按设备 ID 过滤。",
    "Optional. Filter by session id.":
        "可选。按会话 ID 过滤。",
    "Optional filter by channel id.":
        "可选。按频道 ID 过滤。",
    "The channels to return guide information for.":
        "要返回节目单信息的频道 ID。",
    "Optional. Get counts from a specific user's library.":
        "可选。只统计指定用户媒体库中的数量。",
    "Optional. Get counts of favorite items":
        "可选。同时统计收藏条目的数量。",
    "Optional attach user data.":
        "可选。附带用户数据。",
    "Optional. Adds current program info to each channel":
        "可选。为每个频道附加当前正在播出的节目信息。",
    "Optional, to attach default values based on a program.":
        "可选。按指定节目附加默认值。",
    "Optional. The image provider to use":
        "可选。要使用的图片提供方。",
    "Optional. The dlna device profile id to utilize.":
        "可选。要使用的 DLNA 设备配置文件 ID。",
    "Optional. Supply the cache tag from the item object to receive strong caching headers.":
        "可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。",
    "Optional. Apply a background color for transparent images.":
        "可选。为透明图片填充背景色。",
    "Optional. Apply a foreground layer on top of the image.":
        "可选。在图片上叠加前景层。",
    "Optional quality setting, from 0-100. Defaults to 90 and should suffice in most cases.":
        "可选。图片质量 0–100，默认 90，多数场景足够。",
    "Optional.":
        "可选。",
    "Optional version. Defaults to latest version.":
        "可选。版本号，默认取最新版本。",
    "Optional update class (Dev, Beta, Release). Defaults to Release.":
        "可选。更新通道（Dev、Beta、Release），默认 Release。",
    "Optional package type filter (System/UserInstalled)":
        "可选。包类型过滤（System 系统内置 / UserInstalled 用户安装）。",
    "Optional. Filter by target system type. Allows multiple, comma delimited.":
        "可选。按目标系统类型过滤，英文逗号分隔多个。",
    "Optional. Filter by premium status":
        "可选。按是否为高级（Premium）功能过滤。",
    "Optional. Filter by package that contain adult content.":
        "可选。筛选是否包含成人内容的包。",
    "Optional. Sort by SortName or Priority":
        "可选。按 SortName 或 Priority 排序。",
    "Optional. Sort in Ascending or Descending order":
        "可选。按升序或降序排序。",
    "Optional filter by recording status.":
        "可选。按录制状态过滤。",
    "Optional filter by recordings that are in progress, or not.":
        "可选。筛选正在录制 / 非正在录制的录制项。",
    "Optional filter by recordings belonging to a series timer":
        "可选。按所属系列定时器过滤录制项。",
    "Optional filter by timers belonging to a series timer":
        "可选。按所属系列定时器过滤定时器。",
    "Optional. Specify a starting offset, in ticks. 1ms = 10000 ticks.":
        "可选。起始偏移，单位 tick，1 毫秒 = 10000 ticks。",
    "Optional. The current position, in ticks. 1ms = 10000 ticks.":
        "可选。当前位置，单位 tick，1 毫秒 = 10000 ticks。",
    "Optional. The position, in ticks, where playback stopped. 1ms = 10000 ticks.":
        "可选。播放停止时的位置，单位 tick，1 毫秒 = 10000 ticks。",
    "Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.":
        "可选。目标音频编码，如 mp3；省略时服务端按 URL 扩展名自动选择。可选值：aac、mp3、vorbis、wma。",
    "Optional. Specify a specific audio sample rate, e.g. 44100":
        "可选。指定音频采样率，如 44100。",
    "Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.":
        "可选。目标音频码率，如 128000；省略时使用编码器默认值。",
    "Optional. Specify a specific number of audio channels to encode to, e.g. 2":
        "可选。指定音频声道数，如 2。",
    "Optional. Specify a maximum number of audio channels to encode to, e.g. 2":
        "可选。指定最大音频声道数，如 2。",
    "Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false":
        "可选。为 true 时直接静态输出原文件、不做任何编码。URL 使用无扩展名或原文件扩展名。true/false。",
    "Whether or not to copy timestamps when transcoding with an offset. Defaults to false.":
        "带偏移转码时是否复制时间戳，默认 false。",
    "Optional. The fixed horizontal resolution of the encoded video.":
        "可选。编码视频的固定水平分辨率（宽）。",
    "Optional. The fixed vertical resolution of the encoded video.":
        "可选。编码视频的固定垂直分辨率（高）。",
    "Optional. The maximum horizontal resolution of the encoded video.":
        "可选。编码视频的最大水平分辨率（宽）。",
    "Optional. The maximum vertical resolution of the encoded video.":
        "可选。编码视频的最大垂直分辨率（高）。",
    "Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.":
        "可选。目标视频码率，如 500000；省略时使用编码器默认值。",
    "Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.":
        "可选。要使用的字幕流序号；省略则不输出字幕。",
    "Optional. Specify the subtitle delivery method.":
        "可选。字幕交付方式（如 Encode 烧录、Embed 内嵌、External 外挂）。",
    "Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h264, mpeg4, theora, vpx, wmv.":
        "可选。目标视频编码，如 h264；省略时服务端按 URL 扩展名自动选择。可选值：h264、mpeg4、theora、vpx、wmv。",
    "Optional. The index of the audio stream to use. If omitted the first audio stream will be used.":
        "可选。要使用的音频流序号；省略则用第一条音频流。",
    "Optional. The index of the video stream to use. If omitted the first video stream will be used.":
        "可选。要使用的视频流序号；省略则用第一条视频流。",
    "Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.":
        "请求参数与原片一致时是否允许自动直接流复制，默认 true。",
    "Determines whether or not parent items should be searched for theme media.":
        "是否在父级条目中继续查找主题媒体（主题曲/主题视频）。",
    "The device id of the client requesting. Used to stop encoding processes when needed.":
        "请求方客户端的设备 ID，用于在需要时终止转码进程。",
    "Whether the item should be hidden from reusme or not. true/false":
        "是否把该条目从“继续观看”中隐藏，true/false。",
    "Whether the user likes the item or not. true/false":
        "用户是否喜欢该条目，true/false。",
    "Whether or not to lock the new collection.":
        "是否锁定新建的合集。",
    "Optional - create the collection within a specific folder":
        "可选。在指定文件夹内创建合集。",
    "Item Ids to add to the collection":
        "要加入合集的条目 ID。",
    "Item Ids to add to the playlist":
        "要加入播放列表的条目 ID。",
    "Item id, comma delimited":
        "条目 ID，英文逗号分隔。",
    "Item id list. This allows multiple, comma delimited.":
        "条目 ID 列表，英文逗号分隔。",
    "The ids of the items to play, comma delimited":
        "要播放的条目 ID，英文逗号分隔。",
    "Whether or not to group items into a parent container.":
        "是否把条目归组到父容器中。",
    "Whether or not to replace all images":
        "是否替换全部图片。",
    "Indicates if the refresh should occur recursively.":
        "指示是否递归刷新。",
    "Specifies the metadata refresh mode":
        "指定元数据刷新模式。",
    "Specifies the image refresh mode":
        "指定图片刷新模式。",
    "Determines if metadata should be replaced. Only applicable if mode is FullRefresh":
        "是否替换元数据，仅在刷新模式为 FullRefresh 时有效。",
    "Determines if images should be replaced. Only applicable if mode is FullRefresh":
        "是否替换图片，仅在刷新模式为 FullRefresh 时有效。",
    "An optional filter to include or exclude files from the results. true/false":
        "可选。结果中是否包含文件，true/false。",
    "An optional filter to include or exclude folders from the results. true/false":
        "可选。结果中是否包含文件夹，true/false。",
    "Filter by channels that are liked, or not.":
        "按频道是否被喜欢过滤。",
    "Filter by channels that are disliked, or not.":
        "按频道是否被不喜欢过滤。",
    "Incorporate favorite and like status into channel sorting.":
        "把收藏与喜欢状态纳入频道排序。",
    "Filter by items that are folders, or not.":
        "按是否为文件夹过滤。",
    "Filter by items that are played, or not.":
        "按是否已播放过滤。",
    "Set to true to force normalization of orientation in the event the renderer does not support it.":
        "设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。",
    "Set to true to retain image animation (when supported).":
        "设为 true 时保留图片动画（若格式支持）。",
    "Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.":
        "是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。",
    "Enable or disable image enhancers such as cover art.":
        "是否启用封面图等图像增强。",
    "Determines the output foramt of the image - original,gif,jpg,png":
        "图片输出格式：original（原格式）、gif、jpg、png。",
    "The maximum image width to return.":
        "返回图片的最大宽度。",
    "The maximum image height to return.":
        "返回图片的最大高度。",
    "The fixed image width to return.":
        "返回图片的固定宽度。",
    "The fixed image height to return.":
        "返回图片的固定高度。",
    "Return sanitized log":
        "返回脱敏（去敏感信息）后的日志。",
    "Whether or not to include external views such as channels or live tv":
        "是否包含频道、直播电视等外部视图。",
    "The authorization header can be either named 'Authorization' or 'X-Emby-Authorization'. It must be of the following schema: Emby UserId=\"(guid)\", Client=\"(string)\", Device=\"(string)\", DeviceId=\"(string)\", Version=\"string\", Token=\"(string)\" Please consult the documentation for further details.":
        "认证头，名称可以是 Authorization 或 X-Emby-Authorization，格式为：Emby UserId=\"(guid)\", Client=\"(string)\", Device=\"(string)\", DeviceId=\"(string)\", Version=\"string\", Token=\"(string)\"。详见认证章节。",
}

NOTE_B = {
    # ── 模型字段说明 ────────────────────────────────────────────────
    "Item Id": "条目 ID。",
    "Item id": "条目 ID。",
    "User Id": "用户 ID。",
    "UserId Id": "用户 ID。",
    "UserId": "用户 ID。",
    "Image Type": "图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。",
    "Image Index": "图片序号，同类型图片从 0 开始编号。",
    "Binary stream": "二进制流，请求体直接传文件内容。",
    "Container": "封装格式（如 mkv、mp4、ts）。",
    "Format": "格式。",
    "Key": "键。",
    "Name": "名称。",
    "Type": "类型。",
    "Size": "大小。",
    "Language": "语言。",
    "Location": "位置。",
    "Country": "国家/地区。",
    "Category": "分类。",
    "Album": "专辑。",
    "Client": "客户端名称。",
    "App": "应用名称。",
    "ParentId": "父级 ID。",
    "ItemIds": "条目 ID 列表。",
    "Ids": "ID 列表。",
    "Id": "标识。",
    "MediaSourceId": "媒体源 ID。",
    "LiveStreamId": "直播流 ID。",
    "PlaySessionId": "播放会话 ID。",
    "Session Id": "会话 ID。",
    "Device Id": "设备 ID。",
    "Plugin Id": "插件 ID。",
    "Profile Id": "配置文件 ID。",
    "Timer Id": "定时器 ID。",
    "Tuner Id": "调谐器 ID。",
    "Tuner host id": "调谐器主机 ID。",
    "Recording Id": "录制 ID。",
    "TargetId": "目标 ID。",
    "SubtitleId": "字幕 ID。",
    "StartPositionTicks": "起始位置，单位 tick（1 毫秒 = 10000 ticks）。",
    "EndPositionTicks": "结束位置，单位 tick（1 毫秒 = 10000 ticks）。",
    "CopyTimestamps": "是否复制时间戳。",
    "Server UuId": "服务器 UUID。",
    "Provider id": "外部数据源 ID。",
    "Provider Id": "外部数据源 ID。",
    "Auth Key": "认证密钥。",
    "Installation Id": "安装 ID。",
    "ConnectUserId": "Connect 用户 ID。",
    "Connect username": "Connect 用户名。",
    "DisplayPreferences Id": "显示偏好 ID。",
    "Codec Id": "编码 ID。",
    "Parameter Context": "参数上下文。",
    "NewIndex": "新序号。",
    "MediaSourceId ": "媒体源 ID。",
    "Movie Id": "电影 ID。",
    "Channel Id": "频道 ID。",
    "Channel id": "频道 ID。",
    "The id of the MediaSource": "媒体源 ID。",
    "The id of the item": "条目 ID。",
    "The item id": "条目 ID。",
    "The item ids": "条目 ID 列表。",
    "The Id of the item.": "条目 ID。",
    "The name": "名称。",
    "The name.": "名称。",
    "The name of the item.": "条目名称。",
    "The item name": "条目名称。",
    "The genre name": "类型（genre）名称。",
    "The artist name": "艺术家名称。",
    "The studio name": "工作室名称。",
    "The person name": "人物名称。",
    "The person id": "人物 ID。",
    "The image url": "图片 URL。",
    "The url for the new image": "新图片的 URL。",
    "The new image index": "新图片的序号。",
    "The icon filename": "图标文件名。",
    "The subtitle stream index": "字幕流序号。",
    "The subtitle segment length": "字幕分段长度。",
    "The subtitle segment format": "字幕分段格式。",
    "The play session id": "播放会话 ID。",
    "The series id": "剧集（series）ID。",
    "The log file name.": "日志文件名。",
    "The command to send.": "要下发的命令。",
    "The message text.": "消息正文。",
    "The message header.": "消息标题。",
    "The message timeout. If omitted the user will have to confirm viewing the message.":
        "消息超时时间；省略时用户必须手动确认才能关闭消息。",
    "The starting position of the first item.": "第一个条目的起始位置。",
    "The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.":
        "播放命令类型（PlayNow 立即播放、PlayNext 下一首插播、PlayLast 末尾追加）。尚未实现后两者的客户端可一律用 PlayNow。",
    "The type of item to browse to.": "要浏览到的条目类型。",
    "The next media type that will play": "接下来要播放的媒体类型。",
    "The max number of categories to return": "最多返回的分类数。",
    "The max number of items to return per category": "每个分类下最多返回的条目数。",
    "A list of playable media types, comma delimited. Audio, Video, Book, Game, Photo.":
        "可播放媒体类型列表，英文逗号分隔：Audio、Video、Book、Game、Photo。",
    "A list of supported remote control commands, comma delimited":
        "支持的远程控制命令列表，英文逗号分隔。",
    "Determines whether media can be played remotely.": "是否支持远程播放控制。",
    "Determines whether sync is supported.": "是否支持同步（Sync）。",
    "Indicates if the client can seek": "指示客户端是否支持拖动进度。",
    "Indicates if the player is paused.": "指示播放器是否已暂停。",
    "Indicates if the player is muted.": "指示播放器是否已静音。",
    "Scale of 0-100": "取值范围 0–100。",
    "IsPerfectMatch": "是否为完全匹配。",
    "IsForced": "是否为强制字幕（forced）。",
    "IsHearingImpaired": "是否为听障字幕（SDH）。",
    "The date the item was played (if any). Format = yyyyMMddHHmmss":
        "条目最后播放时间（若有），格式 yyyyMMddHHmmss。",
    "The notification's name": "通知名称。",
    "The notification's description": "通知描述。",
    "The notification's image url": "通知图片 URL。",
    "The notification's info url": "通知详情 URL。",
    "The notification level": "通知级别（Normal、Warning、Error）。",
    "The guid of the associated assembly": "关联程序集的 GUID。",
    "Guid of the associated assembly": "关联程序集的 GUID。",
    "The name of the package": "包名称。",
    "Package name": "包名称。",
    "Package type filter (System/UserInstalled)": "包类型过滤（System / UserInstalled）。",
    "The playlist media type": "播放列表媒体类型。",
    "The channels to return guide information for.": "需要返回节目单信息的频道。",
}

# 说明为空的参数，按参数名补充
PNOTE_EMPTY = {
    "StreamFileName": "流文件名。",
    "SectionId": "首页分区 ID。",
    "SegmentContainer": "分片封装格式（如 ts、mp4）。",
    "SegmentId": "分片序号（通常为分片文件名中的数字）。",
    "PlaylistId": "播放列表 ID（HLS 会话内标识）。",
    "PercentPlayed": "已播放百分比，用于生成进度条图。",
    "UnPlayedCount": "未播放集数，用于生成角标。",
    "ProviderName": "提供方名称。",
    "Segment": "分片序号。",
    "EntryIds": "活动日志条目 ID 列表。",
    "TrackType": "轨道类型（Audio 音频 / Subtitle 字幕）。",
    "PlayMethod": "播放方式（DirectPlay 直连、DirectStream 直转封装、Transcode 转码）。",
    "RepeatMode": "循环模式（RepeatNone、RepeatAll、RepeatOne）。",
    "SubtitleOffset": "字幕时间偏移，单位 tick。",
    "PlaybackRate": "播放速率（如 1.0 表示正常速度）。",
    "SubtitleStreamIndex": "字幕流序号。",
    "SegmentContainer ": "分片封装格式。",
}

NOTE = {}
NOTE.update(NOTE_A)
NOTE.update(NOTE_B)

# 官方说明明显复用/笔误时，按参数名给出的更准确中文说明
PNOTE_OVERRIDE = {
    "MinDateLastSaved": "可选。条目最后保存时间的下限，格式为 ISO 8601。",
    "MinDateLastSavedForUser": "可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。",
    "MinEndDate": "可选。结束日期下限，格式为 ISO 8601。",
    "MaxEndDate": "可选。结束日期上限，格式为 ISO 8601。",
    "StartItemId": "可选。跳过列表直到找到指定条目。",
    "AiredDuringSeason": "获取某一季期间播出的全部集，含特别篇。",
}

# 收尾补充：官方少量残留英文说明
NOTE.update({
    "Locale identifier of the client": "客户端区域标识（如 zh-CN）。",
    "Optional filter tasks that are enabled, or not.": "可选。按是否启用筛选任务。",
    "Optional filter tasks that are hidden, or not.": "可选。按是否隐藏筛选任务。",
    "Item name": "条目名称（需 URL 编码）。",
    "Id of the page controller": "页面控制器 ID。",
    "The image type": "图片类型（Primary / Backdrop / Logo / Thumb 等）。",
})
