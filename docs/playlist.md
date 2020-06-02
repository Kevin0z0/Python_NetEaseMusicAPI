## 歌单详情
说明: 1000首以下有歌曲详情,1000首以上须调用[/api/song/detail](song#歌曲详情)

必选参数:

```id```: 歌单id

可选参数:

```s```: 最近的收藏者数量,默认为10

**接口地址:**```/api/playlist/detail```

**调用例子:**```/api/playlist/detail?id=309562578```


## 每日推荐
说明: (需登录)

无参数

**接口地址:**```/api/playlist/recommend```

## 推荐歌单

可选参数:

```limit```: 返回数量, 默认为30

**接口地址:**```/api/playlist/personalized```

## 包含这首歌的歌单
说明: 只返回三个

必选参数:

```id```: 歌单id

**接口地址:**```/api/playlist/simi```

**调用例子:**```/api/playlist/simi?id=1425643256```


## 相关推荐

必选参数:

```id```: 歌单id

**接口地址:**```/api/playlist/related```

**调用例子:**```/api/playlist/related?id=2979314208```

## 收藏/取消收藏歌单

必选参数:

```t```: 0 / 1 0取消收藏，1收藏

```id```: 歌单id

**接口地址:**```/api/playlist/subscribe```

**调用例子:**```/api/playlist/subscribe?id=2014444849&t=1```

## 歌单收藏者

必选参数:

```id```: 歌单id

可选参数:

```limit```: 返回数量, 默认为20

```offset```: 偏移数量，用于分页, 如:```(页数 - 1) * 20```, 其中```20```为```limit```的值, 默认为0

**接口地址:**```/api/playlist/subscribers```

**调用例子:**```/api/playlist/subscribers?id=2014444849&limit=10```


## 对歌单添加或删除歌曲
说明: (需登录)

必选参数:

```op```: add / del  add为添加，del为删除

```pid```: 歌单id

```songs```: 歌曲id，用逗号分开

**接口地址:**```/api/playlist/tracks```

**调用例子:**

```/api/playlist/tracks?op=add&pid=2978140310&songs=1308032189```,

```/api/playlist/tracks?op=del&pid=2978140310&songs=1308032189,36496726```


## 创建歌单
说明: (需登录)

必选参数:

```name```: 歌单名称

可选参数:

```type```: 0（默认）0 普通  10 隐私歌单

**接口地址:**```/api/playlist/create```

**调用例子:**```/api/playlist/create?name=新建歌单&type=10```

## 删除歌单
说明: (需登录)

必选参数:

```id```: 歌单id

**接口地址:**```/api/playlist/delete```

**调用例子:**```/api/playlist/delete?id=4897384823```


## 歌单分类

无参数

**接口地址:**```/api/playlist/catlist```


## 热门歌单分类

无参数

**接口地址:**```/api/playlist/hot```

## 歌单 ( 网友精选碟 )

可选参数:

```tag```: 全部 (默认) / 华语 ... 可从[/api/playlist/catlist](#歌单分类)中获取

```type```: hot (默认) / new hot:最火  new:最新

```limit```: 返回数量, 默认为50

```offset```: 偏移数量，用于分页, 如:```(页数 - 1) * 50```, 其中```50```为```limit```的值, 默认为0

**接口地址:**```/api/playlist/top```

**调用例子:**```/api/playlist/top?tag=华语&type=new```


## 获取精品歌单


可选参数:

```limit```: 返回数量, 默认为50

```before```: 取上一页歌单最后一项的updatetime

**接口地址:**```/api/playlist/tophigh```

**调用例子:**```/api/playlist/tophigh?before=1582697469638```


## 更新

说明: 以下操作都需登录

### 更新歌单

必选参数:

```id```: 歌单id

```name```: 歌单名字

可选参数:

```desc```: 歌单简介

```tags```: 歌单标签，多个标签用逗号隔开

**接口地址:**```/api/playlist/update```

**调用例子:**```/api/playlist/update?id=2978140310&name=古风&desc=666&tags=古风,华语```


### 更新歌单简介

必选参数:

```id```: 歌单id

```desc```: 歌单简介

**接口地址:**```/api/playlist/update/desc```

**调用例子:**```/api/playlist/update/desc?id=2978140310&desc=123123123```

### 更新歌单名

必选参数:

```id```: 歌单id

```name```: 歌单名

**接口地址:**```/api/playlist/update/name```

**调用例子:**```/api/playlist/update/desc?id=2978140310&name=古风```

### 更新歌单标签

```id```: 歌单id

```tags```: 歌单标签，多个用逗号隔开

**接口地址:**```/api/playlist/update/name```

**调用例子:**```/api/playlist/update/desc?id=2978140310&tags=古风,华语```