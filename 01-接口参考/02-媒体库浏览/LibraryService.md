# LibraryService 媒体库服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/LibraryService.html> ｜ 上级目录：[媒体库服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

面向“媒体库”本身：列出媒体库文件夹、统计各类条目数量、库内搜索、获取最新媒体、扫描进度、删除条目、以及物理路径查询。管理端与首页“最新添加”会用到。

- 接口数量：**31**
- 覆盖范围：官方参考站该服务下的全部 31 个端点

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Items` | 从媒体库与文件系统删除条目 | 用户 |
| 2 | `DELETE` | `/Items/{Id}` | 从媒体库与文件系统删除条目 | 用户 |
| 3 | `GET` | `/Albums/{Id}/Similar` | 查找与指定专辑相似的专辑 | 用户 |
| 4 | `GET` | `/Artists/{Id}/Similar` | 查找相似艺术家 | 用户 |
| 5 | `GET` | `/Games/{Id}/Similar` | 查找与指定游戏相似的游戏 | 用户 |
| 6 | `GET` | `/Items/{Id}/Ancestors` | 获取条目的所有父级 | 用户 |
| 7 | `GET` | `/Items/{Id}/CriticReviews` | 获取条目的影评 | 用户 |
| 8 | `GET` | `/Items/{Id}/DeleteInfo` | 获取条目的删除信息 | 用户 |
| 9 | `GET` | `/Items/{Id}/Download` | 下载条目媒体文件 | 用户 |
| 10 | `GET` | `/Items/{Id}/File` | 获取条目的原始文件 | 用户 |
| 11 | `GET` | `/Items/{Id}/Similar` | 获取相似条目 | 用户 |
| 12 | `GET` | `/Items/{Id}/ThemeMedia` | 获取条目的主题视频与主题曲 | 用户 |
| 13 | `GET` | `/Items/{Id}/ThemeSongs` | 获取条目的主题曲 | 用户 |
| 14 | `GET` | `/Items/{Id}/ThemeVideos` | 获取条目的主题视频 | 用户 |
| 15 | `GET` | `/Items/Counts` | 统计各类条目数量 | 用户 |
| 16 | `GET` | `/Items/Intros` | 获取片头调试信息 | 管理员 |
| 17 | `GET` | `/Libraries/AvailableOptions` | 获取媒体库可选配置项 | 用户 |
| 18 | `GET` | `/Library/MediaFolders` | 获取全部用户媒体文件夹 | 用户 |
| 19 | `GET` | `/Library/PhysicalPaths` | 获取虚拟文件夹对应的物理路径 | 管理员 |
| 20 | `GET` | `/Library/SelectableMediaFolders` | 获取全部用户媒体文件夹 | 用户 |
| 21 | `GET` | `/Movies/{Id}/Similar` | 查找与指定电影相似的电影与预告片 | 用户 |
| 22 | `GET` | `/Shows/{Id}/Similar` | 查找与指定剧集相似的剧集 | 用户 |
| 23 | `GET` | `/Trailers/{Id}/Similar` | 查找与指定预告片相似的电影与预告片 | 用户 |
| 24 | `POST` | `/Items/{Id}/Delete` | 从媒体库与文件系统删除条目 | 用户 |
| 25 | `POST` | `/Items/Delete` | 从媒体库与文件系统删除条目 | 用户 |
| 26 | `POST` | `/Library/Media/Updated` | 上报外部来源新增了电影 | 用户 |
| 27 | `POST` | `/Library/Movies/Added` | 已弃用，请改用 /Library/Media/Updated | 用户 |
| 28 | `POST` | `/Library/Movies/Updated` | 已弃用，请改用 /Library/Media/Updated | 用户 |
| 29 | `POST` | `/Library/Refresh` | 启动媒体库扫描 | 管理员 |
| 30 | `POST` | `/Library/Series/Added` | 已弃用，请改用 /Library/Media/Updated | 用户 |
| 31 | `POST` | `/Library/Series/Updated` | 已弃用，请改用 /Library/Media/Updated | 用户 |

---

## 1. 从媒体库与文件系统删除条目

`DELETE` `/Items`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Ids` | query | string | 否 | ID 列表。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 2. 从媒体库与文件系统删除条目

