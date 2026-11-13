# ImageService 图片服务

> 官方文档：<https://dev.emby.media/reference/RestAPI/ImageService.html> ｜ 上级目录：[图片服务](README.md) ｜ [返回总目录](../../README.md)

## 概述

所有图片出口：条目主图/背景图/Logo/缩略图、人物与工作室图片、用户头像。支持指定尺寸、格式、质量、裁白、圆角、进度角标等参数，也支持上传/删除图片。图片 URL 是客户端列表页性能的关键。

- 接口数量：**49**
- 收录范围：当前官方文档快照中的 49 个端点；不代表已逐接口实机验证。

## 接口一览

| # | 方法 | 路径 | 说明 | 权限 |
|---:|---|---|---|---|
| 1 | `DELETE` | `/Items/{Id}/Images/{Type}` | 删除条目的图片 | 管理员 |
| 2 | `DELETE` | `/Items/{Id}/Images/{Type}/{Index}` | 删除条目指定序号的图片 | 管理员 |
| 3 | `DELETE` | `/Users/{Id}/Images/{Type}` | 删除用户头像 | 用户 |
| 4 | `DELETE` | `/Users/{Id}/Images/{Type}/{Index}` | 删除用户指定序号的图片 | 用户 |
| 5 | `GET` | `/Artists/{Name}/Images/{Type}` | 获取艺术家的图片 | 用户 |
| 6 | `GET` | `/Artists/{Name}/Images/{Type}/{Index}` | 获取艺术家指定序号的图片 | 用户 |
| 7 | `GET` | `/GameGenres/{Name}/Images/{Type}` | 获取游戏类型的图片 | 用户 |
| 8 | `GET` | `/GameGenres/{Name}/Images/{Type}/{Index}` | 获取游戏类型指定序号的图片 | 用户 |
| 9 | `GET` | `/Genres/{Name}/Images/{Type}` | 获取类型（genre）的图片 | 用户 |
| 10 | `GET` | `/Genres/{Name}/Images/{Type}/{Index}` | 获取类型指定序号的图片 | 用户 |
| 11 | `GET` | `/Items/{Id}/Images` | 获取条目图片信息 | 用户 |
| 12 | `GET` | `/Items/{Id}/Images/{Type}` | 获取条目的图片（主图） | 用户 |
| 13 | `GET` | `/Items/{Id}/Images/{Type}/{Index}` | 获取条目指定序号的图片 | 用户 |
| 14 | `GET` | `/Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnPlayedCount}` | 按尺寸/格式获取条目图片（含进度角标参数） | 用户 |
| 15 | `GET` | `/MusicGenres/{Name}/Images/{Type}` | 获取音乐类型的图片 | 用户 |
| 16 | `GET` | `/MusicGenres/{Name}/Images/{Type}/{Index}` | 获取音乐类型指定序号的图片 | 用户 |
| 17 | `GET` | `/Persons/{Name}/Images/{Type}` | 获取人物的图片 | 用户 |
| 18 | `GET` | `/Persons/{Name}/Images/{Type}/{Index}` | 获取人物指定序号的图片 | 用户 |
| 19 | `GET` | `/Studios/{Name}/Images/{Type}` | 获取工作室的图片 | 用户 |
| 20 | `GET` | `/Studios/{Name}/Images/{Type}/{Index}` | 获取工作室指定序号的图片 | 用户 |
| 21 | `GET` | `/Users/{Id}/Images/{Type}` | 获取用户头像 | 用户 |
| 22 | `GET` | `/Users/{Id}/Images/{Type}/{Index}` | 获取用户指定序号的图片 | 用户 |
| 23 | `HEAD` | `/Artists/{Name}/Images/{Type}` | 探测艺术家图片是否存在 | 用户 |
| 24 | `HEAD` | `/Artists/{Name}/Images/{Type}/{Index}` | 探测艺术家指定序号图片 | 用户 |
| 25 | `HEAD` | `/GameGenres/{Name}/Images/{Type}` | 探测游戏类型图片是否存在 | 用户 |
| 26 | `HEAD` | `/GameGenres/{Name}/Images/{Type}/{Index}` | 探测游戏类型指定序号图片 | 用户 |
| 27 | `HEAD` | `/Genres/{Name}/Images/{Type}` | 探测类型图片是否存在 | 用户 |
| 28 | `HEAD` | `/Genres/{Name}/Images/{Type}/{Index}` | 探测类型指定序号图片 | 用户 |
| 29 | `HEAD` | `/Items/{Id}/Images/{Type}` | 探测条目图片是否存在 | 用户 |
| 30 | `HEAD` | `/Items/{Id}/Images/{Type}/{Index}` | 探测条目指定序号图片 | 用户 |
| 31 | `HEAD` | `/Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnPlayedCount}` | 探测条目图片（含尺寸参数） | 用户 |
| 32 | `HEAD` | `/MusicGenres/{Name}/Images/{Type}` | 探测音乐类型图片是否存在 | 用户 |
| 33 | `HEAD` | `/MusicGenres/{Name}/Images/{Type}/{Index}` | 探测音乐类型指定序号图片 | 用户 |
| 34 | `HEAD` | `/Persons/{Name}/Images/{Type}` | 探测人物图片是否存在 | 用户 |
| 35 | `HEAD` | `/Persons/{Name}/Images/{Type}/{Index}` | 探测人物指定序号图片 | 用户 |
| 36 | `HEAD` | `/Studios/{Name}/Images/{Type}` | 探测工作室图片是否存在 | 用户 |
| 37 | `HEAD` | `/Studios/{Name}/Images/{Type}/{Index}` | 探测工作室指定序号图片 | 用户 |
| 38 | `HEAD` | `/Users/{Id}/Images/{Type}` | 探测用户头像是否存在 | 用户 |
| 39 | `HEAD` | `/Users/{Id}/Images/{Type}/{Index}` | 探测用户指定序号图片 | 用户 |
| 40 | `POST` | `/Items/{Id}/Images/{Type}` | 上传条目图片（需 Base64 编码） | 管理员 |
| 41 | `POST` | `/Items/{Id}/Images/{Type}/{Index}` | 上传条目图片（需 Base64 编码） | 管理员 |
| 42 | `POST` | `/Items/{Id}/Images/{Type}/{Index}/Delete` | 删除条目图片（POST 兼容写法） | 管理员 |
| 43 | `POST` | `/Items/{Id}/Images/{Type}/{Index}/Index` | 更新条目图片的序号 | 管理员 |
| 44 | `POST` | `/Items/{Id}/Images/{Type}/{Index}/Url` | 从远程 URL 添加条目图片 | 管理员 |
| 45 | `POST` | `/Items/{Id}/Images/{Type}/Delete` | 删除条目图片（POST 兼容写法） | 管理员 |
| 46 | `POST` | `/Users/{Id}/Images/{Type}` | 上传用户头像 | 用户 |
| 47 | `POST` | `/Users/{Id}/Images/{Type}/{Index}` | 上传用户图片 | 用户 |
| 48 | `POST` | `/Users/{Id}/Images/{Type}/{Index}/Delete` | 删除用户图片（POST 兼容写法） | 用户 |
| 49 | `POST` | `/Users/{Id}/Images/{Type}/Delete` | 删除用户图片（POST 兼容写法） | 用户 |

