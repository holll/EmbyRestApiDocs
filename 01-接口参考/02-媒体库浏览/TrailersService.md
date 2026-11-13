# TrailersService 预告片服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/TrailersService.html> ｜ 上级目录：[预告片服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

获取与某部电影/预告片相似的电影与预告片，用于“即将上映/相关推荐”。

- 接口数量：**1**
- 收录范围：当前官方文档快照中的 1 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `GET` | `/Trailers` | 查找与指定预告片相似的电影与预告片 | 用户 |

---

## 1. 查找与指定预告片相似的电影与预告片

`GET` `/Trailers`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ArtistType` | query | string | 未标注 | 艺术家类型：Artist（艺术家）或 AlbumArtist（专辑艺术家）。 |
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
| `AiredDuringSeason` | query | string | 未标注 | 获取某一季期间播出的全部集，含特别篇。 |
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
| `Recursive` | query | boolean | 未标注 | 在文件夹内搜索时是否递归查找子文件夹，true/false。 |
| `SearchTerm` | query | string | 未标注 | 搜索关键词。 |
| `SortOrder` | query | string | 未标注 | 排序方向：Ascending（升序）/ Descending（降序）。 |
| `ParentId` | query | string | 未标注 | 指定该项可把查询限定到某个条目或文件夹；省略则从媒体库根目录开始。 |
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
| `ProjectToMedia` | query | string | 未标注 | 把结果投影为媒体条目（仅返回媒体相关字段）。 |
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
| `UserId` | query | string | 未标注 | 用户 ID。 |
| `MinOfficialRating` | query | string | 否 | 可选。按最低分级过滤（如 PG、PG-13、TV-MA）。 |
| `IsLocked` | query | boolean | 否 | 可选。筛选已锁定的条目。 |
| `IsPlaceHolder` | query | boolean | 否 | 可选。筛选占位条目（无实际文件）。 |
| `HasOfficialRating` | query | boolean | 否 | 可选。筛选带分级信息的条目。 |
| `GroupItemsIntoCollections` | query | string | 未标注 | 是否把条目折叠进其所属合集（套装）后再返回。 |
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
