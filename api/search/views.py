from django.shortcuts import render
from .__init__ import *


def home(request):
    # type:  1: 单曲, 10: 专辑, 100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 1009: 电台, 1014: 视频
    query = request_query(request,
                          ["value", "s"],
                          ["type", {"type": 1}],
                          ["limit", {"limit": 10}],
                          ["offset", {"offset": 0}])
    if query["s"]:
        data = send(query).POST("weapi/search/get")
        return Http_Response(request, data.text)
    return Http_Response("", "这里是搜索API", "")


def default(request):
    # 默认搜索关键词
    data = send(url="/api/search/defaultkeyword/get", encrypt_method="eapi").POST(
        "http://interface3.music.163.com/eapi/search/defaultkeyword/get")
    return Http_Response(request, data.text)


def suggest(request):
    # 搜索建议
    query = request_query(request,
                          ["value", "s"],
                          ["type", {"type": "web"}])
    rtype = "web" if query.pop("type") == "web" else "keyword"
    data = send(query).POST("weapi/search/suggest/"+rtype)
    return Http_Response(request, data.text)


def multimatch(request):
    # 搜索多重匹配
    query = request_query(request, ["type", {"type": 1}], ["value", {"s": ""}])
    data = send(query).POST("weapi/search/suggest/multimatch")
    return Http_Response(request, data.text)


def hot(request):
    # 热搜列表(简略)
    query = {"type": 1111}
    data = send(query).POST("weapi/search/hot", cookie={"ua": "mobile"})
    return Http_Response(request, data.text)


def hotdetail(request):
    # 热搜列表(详细)
    data = send().POST("weapi/hotsearchlist/get")
    return Http_Response(request, data.text)
