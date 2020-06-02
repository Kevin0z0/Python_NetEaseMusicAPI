## 获取视频url

必选参数:

```id```: 视频id

可选参数:

```res```: 画质 (默认1080) 具体画质可从[/api/video/detail](#获取视频详情)中获取

**接口地址:**```/api/video/url```

**调用例子:**```/api/video/url?id=52A33E83CE2E28BF0A895B526CCA91EE&res=720```

## 获取视频详情

必选参数:

```id```: 视频id

**接口地址:**```/api/video/detail```

**调用例子:**```/api/video/detail?id=52A33E83CE2E28BF0A895B526CCA91EE```

## 获取视频标签列表

无参数

**接口地址:**```/api/video/lists```

## 获取视频标签下的视频

必选参数:

```id```: 从[/api/video/lists](#获取视频标签列表)中获取id

**接口地址:**```/api/video/group```

**调用例子:**```/api/video/group?id=243123```

## 相关视频

必选参数:

```id```: 视频id

**接口地址:**```/api/video/related```

**调用例子:**```/api/video/related?id=222DE075F86371A76E06B5209830C65B```

## 收藏与取消收藏视频
说明: 需登录

必选参数:

```id```: 视频id

可选参数:

```t```: 默认为1 (收藏)，0为取消收藏

**接口地址:**```/api/video/sub```

**调用例子:**```/api/video/sub?id=222DE075F86371A76E06B5209830C65B&t=0```取消收藏此视频
