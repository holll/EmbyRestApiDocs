# LiveTvService 直播电视服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/LiveTvService.html> ｜ 上级目录：[直播电视服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

完整的直播电视管理：频道与频道映射、节目单（EPG）、录制与定时器、系列定时器、调谐器主机、节目单提供方。接口数量全项目最多，建议按“频道/节目单/录制/调谐器”四块阅读。

- 接口数量：**61**
- 收录范围：当前官方文档快照中的 61 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/LiveTv/ChannelMappingOptions` | 重置频道映射选项 | 管理员 |
| 2 | `DELETE` | `/LiveTv/ChannelMappings` | 重置频道映射 | 管理员 |
| 3 | `DELETE` | `/LiveTv/ListingProviders` | 删除节目单提供方 | 管理员 |
| 4 | `DELETE` | `/LiveTv/Recordings/{Id}` | 删除直播录制项 | 用户 |
| 5 | `DELETE` | `/LiveTv/SeriesTimers/{Id}` | 取消直播系列定时器 | 用户 |
| 6 | `DELETE` | `/LiveTv/Timers/{Id}` | 取消直播定时器 | 用户 |
| 7 | `DELETE` | `/LiveTv/TunerHosts` | 删除调谐器主机 | 管理员 |
| 8 | `GET` | `/LiveTv/AvailableRecordingOptions` | 获取可用录制选项 | 用户 |
| 9 | `GET` | `/LiveTv/ChannelMappingOptions` | 获取频道映射选项 | 管理员 |
| 10 | `GET` | `/LiveTv/ChannelMappings` | 获取频道映射 | 管理员 |
| 11 | `GET` | `/LiveTv/Channels` | 获取可用直播频道 | 用户 |
| 12 | `GET` | `/LiveTv/Channels/{Id}` | 获取直播电视频道 | 用户 |
| 13 | `GET` | `/LiveTv/ChannelTags` | 获取直播频道标签 | 用户 |
| 14 | `GET` | `/LiveTv/ChannelTags/Prefixes` | 获取直播频道标签前缀 | 用户 |
| 15 | `GET` | `/LiveTv/EPG` | 获取节目单（EPG） | 用户 |
| 16 | `GET` | `/LiveTv/Folder` | 获取直播电视根文件夹 | 用户 |
| 17 | `GET` | `/LiveTv/GuideInfo` | 获取节目单信息 | 用户 |
| 18 | `GET` | `/LiveTv/Info` | 获取可用直播服务 | 用户 |
| 19 | `GET` | `/LiveTv/ListingProviders` | 获取当前节目单提供方 | 管理员 |
| 20 | `GET` | `/LiveTv/ListingProviders/Available` | 获取节目单提供方 | 管理员 |
| 21 | `GET` | `/LiveTv/ListingProviders/Default` | 获取节目单提供方的默认配置 | 用户 |
| 22 | `GET` | `/LiveTv/ListingProviders/Lineups` | 获取可用频道列表（Lineup） | 管理员 |
| 23 | `GET` | `/LiveTv/Manage/Channels` | 获取频道管理列表 | 管理员 |
| 24 | `GET` | `/LiveTv/Programs` | 获取可用的直播节目单（EPG） | 用户 |
| 25 | `GET` | `/LiveTv/Programs/Recommended` | 获取可用的直播节目单（EPG） | 用户 |
| 26 | `GET` | `/LiveTv/Recordings` | 获取直播录制列表 | 用户 |
| 27 | `GET` | `/LiveTv/Recordings/{Id}` | 获取直播录制项详情 | 用户 |
| 28 | `GET` | `/LiveTv/Recordings/Folders` | 获取录制文件夹 | 用户 |
| 29 | `GET` | `/LiveTv/Recordings/Groups` | 获取直播录制分组 | 用户 |
| 30 | `GET` | `/LiveTv/Recordings/Series` | 获取直播录制列表 | 用户 |
| 31 | `GET` | `/LiveTv/SeriesTimers` | 获取直播系列定时器列表 | 用户 |
| 32 | `GET` | `/LiveTv/SeriesTimers/{Id}` | 获取直播系列定时器详情 | 用户 |
| 33 | `GET` | `/LiveTv/Timers` | 获取直播定时器列表 | 用户 |
| 34 | `GET` | `/LiveTv/Timers/{Id}` | 获取直播定时器详情 | 用户 |
| 35 | `GET` | `/LiveTv/Timers/Defaults` | 获取新建定时器的默认值 | 用户 |
| 36 | `GET` | `/LiveTv/TunerHosts` | 获取调谐器主机列表 | 管理员 |
| 37 | `GET` | `/LiveTv/TunerHosts/Default/{Type}` | 获取调谐器主机列表 | 管理员 |
| 38 | `GET` | `/LiveTv/TunerHosts/Types` | 获取调谐器主机类型 | 用户 |
| 39 | `GET` | `/LiveTv/Tuners/Discover` | 发现网络中的调谐器 | 用户 |
| 40 | `GET` | `/LiveTv/Tuners/Discvover` | 发现网络中的调谐器（拼写兼容写法） | 用户 |
| 41 | `HEAD` | `/LiveTv/ChannelMappingOptions` | 探测频道映射选项 | 管理员 |
| 42 | `HEAD` | `/LiveTv/ChannelMappings` | 探测频道映射 | 管理员 |
| 43 | `POST` | `/LiveTv/ChannelMappingOptions` | 设置频道映射选项 | 管理员 |
| 44 | `POST` | `/LiveTv/ChannelMappings` | 设置频道映射 | 管理员 |
| 45 | `POST` | `/LiveTv/ListingProviders` | 添加节目单提供方 | 管理员 |
| 46 | `POST` | `/LiveTv/ListingProviders/Delete` | 删除节目单提供方 | 管理员 |
| 47 | `POST` | `/LiveTv/Manage/Channels/{Id}/Disabled` | 设置频道是否禁用 | 管理员 |
| 48 | `POST` | `/LiveTv/Manage/Channels/{Id}/SortIndex` | 设置频道排序序号 | 管理员 |
| 49 | `POST` | `/LiveTv/Programs` | 获取可用的直播节目单（EPG） | 用户 |
| 50 | `POST` | `/LiveTv/Recordings/{Id}/Delete` | 删除直播录制项 | 用户 |
| 51 | `POST` | `/LiveTv/SeriesTimers` | 新建直播系列定时器 | 用户 |
| 52 | `POST` | `/LiveTv/SeriesTimers/{Id}` | 更新直播系列定时器 | 用户 |
| 53 | `POST` | `/LiveTv/SeriesTimers/{Id}/Delete` | 取消直播系列定时器 | 用户 |
| 54 | `POST` | `/LiveTv/Timers` | 新建直播定时器 | 用户 |
| 55 | `POST` | `/LiveTv/Timers/{Id}` | 更新直播定时器 | 用户 |
| 56 | `POST` | `/LiveTv/Timers/{Id}/Delete` | 取消直播定时器 | 用户 |
| 57 | `POST` | `/LiveTv/TunerHosts` | 添加调谐器主机 | 管理员 |
| 58 | `POST` | `/LiveTv/TunerHosts/Delete` | 删除调谐器主机 | 管理员 |
| 59 | `POST` | `/LiveTv/Tuners/{Id}/Reset` | 重置电视调谐器 | 管理员 |
| 60 | `PUT` | `/LiveTv/ChannelMappingOptions` | 更新频道映射选项 | 管理员 |
| 61 | `PUT` | `/LiveTv/ChannelMappings` | 更新频道映射 | 管理员 |

---

## 1. 重置频道映射选项

`DELETE` `/LiveTv/ChannelMappingOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 2. 重置频道映射

