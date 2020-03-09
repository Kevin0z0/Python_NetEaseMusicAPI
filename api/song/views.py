from django.shortcuts import render
from .__init__ import Http_Response, request_query, send, BASE_URL
from json import loads


def home(request):
    return Http_Response("", "这里是歌曲信息接口", "")


def url(request):
    # 歌曲URL
    query = request_query(request, ["id", "ids"], ["br", {"br": "999000"}])
    query["ids"] = "[" + query["ids"] + "]"
    # data = send({"url": BASE_URL + "api/song/enhance/player/url", "params": query}, "linuxapi").POST("")
    data = send(query).POST("weapi/song/enhance/player/url")
    return Http_Response(request, data.text)


def lyric(request):
    # 歌词
    query = request_query(request, "id")
    data = send({"url": BASE_URL + "api/song/lyric?lv=-1&kv=-1&tv=-1",
                 "params": query}, "linuxapi").POST("")
    return Http_Response(request, data.text)


def check(request):
    # 检查音乐是否可用
    init_data = {}
    query = request_query(request, ["id", "ids"], "br")
    query["ids"] = "[" + query["ids"] + "]"
    temp = query.copy()
    if "br" not in query or query["br"] == None:
        temp["br"] = "999000"
    data = loads(send(temp).POST("weapi/song/enhance/player/url").content)
    br = data["data"][0]["br"]
    if not query["br"]:
        init_data["maxbr"] = br
    else:
        if br < int(query["br"]):
            init_data["br"] = False
        else:
            init_data["br"] = True
    return Http_Response(request, str(init_data))


def detail(request):
    # 获取音乐详情
    query = request_query(request, ["id", "ids"])
    query["c"] = '[' + \
        ",".join(['{"id":' + i + '}' for i in query["ids"].split(",")]) + ']'
    query["ids"] = "[" + query["ids"] + "]"
    data = send(query).POST("weapi/v3/song/detail")
    return Http_Response(request, data.text)


def recommend(request):
    # 每日推荐
    data = send({"total": "true"}).POST("weapi/v1/discovery/recommend/songs")
    return Http_Response(request, data.text)


def newsong(request):
    # 推荐新音乐
    data = send({"type": "recommend"}).POST("weapi/personalized/newsong")
    return Http_Response(request, data.text)


def simi(request):
    # 相似歌曲
    query = request_query(request,
                          ["id", "songid"],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/v1/discovery/simiSong")
    return Http_Response(request, data.text)


def top(request):
    # 新歌速递
    '''
    全部:0 华语:7 欧美:96 日本:8 韩国:16
    '''
    query = request_query(request, ["type", {"areaId": 0}])
    query["total"] = True
    data = send(query).POST("weapi/v1/discovery/new/songs")
    return Http_Response(request, data.text)


def simiuser(request):
    # 获取最近 5 个听了这首歌的用户
    query = request_query(request,
                          ["id", "songid"])
    data = send(query).POST("weapi/discovery/simiUser")
    return Http_Response(request, data.text)


def new(request):
    # 新碟上架
    query = request_query(request,
                          # 全部：ALL 国内：ZH 欧美：EA 韩国：KR 日本：JP
                          ["area", {"area": "ALL"}],
                          ["limit", {"limit": 50}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/album/new")
    return Http_Response(request, data.text)


def like(request):
    # 给喜欢音乐的音乐点小心心
    query = request_query(request,
                          ["id", "trackId"],
                          "like",
                          ["alg", {"alg": "itembased"}],
                          ["time", {"time": 25}])
    url = "weapi/radio/like?alg={}&trackId={}&time={}".format(
        query["alg"], query["trackId"], query["time"])
    data = send({"trackId": query["trackId"], "like": query["like"]}).POST(url)
    return Http_Response(request, data.text)


def intelligence(request):
    query = request_query(request,
                          ["id", "songId"],
                          ["pid", "playlistId"],
                          ["sid", {"startMusicId": ""}],
                          ["count", {"count": 1}])
    if query["startMusicId"] == "":
        query["startMusicId"] = query["songId"]
    query["type"] = "fromPlayOne"
    data = send(query).POST("weapi/playmode/intelligence/list")
    return Http_Response(request, data.text)
