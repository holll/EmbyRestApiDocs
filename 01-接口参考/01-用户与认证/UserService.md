# UserService 用户服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/UserService.html> ｜ 上级目录：[用户服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

账号体系的核心：登录认证、用户增删改、权限策略（Policy）、密码与“忘记密码”、用户设置项、以及收藏/评分/播放状态等用户数据。第三方客户端首次接入几乎都要先走这里的认证接口。

- 接口数量：**25**
- 收录范围：当前官方文档快照中的 25 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Users/{Id}` | 删除用户 | 管理员 |
| 2 | `DELETE` | `/Users/{Id}/RecentlySearched` | 清空最近搜索记录 | 用户 |
| 3 | `DELETE` | `/Users/{Id}/TrackSelections/{TrackType}` | 清除用户已选的音轨/字幕轨 | 用户 |
| 4 | `GET` | `/Users/{Id}` | 按 ID 获取用户 | 用户 |
| 5 | `GET` | `/Users/{UserId}/TypedSettings/{Key}` | 获取指定类型的用户设置 | 用户 |
| 6 | `GET` | `/Users/CopyDataOptions` | 获取复制用户数据的选项 | 管理员 |
| 7 | `GET` | `/Users/ItemAccess` | 获取用户列表 | 用户 |
| 8 | `GET` | `/Users/Prefixes` | 获取用户列表 | 管理员 |
| 9 | `GET` | `/Users/Public` | 获取登录界面展示的公开用户 | 用户 |
| 10 | `GET` | `/Users/Query` | 获取用户列表 | 管理员 |
| 11 | `POST` | `/Users/AuthenticateByName` | 用户认证（登录） | 用户 |
| 12 | `POST` | `/Users/{Id}` | 更新用户 | 用户 |
| 13 | `POST` | `/Users/{Id}/Authenticate` | 用户认证（登录） | 用户 |
| 14 | `POST` | `/Users/{Id}/Configuration` | 更新用户配置 | 用户 |
| 15 | `POST` | `/Users/{Id}/Configuration/Partial` | 更新用户配置 | 用户 |
| 16 | `POST` | `/Users/{Id}/Delete` | 删除用户 | 管理员 |
| 17 | `POST` | `/Users/{Id}/Password` | 修改用户密码 | 用户 |
| 18 | `POST` | `/Users/{Id}/Policy` | 更新用户策略（权限） | 管理员 |
| 19 | `POST` | `/Users/{Id}/RecentlySearched/Delete` | 清空最近搜索记录 | 用户 |
| 20 | `POST` | `/Users/{Id}/TrackSelections/{TrackType}/Delete` | 清除用户已选的音轨/字幕轨 | 用户 |
| 21 | `POST` | `/Users/{UserId}/CopyData` | 在两个用户间复制数据 | 管理员 |
| 22 | `POST` | `/Users/{UserId}/TypedSettings/{Key}` | 更新指定类型的用户设置 | 用户 |
| 23 | `POST` | `/Users/ForgotPassword` | 发起本地用户忘记密码流程 | 用户 |
| 24 | `POST` | `/Users/ForgotPassword/Pin` | 校验忘记密码 PIN | 用户 |
| 25 | `POST` | `/Users/New` | 创建用户 | 管理员 |

---

## 1. 删除用户

`DELETE` `/Users/{Id}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |

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

## 2. 清空最近搜索记录

`DELETE` `/Users/{Id}/RecentlySearched`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |

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

## 3. 清除用户已选的音轨/字幕轨