`DELETE` `/Items/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 3. 查找与指定专辑相似的专辑

`GET` `/Albums/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 4. 查找相似艺术家

`GET` `/Artists/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 5. 查找与指定游戏相似的游戏

`GET` `/Games/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 6. 获取条目的所有父级

`GET` `/Items/{Id}/Ancestors`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | query | string | 否 | 可选。按用户 ID 过滤，并在结果中附带该用户的用户数据。 |
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)、[`SyncJobItemStatus`](../../02-数据模型/04-播放与转码.md#syncjobitemstatus)

> 该接口在官方文档中还引用了 26 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 7. 获取条目的影评

`GET` `/Items/{Id}/CriticReviews`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 8. 获取条目的删除信息

`GET` `/Items/{Id}/DeleteInfo`

- **权限**：用户令牌
- **成功响应**：`200` → `DeleteInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `DeleteInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`DeleteInfo`](../../02-数据模型/06-系统与配置.md#deleteinfo)

---

## 9. 下载条目媒体文件

`GET` `/Items/{Id}/Download`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

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

## 10. 获取条目的原始文件

`GET` `/Items/{Id}/File`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

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

## 11. 获取相似条目

`GET` `/Items/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 12. 获取条目的主题视频与主题曲

`GET` `/Items/{Id}/ThemeMedia`

- **权限**：用户令牌
- **成功响应**：`200` → `AllThemeMediaResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `InheritFromParent` | query | string | 否 | 是否在父级条目中继续查找主题媒体（主题曲/主题视频）。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AllThemeMediaResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AllThemeMediaResult`](../../02-数据模型/02-媒体条目.md#allthememediaresult)

> 该接口在官方文档中还引用了 29 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 13. 获取条目的主题曲

`GET` `/Items/{Id}/ThemeSongs`

- **权限**：用户令牌
- **成功响应**：`200` → `ThemeMediaResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `InheritFromParent` | query | string | 否 | 是否在父级条目中继续查找主题媒体（主题曲/主题视频）。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ThemeMediaResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ThemeMediaResult`](../../02-数据模型/02-媒体条目.md#thememediaresult)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 14. 获取条目的主题视频

`GET` `/Items/{Id}/ThemeVideos`

- **权限**：用户令牌
- **成功响应**：`200` → `ThemeMediaResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `InheritFromParent` | query | string | 否 | 是否在父级条目中继续查找主题媒体（主题曲/主题视频）。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ThemeMediaResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ThemeMediaResult`](../../02-数据模型/02-媒体条目.md#thememediaresult)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 15. 统计各类条目数量

`GET` `/Items/Counts`

- **权限**：用户令牌
- **成功响应**：`200` → `ItemCounts`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | query | string | 否 | 可选。只统计指定用户媒体库中的数量。 |
| `IsFavorite` | query | boolean | 否 | 可选。同时统计收藏条目的数量。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ItemCounts` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ItemCounts`](../../02-数据模型/02-媒体条目.md#itemcounts)

---

## 16. 获取片头调试信息

`GET` `/Items/Intros`

- **权限**：管理员令牌
- **成功响应**：`200` → `IntroDebugInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `IntroDebugInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`IntroDebugInfo`](../../02-数据模型/06-系统与配置.md#introdebuginfo)

---

## 17. 获取媒体库可选配置项

`GET` `/Libraries/AvailableOptions`

- **权限**：用户令牌
- **成功响应**：`200` → `LibraryOptionsResult`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `LibraryOptionsResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`LibraryOptionsResult`](../../02-数据模型/06-系统与配置.md#libraryoptionsresult)

> 该接口在官方文档中还引用了 8 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 18. 获取全部用户媒体文件夹

`GET` `/Library/MediaFolders`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsHidden` | query | boolean | 否 | 可选。筛选标记为隐藏（或未隐藏）的文件夹。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 19. 获取虚拟文件夹对应的物理路径

`GET` `/Library/PhysicalPaths`

- **权限**：管理员令牌
- **成功响应**：`200` → `array`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `array` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 20. 获取全部用户媒体文件夹

`GET` `/Library/SelectableMediaFolders`

- **权限**：用户令牌
- **成功响应**：`200` → `MediaFolder []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `MediaFolder []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`MediaFolder`](../../02-数据模型/02-媒体条目.md#mediafolder)、[`SubFolder`](../../02-数据模型/02-媒体条目.md#subfolder)

---

## 21. 查找与指定电影相似的电影与预告片

`GET` `/Movies/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 22. 查找与指定剧集相似的剧集

`GET` `/Shows/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 23. 查找与指定预告片相似的电影与预告片

`GET` `/Trailers/{Id}/Similar`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `ArtistType` | query | string | 否 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
| `MaxOfficialRating` | query | string | 否 | 可选。按最高分级过滤（如 PG、PG-13、TV-MA）。 |
| `HasThemeSong` | query | boolean | 否 | 可选。筛选含主题曲的条目。 |
| `HasThemeVideo` | query | boolean | 否 | 可选。筛选含主题视频的条目。 |
| `HasSubtitles` | query | boolean | 否 | 可选。筛选含字幕的条目。 |
| `HasSpecialFeature` | query | boolean | 否 | 可选。筛选含特别收录（花絮）的条目。 |
| `HasTrailer` | query | boolean | 否 | 可选。筛选含预告片的条目。 |
| `IsSpecialSeason` | query | boolean | 否 | 可选。筛选特别季。 |
| `AdjacentTo` | query | string | 否 | 可选。返回与指定条目同级的条目（同季/同专辑内）。 |
| `StartItemId` | query | string | 否 | 可选。跳过列表直到找到指定条目。 |
| `MinIndexNumber` | query | integer | 否 | 可选。按最小集数（序号）过滤。 |
| `MinStartDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MaxStartDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `MinEndDate` | query | string | 否 | 可选。结束日期下限，格式为 ISO 8601。 |
| `MaxEndDate` | query | string | 否 | 可选。结束日期上限，格式为 ISO 8601。 |
| `MinPlayers` | query | string | 否 | 可选。按最小玩家人数过滤。 |
| `MaxPlayers` | query | string | 否 | 可选。按最大玩家人数过滤。 |
| `ParentIndexNumber` | query | integer | 否 | 可选。按父级序号（季号）过滤。 |
| `HasParentalRating` | query | boolean | 否 | 可选。筛选有/无家长分级的条目。 |
| `IsHD` | query | boolean | 否 | 可选。筛选高清（HD）或非高清条目。 |
| `IsUnaired` | query | boolean | 否 | 可选。筛选未播出集或非未播出集。 |
| `MinCommunityRating` | query | string | 否 | 可选。按最低社区评分过滤。 |
| `MinCriticRating` | query | string | 否 | 可选。按最低影评人评分过滤。 |
| `AiredDuringSeason` | query | string | 否 | 获取某一季期间播出的全部集，含特别篇。 |
| `MinPremiereDate` | query | string | 否 | 可选。首播日期下限，格式为 ISO 8601。 |
| `MinDateLastSaved` | query | string | 否 | 可选。条目最后保存时间的下限，格式为 ISO 8601。 |
| `MinDateLastSavedForUser` | query | string | 否 | 可选。条目对指定用户可见的最后保存时间下限，格式为 ISO 8601。 |
| `MaxPremiereDate` | query | string | 否 | 可选。首播日期上限，格式为 ISO 8601。 |
| `HasOverview` | query | boolean | 否 | 可选。筛选有/无简介的条目。 |
| `HasImdbId` | query | boolean | 否 | 可选。筛选有/无 IMDb ID 的条目。 |
| `HasTmdbId` | query | boolean | 否 | 可选。筛选有/无 TMDB ID 的条目。 |
| `HasTvdbId` | query | boolean | 否 | 可选。筛选有/无 TVDB ID 的条目。 |
| `ExcludeItemIds` | query | string | 否 | 可选。排除指定条目 ID，可用英文逗号分隔多个。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `Recursive` | query | boolean | 否 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 否 | 搜索关键词。 |
| `SortOrder` | query | string | 否 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 否 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
| `Fields` | query | string | 否 | 可选。指定输出中额外返回的字段，英文逗号分隔。可选值：Budget、Chapters、DateCreated、Genres、HomePageUrl、IndexOptions、MediaStreams、Overview、ParentId、Path、People、ProviderIds、PrimaryImageAspectRatio、Revenue、SortName、Studios、Taglines。 |
| `ExcludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `IncludeItemTypes` | query | string | 否 | 可选。按条目类型过滤结果，可用英文逗号分隔多个值。 |
| `AnyProviderIdEquals` | query | string | 否 | 可选。只保留至少匹配一个给定外部 ID 的条目。每个 ID 形如 prov.id（例如 imdb.tt123456），多组用英文逗号分隔。 |
| `Filters` | query | string | 否 | 可选。附加过滤条件，英文逗号分隔。可选值：IsFolder、IsNotFolder、IsUnplayed、IsPlayed、IsFavorite、IsResumable、Likes、Dislikes。 |
| `IsFavorite` | query | boolean | 否 | 可选。筛选已收藏 / 未收藏的条目。 |
| `IsMovie` | query | boolean | 否 | 可选。只筛选电影。 |
| `IsSeries` | query | boolean | 否 | 可选。只筛选剧集。 |
| `IsFolder` | query | boolean | 否 | 可选。只筛选文件夹。 |
| `IsNews` | query | boolean | 否 | 可选。只筛选新闻。 |
| `IsKids` | query | boolean | 否 | 可选。只筛选儿童内容。 |
| `IsSports` | query | boolean | 否 | 可选。只筛选体育内容。 |
| `IsNew` | query | boolean | 否 | 可选。按“新增”标记筛选。 |
| `IsPremiere` | query | boolean | 否 | 可选。按“首播”标记筛选。 |
| `IsNewOrPremiere` | query | boolean | 否 | 可选。按“新增或首播”标记筛选。 |
| `IsRepeat` | query | boolean | 否 | 可选。按“重播”标记筛选。 |
| `ProjectToMedia` | query | string | 否 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
| `MediaTypes` | query | string | 否 | 可选。按媒体类型过滤，英文逗号分隔多个。 |
| `ImageTypes` | query | string | 否 | 可选。按包含的图片类型过滤，可用英文逗号分隔多个值。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔多个。可选值：Album、AlbumArtist、Artist、Budget、CommunityRating、CriticRating、DateCreated、DatePlayed、PlayCount、PremiereDate、ProductionYear、SortName、Random、Revenue、Runtime。 |
| `IsPlayed` | query | boolean | 否 | 可选。筛选已播放 / 未播放的条目。 |
| `Genres` | query | string | 否 | 可选。按类型（genre）过滤，可用英文竖线 \| 分隔多个。 |
| `OfficialRatings` | query | string | 否 | 可选。按分級（OfficialRating）过滤，可用英文竖线 \| 分隔多个。 |
| `Tags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `ExcludeTags` | query | string | 否 | 可选。按标签过滤，可用英文竖线 \| 分隔多个。 |
| `Years` | query | integer | 否 | 可选。按制作年份过滤，可用英文逗号分隔多个。 |
| `EnableImages` | query | boolean | 否 | 可选。输出中包含图片信息。 |
| `EnableUserData` | query | boolean | 否 | 可选。输出中包含用户数据。 |
| `ImageTypeLimit` | query | integer | 否 | 可选。每种图片类型最多返回的图片数量。 |
| `EnableImageTypes` | query | boolean | 否 | 可选。输出中要包含的图片类型。 |
| `Person` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonIds` | query | string | 否 | 可选。只保留包含指定人物的结果。 |
| `PersonTypes` | query | string | 否 | 可选。与 Person 同时使用时，只保留人物类型匹配的结果，英文逗号分隔多个。 |
| `Studios` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `StudioIds` | query | string | 否 | 可选。按工作室过滤，可用英文竖线 \| 分隔多个。 |
| `Artists` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `ArtistIds` | query | string | 否 | 可选。按艺术家过滤，可用英文竖线 \| 分隔多个。 |
| `Albums` | query | string | 否 | 可选。按专辑过滤，可用英文竖线 \| 分隔多个。 |
| `Ids` | query | string | 否 | 可选。需要精确获取指定条目时，传入条目 ID 列表，英文逗号分隔。 |
| `VideoTypes` | query | string | 否 | 可选。按视频类型过滤（videofile、dvd、bluray、iso），英文逗号分隔多个。 |
| `Containers` | query | string | 否 | 可选。按封装格式（Container）过滤，英文逗号分隔多个。 |
| `AudioCodecs` | query | string | 否 | 可选。按音频编码过滤，英文逗号分隔多个。 |
| `AudioLayouts` | query | string | 否 | 可选。按音频声道布局过滤，英文逗号分隔多个。 |
| `VideoCodecs` | query | string | 否 | 可选。按视频编码过滤，英文逗号分隔多个。 |
| `ExtendedVideoTypes` | query | string | 否 | 可选。按扩展视频类型过滤，英文逗号分隔多个。 |
| `SubtitleCodecs` | query | string | 否 | 可选。按字幕编码过滤，英文逗号分隔多个。 |
| `Path` | query | string | 否 | 可选。按文件路径过滤。 |
| `UserId` | query | string | 否 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 否 | 是否把条目折叠进其所属合集（套装）后再返回。 |
| `Is3D` | query | boolean | 否 | 可选。筛选 3D 或非 3D 条目。 |
| `SeriesStatus` | query | string | 否 | 可选。按剧集状态过滤，英文逗号分隔多个。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `ArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `AlbumArtistStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `NameStartsWith` | query | string | 否 | 可选。筛选排序名正好等于给定字符串的条目（用于字母索引定位）。 |
| `NameLessThan` | query | string | 否 | 可选。筛选排序名小于等于给定字符串的条目。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_BaseItemDto`](../../02-数据模型/01-通用结构.md#queryresult_baseitemdto)

> 该接口在官方文档中还引用了 28 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 24. 从媒体库与文件系统删除条目

`POST` `/Items/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 25. 从媒体库与文件系统删除条目

`POST` `/Items/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Ids` | query | string | 否 | ID 列表。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 26. 上报外部来源新增了电影

`POST` `/Library/Media/Updated`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | PostUpdatedMedia | — | 请求体：`PostUpdatedMedia` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`PostUpdatedMedia`](../../02-数据模型/02-媒体条目.md#postupdatedmedia)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 27. 已弃用，请改用 /Library/Media/Updated

`POST` `/Library/Movies/Added`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 28. 已弃用，请改用 /Library/Media/Updated

`POST` `/Library/Movies/Updated`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 29. 启动媒体库扫描

`POST` `/Library/Refresh`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 30. 已弃用，请改用 /Library/Media/Updated

`POST` `/Library/Series/Added`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 31. 已弃用，请改用 /Library/Media/Updated

`POST` `/Library/Series/Updated`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
