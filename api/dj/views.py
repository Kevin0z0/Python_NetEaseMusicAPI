from django.shortcuts import render
from .__init__ import *


def home(request):
    return Http_Response("", "这是电台API", "")


def banner(request):
    # 电台banner
    data = send().POST("weapi/djradio/banner/get", {"os": "pc"})
    return Http_Response(request, data.text)


def hot(request):
    # 热门电台
    query = request_query(request, ["limit", {"limit": 30}], [
                          "offset", {"offset": 0}])
    data = send(query).POST("weapi/djradio/hot/v1")
    return Http_Response(request, data.text)


def hot_radio(request):
    # 类别热门电台
    query = request_query(request,
                          ["cid", "cateId"],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}],)
    data = send(query).POST("weapi/djradio/hot")
    return Http_Response(request, data.text)


def detail(request):
    # 电台详情
    query = request_query(request, ["rid", "id"])
    data = send(query).POST("weapi/djradio/get")
    return Http_Response(request, data.text)


def pay(request):
    # 付费精品
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/djradio/toplist/pay")
    return Http_Response(request, data.text)


def program(request):
    # 电台节目
    query = request_query(request,
                          ["rid", "radioId"],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}],
                          "asc")
    data = send(query).POST("weapi/dj/program/byradio")
    return Http_Response(request, data.text)


def program_detail(request):
    # 节目详情
    query = request_query(request, "id")
    data = send(query).POST("weapi/dj/program/detail")
    return Http_Response(request, data.text)


def program_toplist(request):
    # 节目榜
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/program/toplist/v1")
    return Http_Response(request, data.text)


def program_toplist_hours(request):
    # 节目24小时榜
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/djprogram/toplist/hours")
    return Http_Response(request, data.text)


def streamer_hours(request):
    # 24小时主播榜
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/dj/toplist/hours")
    return Http_Response(request, data.text)


def streamer_newcomer(request):
    # 主播新人榜
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/dj/toplist/newcomer")
    return Http_Response(request, data.text)


def streamer_hot(request):
    # 最热主播榜
    query = request_query(request, ["limit", {"limit": 100}])
    data = send(query).POST("weapi/dj/toplist/popular")
    return Http_Response(request, data.text)


def toplist(request):
    # 新晋电台榜/热门电台榜
    query = request_query(request, ["limit", {"limit": 100}], [
                          "offset", {"offset": 0}], ["type", {"type": 0}])
    data = send(query).POST("weapi/djradio/toplist")
    return Http_Response(request, data.text)


def catelist(request):
    # 电台分类
    data = send().POST("weapi/djradio/category/get")
    return Http_Response(request, data.text)


def recommend(request):
    # 精选电台
    data = send().POST("weapi/djradio/recommend/v1")
    return Http_Response(request, data.text)


def recommend_type(request):
    # 分类推荐
    query = request_query(request, ["cid", "cateId"])
    data = send(query).POST("weapi/djradio/recommend")
    return Http_Response(request, data.text)


def category_recommend(request):
    # 推荐类型
    data = send().POST("weapi/djradio/home/category/recommend")
    return Http_Response(request, data.text)


def category_excludehot(request):
    # 非热门类型
    data = send().POST("weapi/djradio/category/excludehot")
    return Http_Response(request, data.text)


def sub(request):
    # 订阅
    query = request_query(request, ["rid", "id"], ["type", {"type": 1}])
    type = "sub" if query.pop("type") == "1" else "unsub"
    data = send(query).POST("weapi/djradio/" + type)
    return Http_Response(request, data.text)


def sublist(request):
    # 订阅列表
    query = request_query(request,
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/djradio/get/subed")
    return Http_Response(request, data.text)


def paygift(request):
    # 付费精选
    query = request_query(request,
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/djradio/home/paygift/list?_nmclfl=1")
    return Http_Response(request, data.text)


def today(request):
    # 今日优选
    query = request_query(request, ["page", {"page": 0}])
    data = send(query).POST("weapi/djradio/home/today/perfered")
    return Http_Response(request, data.text)


def djprogram(request):
    # 推荐电台
    data = send().POST("weapi/personalized/djprogram")
    return Http_Response(request, data.text)


def program_recommend(request):
    # 推荐节目
    query = request_query(request, ["limit", {"limit": 10}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/program/recommend/v1")
    return Http_Response(request, data.text)
