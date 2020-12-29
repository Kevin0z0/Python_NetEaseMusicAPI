## 文档

[https://kevin0z0.github.io/Python_NetEaseMusicAPI/#/](https://kevin0z0.github.io/Python_NetEaseMusicAPI/#/)

## 关于

本项目基于[Binaryify](https://github.com/Binaryify/NeteaseCloudMusicApi)的Nodejs版本略微修改

刚开始学Django，可能有很多地方配置的不是很到位，还请大佬指点

由于不清楚django有什么潜在的漏洞，此项目没有过滤任何字符串也没有添加waf，如果部署在自己的云服务器上的，建议不要使用root权限，要是使用的人多考虑搭个docker


参考项目:

[https://github.com/Binaryify/NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)

[https://github.com/darknessomi/musicbox](https://github.com/darknessomi/musicbox)

## 新增

### 支持直接用js引用api

例: 
请求var```<script src="/api/search?value=李荣浩&var=search"></script>```

则返回变量
```javascript
search={"result":{"songs":[{"id":1407551413,"name":"麻雀","artists":[{"id":4292,"name":"李荣浩","picUrl":null,"alias":[],"albumSize":0,...}
```
若请求cb```<script src="/api/search?value=李荣浩&cb=search"></script>```

则直接执行名为search的函数（类似百度的搜索提示功能）
```javascript
search({"result":{"songs":[{"id":1407551413,"name":"麻雀","artists":[{"id":4292,"name":"李荣浩",...})
```

### 支持简易的日志记录

对应的日志在```home/log```中

## 安装

本项目基于Django3.0，只支持3.6及以上的版本运行

``` bash
git clone https://github.com/Kevin0z0/Python_NetEaseMusicAPI.git
cd Python_NetEaseMusicAPI
pip install -r requirements.txt
```
## 运行

运行前请先确保已安装了python3.6、django3.0 及以上版本

如果是编译版的python，缺少sqlite3的，请看此处[https://stackoverflow.com/questions/1210664/no-module-named-sqlite3](https://stackoverflow.com/questions/1210664/no-module-named-sqlite3)

##### 如果在本地运行
```bash
python manage.py runserver 8000
```

##### 如果需要在外部访问
```bash
python manage.py runserver 0:8000
```

```8000```为端口号，有需要可自行修改

## 接口调用须知

> 请自觉遵守法律法规，本项目仅供学习参考，一切法律责任由用户自己承担，与本人无关

本项目支持GET、POST的```urlencoded```和```json```方式请求，请放心食用 (需要登录后操作的接口建议用POST)

POST的json方式请求数据时数字类的id可以整型和字符串型发送

接口返回的数据全都为json数据，如果有其他奇怪的数据返回，请尽快反馈

部分接口可能会有bug，还请大佬们能提个issue

第一次写文档，如果有什么不清楚的也可以看[Binaryify](https://binaryify.github.io/NeteaseCloudMusicApi)大佬的文档，两边除了接口不一致，功能基本一致

## 目录

**用户**

登录

发送验证码

验证验证码

注册（更改密码）

检测手机号码是否已注册

初始化昵称

手机号换绑

退出登录

登录状态

获取详情

用户歌单

已购专辑

刷新

签到

私人FM

FM垃圾桶

获取用户喜欢的音乐列表

获取用户信息, 歌单, 收藏, mv, dj 数量

获取用户播放记录

获取用户创建的电台

获取用户创建的电台的详细信息

获取用户关注列表

获取用户粉丝

动态

获取所有动态

获取用户动态

转发用户动态

删除用户动态

分享歌曲、歌单、mv、电台、电台节目到动态

关注 / 取消关注用户

云盘

云盘歌曲详情

删除云盘歌曲

设置

更新用户信息

资源点赞( MV,电台,视频)

**音乐**

歌曲链接

是否可用(未完成)

歌词

歌曲详情

每日推荐

推荐新音乐

相似歌曲

新歌速递

获取最近 5 个听了这首歌的用户

新碟上架

喜欢音乐

智能播放/心动模式

**歌单**

歌单详情

每日推荐

推荐歌单

包含这首歌的歌单

相关推荐

收藏/取消收藏歌单

歌单收藏者

对歌单添加或删除歌曲

创建歌单

删除歌单

歌单分类

热门歌单分类

歌单 ( 网友精选碟 )

获取精品歌单

更新

更新歌单

更新歌单简介

更新歌单名

更新歌单标签

**歌手**

歌手单曲

歌手专辑

最新专辑

获取专辑内容

专辑动态信息

收藏/取消收藏专辑

获取已收藏专辑列表

歌手详情

歌手MV

热门歌手

获取相似歌手

歌手分类列表

收藏/取消收藏歌手

收藏的歌手列表

歌手热门50首歌曲

歌手榜

**搜索**

默认搜索关键词

搜索建议

搜索多重匹配

热搜列表(简略)

热搜列表(详细)

**电台**

Banner

热门电台

类别热门电台

电台详情

付费精品

节目

节目详情

节目榜

节目24小时榜

24小时主播榜

主播新人榜

最热主播榜

新晋电台榜/热门电台榜

电台分类

精选电台

分类推荐

推荐类型

非热门类型
订阅

订阅列表

付费精选

今日优选

推荐电台

推荐节目

**MV**

全部MV

最新MV

网易出品MV

推荐MV

相似MV

MV排行

MV详情

MV链接

收藏/取消收藏 MV

收藏的 MV 列表

**视频**

获取视频url

获取视频详情

获取视频标签列表

获取视频标签下的视频

相关视频

收藏与取消收藏视频

**评论**

发送/删除/回复评论

歌曲评论

专辑评论

歌单评论

电台评论

视频评论

热门评论

动态评论

点赞/取消点赞评论

**消息**

私信

私信内容

发送私信（纯文本 / 带歌单）

评论通知

@我通知

通知

**其他**

获取热门话题

云村热评

Banner

独家放送

排行榜

所有榜单

所有榜单内容摘要
