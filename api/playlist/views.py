from django.shortcuts import render
from .__init__ import request_query, Http_Response, send, BASE_URL
from json import loads, dumps


def home(request):
    return Http_Response("", "这是歌单API", "")


def detail(request):
    # 歌单详情
    query = request_query(request, "id", ["s", {"s": 8}])
    print(query)
    query["n"] = 100000
    data = send({"url": BASE_URL + "api/v3/playlist/detail",
                 "params": query}, "linuxapi").POST("")
    return Http_Response(request, data.text)


def recommend(request):
    # 每日推荐
    data = send().POST("weapi/v1/discovery/recommend/resource")
    return Http_Response(request, data.text)


def personalized(request):
    # 推荐歌单
    query = request_query(request, ["limit", {"limit": 30}])
    query["total"] = True
    query["n"] = 1000
    data = send(query).POST("weapi/personalized/playlist")
    return Http_Response(request, data.text)


def simi(request):
    # 包含这首歌的歌单
    query = request_query(request, ["id", "songid"])
    data = send(query).POST("weapi/discovery/simiPlaylist")
    return Http_Response(request, data.text)


def related(request):
    # 相关推荐
    import re
    query = request_query(request, "id")
    doc = send().GET("playlist?id=" + query["id"], {"ua": "pc"}).text
    try:
        value = re.findall(
            r'<div class="cver u-cover u-cover-3">.*?title="(.*?)".*?data-res-id="(.*?)".*?<img src="(.*?)\?param=50y50".*?<a class="nm nm f-thide s-fc3" href="/user/home\?id=(.*?)" title="(.*?)".*?</div>', doc, re.S | re.M)
        data = {"code": 200, "playlists": []}
        for i in value:
            temp = {
                "name": i[0],
                "id": i[1],
                "coverImgUrl": i[2],
                "creator": {"userId": i[3], "nickname": i[4]}
            }
            data["playlists"].append(temp)
    except:
        data = {"code": 400, "playlists": []}
    return Http_Response(request, dumps(data))


def subscribe(request):
    # 收藏/取消收藏歌单
    query = request_query(request, "t", "id")
    type = "unsubscribe" if query.pop("t") == "0" else "subscribe"
    data = send(query).POST("/weapi/playlist/"+type)
    return Http_Response(request, data.text)


def subscribers(request):
    # 歌单收藏者
    query = request_query(request, "id",
                          ["limit", {"limit": 20}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/playlist/subscribers")
    return Http_Response(request, data.text)


def tracks(request):
    # 对歌单添加或删除歌曲
    query = request_query(request, "op", "pid", ["songs", "trackIds"])
    query["trackIds"] = "[" + query["trackIds"] + "]"
    data = send(query).POST("weapi/playlist/manipulate/tracks")
    return Http_Response(request, data.text)


def create(request):
    # 创建歌单
    query = request_query(request, "name", ["type", {"privacy", 0}])
    data = send(query).POST("weapi/playlist/create", {"os": "pc"})
    return Http_Response(request, data.text)


def delete(request):
    # 删除歌单
    query = request_query(request, "pid")
    data = send(query).POST("weapi/playlist/delete")
    return Http_Response(request, data.text)


def catlist(request):
    # 歌单分类
    data = send().POST("weapi/playlist/catalogue")
    return Http_Response(request, data.text)


def hot(request):
    # 热门歌单分类
    data = send().POST("weapi/playlist/hottags")
    return Http_Response(request, data.text)


def top(request):
    # 歌单 ( 网友精选碟 )
    '''
    全部,华语,欧美,日语,韩语,粤语,小语种,流行,摇滚,民谣,电子,舞曲,说唱,轻音乐,爵士,乡村,R&B/Soul,古典,民族,英伦,金属,朋克,蓝调,雷鬼,世界音乐,拉丁,另类/独立,New Age,古风,后摇,Bossa Nova,清晨,夜晚,学习,工作,午休,下午茶,地铁,驾车,运动,旅行,散步,酒吧,怀旧,清新,浪漫,性感,伤感,治愈,放松,孤独,感动,兴奋,快乐,安静,思念,影视原声,ACG,儿童,校园,游戏,70后,80后,90后,网络歌曲,KTV,经典,翻唱,吉他,钢琴,器乐,榜单,00后
    '''
    query = request_query(request,
                          ["tag", {"cat": "全部"}],
                          ["type", {"type": "hot"}],
                          ["limit", {"limit": 50}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/playlist/list")
    return Http_Response(request, data.text)


def tophigh(request):
    # 获取精品歌单
    query = request_query(request,
                          ["tag", {"cat": "全部"}],
                          ["limit", {"limit": 50}],
                          ["before", {"lasttime": 0}])
    query["total"] = True
    data = send(query).POST("weapi/playlist/highquality/list")
    return Http_Response(request, data.text)


def update(request):
    # 更新歌单
    query = request_query(request, "id",
                          ["desc", {"desc": ""}],
                          ["tags", {"tags": ""}], "name")
    info = {
        '/api/playlist/desc/update': '{"id":' + query["id"] + ',"desc":"' + query["desc"] + '"}',
        '/api/playlist/tags/update': '{"id":' + query["id"] + ',"tags":"' + query["tags"].replace(",", ";") + '"}',
        '/api/playlist/update/name': '{"id":' + query["id"] + ',"name":"' + query["name"] + '"}',
    }
    data = send(info).POST("weapi/batch", {"os": "pc"})
    return Http_Response(request, data.text)


def update_desc(request):
    query = request_query(request, "id", "desc")
    data = send(query, url="/api/playlist/desc/update", encrypt_method="eapi").POST(
        "http://interface3.music.163.com/eapi/playlist/desc/update")
    return Http_Response(request, data.text)


def update_name(request):
    query = request_query(request, "id", "name")
    data = send(query, url="/api/playlist/update/name", encrypt_method="eapi").POST(
        "http://interface3.music.163.com/eapi/playlist/update/name")
    return Http_Response(request, data.text)


def update_tags(request):
    query = request_query(request, "id", "tags")
    query["tags"] = query["tags"].replace(",", ";")
    data = send(query, url="/api/playlist/tags/update", encrypt_method="eapi").POST(
        "http://interface3.music.163.com/eapi/playlist/tags/update")
    return Http_Response(request, data.text)