`DELETE` `/Users/{Id}/TrackSelections/{TrackType}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `TrackType` | path | string | 是 | 轨道类型（Audio / Subtitle） |

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

## 4. 按 ID 获取用户

`GET` `/Users/{Id}`

- **权限**：用户令牌
- **成功响应**：`200` → `UserDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserDto`](../../02-数据模型/03-用户与账号.md#userdto)

> 该接口在官方文档中还引用了 9 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 5. 获取指定类型的用户设置

`GET` `/Users/{UserId}/TypedSettings/{Key}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Key` | path | string | 是 | 键。 |
| `UserId` | path | string | 是 | 用户 ID |

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

## 6. 获取复制用户数据的选项

`GET` `/Users/CopyDataOptions`

- **权限**：管理员令牌
- **成功响应**：`200` → `FullUserCopyDataOptions`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `FullUserCopyDataOptions` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`FullUserCopyDataOptions`](../../02-数据模型/03-用户与账号.md#fullusercopydataoptions)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 7. 获取用户列表

`GET` `/Users/ItemAccess`

- **权限**：用户令牌
- **成功响应**：`200` → `QueryResult_UserDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsHidden` | query | boolean | 否 | 可选。按 IsHidden=true/false 过滤。 |
| `IsDisabled` | query | boolean | 否 | 可选。按 IsDisabled=true/false 过滤。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `SortOrder` | query | string | 未标注 | 排序方向：Ascending（升序）/ Descending（降序）。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_UserDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_UserDto`](../../02-数据模型/01-通用结构.md#queryresult_userdto)

> 该接口在官方文档中还引用了 10 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 8. 获取用户列表

`GET` `/Users/Prefixes`

- **权限**：管理员令牌
- **成功响应**：`200` → `NameIdPair []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsHidden` | query | boolean | 否 | 可选。按 IsHidden=true/false 过滤。 |
| `IsDisabled` | query | boolean | 否 | 可选。按 IsDisabled=true/false 过滤。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `SortOrder` | query | string | 未标注 | 排序方向：Ascending（升序）/ Descending（降序）。 |

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

## 9. 获取登录界面展示的公开用户

`GET` `/Users/Public`

- **权限**：用户令牌
- **成功响应**：`200` → `UserDto []`

该接口无请求参数。

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserDto []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserDto`](../../02-数据模型/03-用户与账号.md#userdto)、[`UserLinkType`](../../02-数据模型/03-用户与账号.md#userlinktype)

> 该接口在官方文档中还引用了 8 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 10. 获取用户列表

`GET` `/Users/Query`

- **权限**：管理员令牌
- **成功响应**：`200` → `QueryResult_UserDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `IsHidden` | query | boolean | 否 | 可选。按 IsHidden=true/false 过滤。 |
| `IsDisabled` | query | boolean | 否 | 可选。按 IsDisabled=true/false 过滤。 |
| `StartIndex` | query | integer | 否 | 可选。开始返回的记录序号，序号更小的记录会被丢弃。 |
| `Limit` | query | integer | 否 | 可选。最多返回的记录条数。 |
| `NameStartsWithOrGreater` | query | string | 否 | 可选。筛选排序名大于等于给定字符串的条目。 |
| `SortOrder` | query | string | 未标注 | 排序方向：Ascending（升序）/ Descending（降序）。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `QueryResult_UserDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`QueryResult_UserDto`](../../02-数据模型/01-通用结构.md#queryresult_userdto)

> 该接口在官方文档中还引用了 10 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 11. 用户认证（登录）

`POST` `/Users/AuthenticateByName`

- **权限**：用户令牌
- **成功响应**：`200` → `AuthenticationResult`

> Authenticate a user by nane and password. A 200 status code indicates success, while anything in the 400 or 500 range indicates failure

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `X-Emby-Authorization` | header | string | 是 | 认证头，名称可以是 Authorization 或 X-Emby-Authorization，格式为：Emby UserId="(guid)", Client="(string)", Device="(string)", DeviceId="(string)", Version="string", Token="(string)"。详见认证章节。 |
| `body` | body | AuthenticateUserByName | 是 | 请求体：`AuthenticateUserByName` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AuthenticationResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AuthenticationResult`](../../02-数据模型/03-用户与账号.md#authenticationresult)、[`AuthenticateUserByName`](../../02-数据模型/03-用户与账号.md#authenticateuserbyname)

> 该接口在官方文档中还引用了 51 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 12. 更新用户

`POST` `/Users/{Id}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | UserDto | 是 | 请求体：`UserDto` 对象。 |

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

[`UserDto`](../../02-数据模型/03-用户与账号.md#userdto)

> 该接口在官方文档中还引用了 9 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 13. 用户认证（登录）

`POST` `/Users/{Id}/Authenticate`

- **权限**：用户令牌
- **成功响应**：`200` → `AuthenticationResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | AuthenticateUser | 是 | 请求体：`AuthenticateUser` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `AuthenticationResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`AuthenticationResult`](../../02-数据模型/03-用户与账号.md#authenticationresult)、[`AuthenticateUser`](../../02-数据模型/03-用户与账号.md#authenticateuser)

> 该接口在官方文档中还引用了 51 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 14. 更新用户配置

`POST` `/Users/{Id}/Configuration`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | UserConfiguration | 是 | 请求体：`UserConfiguration` 对象。 |

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

[`UserConfiguration`](../../02-数据模型/03-用户与账号.md#userconfiguration)

> 该接口在官方文档中还引用了 2 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 15. 更新用户配置

`POST` `/Users/{Id}/Configuration/Partial`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | string (binary) | 是 | 二进制流，请求体直接传文件内容。 |

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

## 16. 删除用户

`POST` `/Users/{Id}/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |

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

## 17. 修改用户密码

`POST` `/Users/{Id}/Password`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | UpdateUserPassword | 是 | 请求体：`UpdateUserPassword` 对象。 |

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

[`UpdateUserPassword`](../../02-数据模型/03-用户与账号.md#updateuserpassword)

---

## 18. 更新用户策略（权限）

`POST` `/Users/{Id}/Policy`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `body` | body | UserPolicy | 是 | 请求体：`UserPolicy` 对象。 |

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

[`UserPolicy`](../../02-数据模型/03-用户与账号.md#userpolicy)

> 该接口在官方文档中还引用了 3 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 19. 清空最近搜索记录

`POST` `/Users/{Id}/RecentlySearched/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |

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

## 20. 清除用户已选的音轨/字幕轨

`POST` `/Users/{Id}/TrackSelections/{TrackType}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID |
| `TrackType` | path | string | 是 | 轨道类型（Audio / Subtitle） |

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

## 21. 在两个用户间复制数据

`POST` `/Users/{UserId}/CopyData`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID |
| `body` | body | CopyData | 是 | 请求体：`CopyData` 对象。 |

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

[`CopyData`](../../02-数据模型/06-系统与配置.md#copydata)

---

## 22. 更新指定类型的用户设置

`POST` `/Users/{UserId}/TypedSettings/{Key}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `UserId` | path | string | 是 | 用户 ID |
| `Key` | path | string | 是 | 键。 |
| `body` | body | string (binary) | 是 | 二进制流，请求体直接传文件内容。 |

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

## 23. 发起本地用户忘记密码流程

`POST` `/Users/ForgotPassword`

- **权限**：用户令牌
- **成功响应**：`200` → `ForgotPasswordResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | ForgotPassword | 是 | 请求体：`ForgotPassword` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ForgotPasswordResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ForgotPasswordResult`](../../02-数据模型/06-系统与配置.md#forgotpasswordresult)、[`ForgotPassword`](../../02-数据模型/06-系统与配置.md#forgotpassword)

> 该接口在官方文档中还引用了 1 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。

---

## 24. 校验忘记密码 PIN

`POST` `/Users/ForgotPassword/Pin`

- **权限**：用户令牌
- **成功响应**：`200` → `PinRedeemResult`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | ForgotPasswordPin | 是 | 请求体：`ForgotPasswordPin` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `PinRedeemResult` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`PinRedeemResult`](../../02-数据模型/06-系统与配置.md#pinredeemresult)、[`ForgotPasswordPin`](../../02-数据模型/06-系统与配置.md#forgotpasswordpin)

---

## 25. 创建用户

`POST` `/Users/New`

- **权限**：管理员令牌
- **成功响应**：`200` → `UserDto`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `body` | body | CreateUserByName | 是 | 请求体：`CreateUserByName` 对象。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `UserDto` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`UserDto`](../../02-数据模型/03-用户与账号.md#userdto)、[`CreateUserByName`](../../02-数据模型/03-用户与账号.md#createuserbyname)

> 该接口在官方文档中还引用了 9 个辅助模型，可在 [模型索引](../../02-数据模型/00-模型索引.md) 中按名称查找。
