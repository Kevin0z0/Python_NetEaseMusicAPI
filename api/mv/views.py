from django.shortcuts import render
from .__init__ import *
from json import dumps


def home(request):
    return Http_Response("", "这是MV API", "")


def all(request):
    # 全部MV
    query = request_query(request,
                          ["area", {"area": "全部"}],
                          ["type", {"type": "全部"}],
                          ["order", {"order": "上升最快"}],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = "true"
    dic = {"tags": dumps({"地区": query["area"], "类型": query["type"], "排序": query["order"]}),
           "offset": query["offset"],
           "limit": query["limit"],
           "total": "true"}
    data = send(dic).POST("https://interface.music.163.com/weapi/mv/all")
    return Http_Response(request, data.text)


def new(request):
    # 最新MV
    query = request_query(request,
                          ["area", {"area": ""}],
                          ["limit", {"limit": 30}])
    query["total"] = True
    data = send(query).POST("https://interface.music.163.com/weapi/mv/first")
    return Http_Response(request, data.text)


def netease(request):
    # 网易出品MV
    query = request_query(request,
                          ["limit", {"limit": 10}],
                          ["offset", {"offset": 0}])
    data = send(query).POST(
        "https://interface.music.163.com/weapi/mv/exclusive/rcmd")
    return Http_Response(request, data.text)


def recommend(request):
    # 推荐MV
    data = send().POST("weapi/personalized/mv")
    return Http_Response(request, data.text)


def simi(request):
    # 相似MV
    query = request_query(request, "mvid")
    data = send(query).POST("weapi/discovery/simiMV")
    return Http_Response(request, data.text)


def top(request):
    # MV排行
    query = request_query(request,
                          ["area", {"area": ""}],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/mv/toplist")
    return Http_Response(request, data.text)


def detail(request):
    # MV详情
    query = request_query(request, ["mvid", "id"])
    data = send(query).POST("weapi/mv/detail")
    return Http_Response(request, data.text)


def url(request):
    # MV地址
    query = request_query(request, ["mvid", "id"], ["r", {"r": 1080}])
    data = send(query).POST("weapi/song/enhance/play/mv/url")
    return Http_Response(request, data.text)


def sub(request):
    # 收藏/取消收藏 MV
    query = request_query(request, ["mvid", "mvId"], ["t", {"t": 1}])
    t = "sub" if query.pop("t") == "1" else "unsub"
    query["mvIds"] = '["' + query["mvId"] + '"]'
    data = send(query).POST("weapi/mv/" + t)
    return Http_Response(request, data.text)


def sublist(request):
    # 收藏的 MV 列表
    query = request_query(request,
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/cloudvideo/allvideo/sublist")
    return Http_Response(request, data.text)