---

## 1. 删除条目的图片

`DELETE` `/Items/{Id}/Images/{Type}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 2. 删除条目指定序号的图片

`DELETE` `/Items/{Id}/Images/{Type}/{Index}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 3. 删除用户头像

`DELETE` `/Users/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 4. 删除用户指定序号的图片

`DELETE` `/Users/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 5. 获取艺术家的图片

`GET` `/Artists/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 6. 获取艺术家指定序号的图片

`GET` `/Artists/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 7. 获取游戏类型的图片

`GET` `/GameGenres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 8. 获取游戏类型指定序号的图片

`GET` `/GameGenres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 9. 获取类型（genre）的图片

`GET` `/Genres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 10. 获取类型指定序号的图片

`GET` `/Genres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 11. 获取条目图片信息

`GET` `/Items/{Id}/Images`

- **权限**：用户令牌
- **成功响应**：`200` → `ImageInfo []`

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，返回 `ImageInfo []` |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |

**涉及的数据模型**

[`ImageInfo`](../../02-数据模型/02-媒体条目.md#imageinfo)、[`ImageType`](../../02-数据模型/02-媒体条目.md#imagetype)

---

## 12. 获取条目的图片（主图）

`GET` `/Items/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 13. 获取条目指定序号的图片

`GET` `/Items/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 14. 按尺寸/格式获取条目图片（含进度角标参数）

`GET` `/Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnPlayedCount}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `PercentPlayed` | path | integer | 是 | 已播放百分比 |
| `UnPlayedCount` | path | integer | 是 | 未播放集数 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | path | integer | 是 | 返回图片的最大宽度。 |
| `MaxHeight` | path | integer | 是 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | path | string | 是 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | path | string | 是 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 15. 获取音乐类型的图片

`GET` `/MusicGenres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 16. 获取音乐类型指定序号的图片

`GET` `/MusicGenres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 17. 获取人物的图片

`GET` `/Persons/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 18. 获取人物指定序号的图片

`GET` `/Persons/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 19. 获取工作室的图片

`GET` `/Studios/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 20. 获取工作室指定序号的图片

`GET` `/Studios/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 21. 获取用户头像

`GET` `/Users/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 22. 获取用户指定序号的图片

`GET` `/Users/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 23. 探测艺术家图片是否存在

`HEAD` `/Artists/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 24. 探测艺术家指定序号图片

`HEAD` `/Artists/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 25. 探测游戏类型图片是否存在

`HEAD` `/GameGenres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 26. 探测游戏类型指定序号图片

`HEAD` `/GameGenres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 27. 探测类型图片是否存在

`HEAD` `/Genres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 28. 探测类型指定序号图片

`HEAD` `/Genres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 29. 探测条目图片是否存在

`HEAD` `/Items/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 30. 探测条目指定序号图片

`HEAD` `/Items/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 31. 探测条目图片（含尺寸参数）

`HEAD` `/Items/{Id}/Images/{Type}/{Index}/{Tag}/{Format}/{MaxWidth}/{MaxHeight}/{PercentPlayed}/{UnPlayedCount}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `PercentPlayed` | path | integer | 是 | 已播放百分比 |
| `UnPlayedCount` | path | integer | 是 | 未播放集数 |
| `Id` | path | string | 是 | 条目 ID。 |
| `MaxWidth` | path | integer | 是 | 返回图片的最大宽度。 |
| `MaxHeight` | path | integer | 是 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | path | string | 是 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | path | string | 是 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 32. 探测音乐类型图片是否存在

`HEAD` `/MusicGenres/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 33. 探测音乐类型指定序号图片

`HEAD` `/MusicGenres/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 34. 探测人物图片是否存在

`HEAD` `/Persons/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 35. 探测人物指定序号图片

`HEAD` `/Persons/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 36. 探测工作室图片是否存在

`HEAD` `/Studios/{Name}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 37. 探测工作室指定序号图片

`HEAD` `/Studios/{Name}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Name` | path | string | 是 | 条目名称（需 URL 编码）。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 38. 探测用户头像是否存在

`HEAD` `/Users/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 39. 探测用户指定序号图片

`HEAD` `/Users/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（二进制内容，如文件流、图片或字幕）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `MaxWidth` | query | integer | 未标注 | 返回图片的最大宽度。 |
| `MaxHeight` | query | integer | 未标注 | 返回图片的最大高度。 |
| `Width` | query | integer | 未标注 | 返回图片的固定宽度。 |
| `Height` | query | integer | 未标注 | 返回图片的固定高度。 |
| `Quality` | query | integer | 否 | 可选。图片质量 0–100，默认 90，多数场景足够。 |
| `Tag` | query | string | 否 | 可选。传入条目对象中的缓存标记（Tag），以便服务端返回强缓存响应头。 |
| `CropWhitespace` | query | string | 未标注 | 是否裁掉图片四周空白，True/False；不指定时，logo 与透明艺术图会自动裁白。 |
| `EnableImageEnhancers` | query | boolean | 未标注 | 是否启用封面图等图像增强。 |
| `Format` | query | string | 未标注 | 图片输出格式：original（原格式）、gif、jpg、png。 |
| `BackgroundColor` | query | string | 否 | 可选。为透明图片填充背景色。 |
| `ForegroundLayer` | query | string | 否 | 可选。在图片上叠加前景层。 |
| `AutoOrient` | query | boolean | 未标注 | 设为 true 时强制校正图片方向（用于不支持旋转信息的渲染端）。 |
| `KeepAnimation` | query | string | 未标注 | 设为 true 时保留图片动画（若格式支持）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 40. 上传条目图片（需 Base64 编码）

`POST` `/Items/{Id}/Images/{Type}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
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

## 41. 上传条目图片（需 Base64 编码）

`POST` `/Items/{Id}/Images/{Type}/{Index}`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
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

## 42. 删除条目图片（POST 兼容写法）

`POST` `/Items/{Id}/Images/{Type}/{Index}/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 43. 更新条目图片的序号

`POST` `/Items/{Id}/Images/{Type}/{Index}/Index`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `NewIndex` | query | integer | 是 | 新图片的序号。 |

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

## 44. 从远程 URL 添加条目图片

`POST` `/Items/{Id}/Images/{Type}/{Index}/Url`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Url` | query | string | 是 | 新图片的 URL。 |

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

## 45. 删除条目图片（POST 兼容写法）

`POST` `/Items/{Id}/Images/{Type}/Delete`

- **权限**：管理员令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 条目 ID。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 46. 上传用户头像

`POST` `/Users/{Id}/Images/{Type}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
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

## 47. 上传用户图片

`POST` `/Users/{Id}/Images/{Type}/{Index}`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |
| `body` | body | string (binary) | 是 | 二进制流，请求体直接传文件内容。 |
| `Index` | path | string | 是 | 序号，从 0 开始 |

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

## 48. 删除用户图片（POST 兼容写法）

`POST` `/Users/{Id}/Images/{Type}/{Index}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Index` | path | integer | 是 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

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

## 49. 删除用户图片（POST 兼容写法）

`POST` `/Users/{Id}/Images/{Type}/Delete`

- **权限**：用户令牌
- **成功响应**：`200`（无返回内容）

**请求参数**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| `Id` | path | string | 是 | 用户 ID。 |
| `Index` | query | integer | 未标注 | 图片序号，同类型图片从 0 开始编号。 |
| `Type` | path | string | 是 | 图片类型（Primary 主图、Backdrop 背景图、Logo、Thumb、Banner 等）。 |

**响应**

| 状态码 | 说明 |
|---|---|
| 200 | 成功，无返回内容 |
| 400 | 请求无法被服务器处理 |
| 401 | 未认证，或令牌已失效 |
| 403 | 已认证但无权限执行该操作 |
| 404 | 资源不存在或不可用 |
| 500 | 服务器内部错误 |