`DELETE` `/LiveTv/ChannelMappings`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 3. 删除节目单提供方

`DELETE` `/LiveTv/ListingProviders`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | query | string | 未标注 | 外部数据源 ID。 |

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

## 4. 删除直播录制项

`DELETE` `/LiveTv/Recordings/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 录制 ID。 |

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

## 5. 取消直播系列定时器

`DELETE` `/LiveTv/SeriesTimers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

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

## 6. 取消直播定时器

`DELETE` `/LiveTv/Timers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

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

## 7. 删除调谐器主机

`DELETE` `/LiveTv/TunerHosts`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | query | string | 未标注 | 调谐器主机 ID。 |

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

## 8. 获取可用录制选项

`GET` `/LiveTv/AvailableRecordingOptions`

- **权限**：用户令牌
- **成功响应**：`200` → `AvailableRecordingOptions`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AvailableRecordingOptions` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AvailableRecordingOptions`](../../02-数据模型/05-直播电视.md#availablerecordingoptions)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 9. 获取频道映射选项

`GET` `/LiveTv/ChannelMappingOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 10. 获取频道映射

`GET` `/LiveTv/ChannelMappings`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 11. 获取可用直播频道

`GET` `/LiveTv/Channels`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsLiked` | query | boolean | 未标注 | 按频道是否被喜欢过滤。 |
| `IsDisliked` | query | boolean | 未标注 | 按频道是否被不喜欢过滤。 |
| `EnableFavoriteSorting` | query | boolean | 未标注 | 把收藏与喜欢状态纳入频道排序。 |
| `AddCurrentProgram` | query | string | 否 | 可选。为每个频道附加当前正在播出的节目信息。 |
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

---

## 12. 获取直播电视频道

`GET` `/LiveTv/Channels/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 频道 ID。 |
| `UserId` | query | string | 否 | 可选。附带用户数据。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 13. 获取直播频道标签

`GET` `/LiveTv/ChannelTags`

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

---

## 14. 获取直播频道标签前缀

`GET` `/LiveTv/ChannelTags/Prefixes`

- **权限**：用户令牌
- **成功响应**：`200` → `Emby_LiveTV_Api_TagItem []`

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
| 200 | 成功，返回 `Emby_LiveTV_Api_TagItem []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`Emby_LiveTV_Api_TagItem`](../../02-数据模型/02-媒体条目.md#emby_livetv_api_tagitem)

---

## 15. 获取节目单（EPG）

`GET` `/LiveTv/EPG`

- **权限**：用户令牌
- **成功响应**：`200` → `EpgRow`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsLiked` | query | boolean | 未标注 | 按频道是否被喜欢过滤。 |
| `IsDisliked` | query | boolean | 未标注 | 按频道是否被不喜欢过滤。 |
| `EnableFavoriteSorting` | query | boolean | 未标注 | 把收藏与喜欢状态纳入频道排序。 |
| `AddCurrentProgram` | query | string | 否 | 可选。为每个频道附加当前正在播出的节目信息。 |
| `ChannelIds` | query | string | 未标注 | 需要返回节目单信息的频道。 |
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
| 200 | 成功，返回 `EpgRow` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`EpgRow`](../../02-数据模型/05-直播电视.md#epgrow)

> 该接口在官方文档中还引用了 29 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 16. 获取直播电视根文件夹

`GET` `/LiveTv/Folder`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 17. 获取节目单信息

`GET` `/LiveTv/GuideInfo`

- **权限**：用户令牌
- **成功响应**：`200` → `GuideInfo`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `GuideInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`GuideInfo`](../../02-数据模型/05-直播电视.md#guideinfo)

---

## 18. 获取可用直播服务

`GET` `/LiveTv/Info`

- **权限**：用户令牌
- **成功响应**：`200` → `LiveTvInfo`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `LiveTvInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`LiveTvInfo`](../../02-数据模型/05-直播电视.md#livetvinfo)

---

## 19. 获取当前节目单提供方

`GET` `/LiveTv/ListingProviders`

- **权限**：管理员令牌
- **成功响应**：`200` → `ListingsProviderInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ChannelId` | query | string | 是 | 频道 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ListingsProviderInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ListingsProviderInfo`](../../02-数据模型/05-直播电视.md#listingsproviderinfo)、[`NameValuePair`](../../02-数据模型/06-系统与配置.md#namevaluepair)

---

## 20. 获取节目单提供方

`GET` `/LiveTv/ListingProviders/Available`

- **权限**：管理员令牌
- **成功响应**：`200` → `ListingProviderTypeInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ListingProviderTypeInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ListingProviderTypeInfo`](../../02-数据模型/05-直播电视.md#listingprovidertypeinfo)

---

## 21. 获取节目单提供方的默认配置

`GET` `/LiveTv/ListingProviders/Default`

- **权限**：用户令牌
- **成功响应**：`200` → `ListingsProviderInfo`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ListingsProviderInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ListingsProviderInfo`](../../02-数据模型/05-直播电视.md#listingsproviderinfo)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 22. 获取可用频道列表（Lineup）

`GET` `/LiveTv/ListingProviders/Lineups`

- **权限**：管理员令牌
- **成功响应**：`200` → `NameIdPair []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | query | string | 未标注 | 外部数据源 ID。 |
| `Location` | query | string | 未标注 | 位置。 |
| `Country` | query | integer | 未标注 | 国家/地区。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `NameIdPair []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`NameIdPair`](../../02-数据模型/06-系统与配置.md#nameidpair)

---

## 23. 获取频道管理列表

`GET` `/LiveTv/Manage/Channels`

- **权限**：管理员令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `SortBy` | query | string | 否 | 可选。排序字段，英文逗号分隔。可选值：Name、StartDate。 |
| `SortOrder` | query | string | 未标注 | 排序方向：Ascending（升序）/ Descending（降序）。 |

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

## 24. 获取可用的直播节目单（EPG）

`GET` `/LiveTv/Programs`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ChannelIds` | query | string | 未标注 | 需要返回节目单信息的频道。 |
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
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 25. 获取可用的直播节目单（EPG）

`GET` `/LiveTv/Programs/Recommended`

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

---

## 26. 获取直播录制列表

`GET` `/LiveTv/Recordings`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ChannelId` | query | string | 否 | 可选。按频道 ID 过滤。 |
| `Status` | query | string | 否 | 可选。按录制状态过滤。 |
| `IsInProgress` | query | boolean | 否 | 可选。筛选正在录制 / 非正在录制的录制项。 |
| `SeriesTimerId` | query | string | 否 | 可选。按所属系列定时器过滤录制项。 |
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
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

---

## 27. 获取直播录制项详情

`GET` `/LiveTv/Recordings/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 录制 ID。 |
| `UserId` | query | string | 否 | 可选。附带用户数据。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `BaseItemDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemDto`](../../02-数据模型/02-媒体条目.md#baseitemdto)

> 该接口在官方文档中还引用了 27 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 28. 获取录制文件夹

`GET` `/LiveTv/Recordings/Folders`

- **权限**：用户令牌
- **成功响应**：`200` → `BaseItemDto []`

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

## 29. 获取直播录制分组

`GET` `/LiveTv/Recordings/Groups`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

该接口无请求参数。

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

## 30. 获取直播录制列表

`GET` `/LiveTv/Recordings/Series`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_BaseItemDto`

该接口无请求参数。

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

## 31. 获取直播系列定时器列表

`GET` `/LiveTv/SeriesTimers`

- **权限**：用户令牌
- **成功响应**：`200` → `SeriesTimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `SortBy` | query | string | 否 | 可选。按 SortName 或 Priority 排序。 |
| `SortOrder` | query | string | 否 | 可选。按升序或降序排序。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `SeriesTimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SeriesTimerInfoDto`](../../02-数据模型/05-直播电视.md#seriestimerinfodto)

> 该接口在官方文档中还引用了 6 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 32. 获取直播系列定时器详情

`GET` `/LiveTv/SeriesTimers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `TimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TimerInfoDto`](../../02-数据模型/05-直播电视.md#timerinfodto)

> 该接口在官方文档中还引用了 30 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 33. 获取直播定时器列表

`GET` `/LiveTv/Timers`

- **权限**：用户令牌
- **成功响应**：`200` → `TimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ChannelId` | query | string | 否 | 可选。按频道 ID 过滤。 |
| `SeriesTimerId` | query | string | 否 | 可选。按所属系列定时器过滤定时器。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TimerInfoDto`](../../02-数据模型/05-直播电视.md#timerinfodto)

> 该接口在官方文档中还引用了 31 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 34. 获取直播定时器详情

`GET` `/LiveTv/Timers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `TimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TimerInfoDto`](../../02-数据模型/05-直播电视.md#timerinfodto)

> 该接口在官方文档中还引用了 30 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 35. 获取新建定时器的默认值

`GET` `/LiveTv/Timers/Defaults`

- **权限**：用户令牌
- **成功响应**：`200` → `SeriesTimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProgramId` | query | string | 否 | 可选。按指定节目附加默认值。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `SeriesTimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SeriesTimerInfoDto`](../../02-数据模型/05-直播电视.md#seriestimerinfodto)

> 该接口在官方文档中还引用了 5 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 36. 获取调谐器主机列表

`GET` `/LiveTv/TunerHosts`

- **权限**：管理员令牌
- **成功响应**：`200` → `TunerHostInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TunerHostInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TunerHostInfo`](../../02-数据模型/05-直播电视.md#tunerhostinfo)

---

## 37. 获取调谐器主机列表

`GET` `/LiveTv/TunerHosts/Default/{Type}`

- **权限**：管理员令牌
- **成功响应**：`200` → `TunerHostInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Type` | path | string | 是 | 类型。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TunerHostInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TunerHostInfo`](../../02-数据模型/05-直播电视.md#tunerhostinfo)

---

## 38. 获取调谐器主机类型

`GET` `/LiveTv/TunerHosts/Types`

- **权限**：用户令牌
- **成功响应**：`200` → `NameIdPair []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `NameIdPair []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`NameIdPair`](../../02-数据模型/06-系统与配置.md#nameidpair)

---

## 39. 发现网络中的调谐器

`GET` `/LiveTv/Tuners/Discover`

- **权限**：用户令牌
- **成功响应**：`200` → `TunerHostInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TunerHostInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TunerHostInfo`](../../02-数据模型/05-直播电视.md#tunerhostinfo)

---

## 40. 发现网络中的调谐器（拼写兼容写法）

`GET` `/LiveTv/Tuners/Discvover`

- **权限**：用户令牌
- **成功响应**：`200` → `TunerHostInfo []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TunerHostInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TunerHostInfo`](../../02-数据模型/05-直播电视.md#tunerhostinfo)

---

## 41. 探测频道映射选项

`HEAD` `/LiveTv/ChannelMappingOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 42. 探测频道映射

`HEAD` `/LiveTv/ChannelMappings`

- **权限**：管理员令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 43. 设置频道映射选项

`POST` `/LiveTv/ChannelMappingOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 44. 设置频道映射

`POST` `/LiveTv/ChannelMappings`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |
| `body` | body | SetChannelMapping | 是 | 请求体：`SetChannelMapping` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SetChannelMapping`](../../02-数据模型/05-直播电视.md#setchannelmapping)

---

## 45. 添加节目单提供方

`POST` `/LiveTv/ListingProviders`

- **权限**：管理员令牌
- **成功响应**：`200` → `ListingsProviderInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | ListingsProviderInfo | 是 | 请求体：`ListingsProviderInfo` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ListingsProviderInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ListingsProviderInfo`](../../02-数据模型/05-直播电视.md#listingsproviderinfo)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 46. 删除节目单提供方

`POST` `/LiveTv/ListingProviders/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | query | string | 未标注 | 外部数据源 ID。 |

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

## 47. 设置频道是否禁用

`POST` `/LiveTv/Manage/Channels/{Id}/Disabled`

- **权限**：管理员令牌
- **成功响应**：`200` → `QueryResult_ChannelManagementInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `body` | body | SetChannelDisabled | 是 | 请求体：`SetChannelDisabled` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_ChannelManagementInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_ChannelManagementInfo`](../../02-数据模型/01-通用结构.md#queryresult_channelmanagementinfo)、[`SetChannelDisabled`](../../02-数据模型/05-直播电视.md#setchanneldisabled)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 48. 设置频道排序序号

`POST` `/LiveTv/Manage/Channels/{Id}/SortIndex`

- **权限**：管理员令牌
- **成功响应**：`200` → `QueryResult_ChannelManagementInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `body` | body | SetChannelSortIndex | 是 | 请求体：`SetChannelSortIndex` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_ChannelManagementInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_ChannelManagementInfo`](../../02-数据模型/01-通用结构.md#queryresult_channelmanagementinfo)、[`SetChannelSortIndex`](../../02-数据模型/05-直播电视.md#setchannelsortindex)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 49. 获取可用的直播节目单（EPG）

`POST` `/LiveTv/Programs`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ChannelIds` | query | string | 未标注 | 需要返回节目单信息的频道。 |
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
| `body` | body | BaseItemsRequest | 是 | 请求体：`BaseItemsRequest` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`BaseItemsRequest`](../../02-数据模型/02-媒体条目.md#baseitemsrequest)

> 该接口在官方文档中还引用了 4 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 50. 删除直播录制项

`POST` `/LiveTv/Recordings/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 录制 ID。 |

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

## 51. 新建直播系列定时器

`POST` `/LiveTv/SeriesTimers`

- **权限**：用户令牌
- **成功响应**：`200` → `SeriesTimerInfoDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | SeriesTimerInfo | 是 | 请求体：`SeriesTimerInfo` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `SeriesTimerInfoDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SeriesTimerInfoDto`](../../02-数据模型/05-直播电视.md#seriestimerinfodto)、[`SeriesTimerInfo`](../../02-数据模型/05-直播电视.md#seriestimerinfo)

> 该接口在官方文档中还引用了 6 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 52. 更新直播系列定时器

`POST` `/LiveTv/SeriesTimers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `body` | body | SeriesTimerInfo | 是 | 请求体：`SeriesTimerInfo` 对象。 |

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

[`SeriesTimerInfo`](../../02-数据模型/05-直播电视.md#seriestimerinfo)

> 该接口在官方文档中还引用了 6 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 53. 取消直播系列定时器

`POST` `/LiveTv/SeriesTimers/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

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

## 54. 新建直播定时器

`POST` `/LiveTv/Timers`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | TimerInfoDto | 是 | 请求体：`TimerInfoDto` 对象。 |

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

[`TimerInfoDto`](../../02-数据模型/05-直播电视.md#timerinfodto)

> 该接口在官方文档中还引用了 30 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 55. 更新直播定时器

`POST` `/LiveTv/Timers/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID |
| `body` | body | TimerInfoDto | 是 | 请求体：`TimerInfoDto` 对象。 |

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

[`TimerInfoDto`](../../02-数据模型/05-直播电视.md#timerinfodto)

> 该接口在官方文档中还引用了 30 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 56. 取消直播定时器

`POST` `/LiveTv/Timers/{Id}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 定时器 ID。 |

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

## 57. 添加调谐器主机

`POST` `/LiveTv/TunerHosts`

- **权限**：管理员令牌
- **成功响应**：`200` → `TunerHostInfo`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | TunerHostInfo | 是 | 请求体：`TunerHostInfo` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `TunerHostInfo` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`TunerHostInfo`](../../02-数据模型/05-直播电视.md#tunerhostinfo)

---

## 58. 删除调谐器主机

`POST` `/LiveTv/TunerHosts/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | query | string | 未标注 | 调谐器主机 ID。 |

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

## 59. 重置电视调谐器

`POST` `/LiveTv/Tuners/{Id}/Reset`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 调谐器 ID。 |

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

## 60. 更新频道映射选项

`PUT` `/LiveTv/ChannelMappingOptions`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |

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

## 61. 更新频道映射

`PUT` `/LiveTv/ChannelMappings`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容，动作类接口）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `ProviderId` | query | string | 是 | 外部数据源 ID。 |
| `body` | body | SetChannelMapping | 是 | 请求体：`SetChannelMapping` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`SetChannelMapping`](../../02-数据模型/05-直播电视.md#setchannelmapping)
