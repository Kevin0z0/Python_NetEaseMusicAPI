from django.shortcuts import render
from .__init__ import *


def home(request):
    return Http_Response("", '这是歌手API', '')


def song(request):
    # 歌手单曲
    query = request_query(request, 'id')
    data = send({}).POST('weapi/v1/artist/' + query['id'])
    return Http_Response(request, data.text)


def album(request):
    # 歌手专辑
    query = request_query(request, 'id', ['limit', {'limit': 30}], [
        'offset', {'offset': 0}])
    query['total'] = True
    id = query.pop('id')
    data = send(query).POST('weapi/artist/albums/' + id)
    return Http_Response(request, data.text)


def album_new(request):
    # 最新专辑
    data = send().POST("weapi/discovery/newAlbum")
    return Http_Response(request, data.text)


def album_detail(request):
    # 获取专辑内容
    query = request_query(request, "id")
    data = send().POST("weapi/v1/album/"+query["id"])
    return Http_Response(request, data.text)


def album_dynamic(request):
    # 专辑动态信息
    query = request_query(request, "id")
    data = send(query).POST("weapi/album/detail/dynamic")
    return Http_Response(request, data.text)


def album_sub(request):
    # 收藏/取消收藏专辑
    query = request_query(request, "id", ["t", {"t": 1}])
    t = "sub" if query.pop("t") == "1" else "unsub"
    data = send(query).POST("weapi/album/" + t)
    return Http_Response(request, data.text)


def album_sublist(request):
    # 获取已收藏专辑列表
    query = request_query(request,
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/album/sublist")
    return Http_Response(request, data.text)


def desc(request):
    # 歌手详情
    query = request_query(request, 'id')
    data = send(query).POST('weapi/artist/introduction')
    return Http_Response(request, data.text)


def mv(request):
    # 歌手MV
    query = request_query(request,
                          ['id', 'artistId'],
                          ['limit', {'limit': 30}],
                          ['offset', {'offset': 0}])
    query['total'] = True
    data = send(query).POST('weapi/artist/mvs')
    return Http_Response(request, data.text)


def top(request):
    # 热门歌手
    query = request_query(request,
                          ['limit', {'limit': 30}],
                          ['offset', {'offset': 0}])
    query["total"] = True
    data = send(query).POST("weapi/artist/top")
    return Http_Response(request, data.text)


def simi(request):
    # 获取相似歌手
    query = request_query(request, ["id", "artistid"])
    data = send(query).POST("weapi/discovery/simiArtist")
    return Http_Response(request, data.text)


def lists(request):
    # 歌手分类列表
    query = request_query(request,
                          ["cat", {"categoryCode": 1001}],
                          ["init", {"initial": ""}],
                          ['limit', {'limit': 30}],
                          ['offset', {'offset': 0}])
    try:
        query["initial"] = ord(query["initial"].upper())
    except:
        pass
    data = send(query).POST("weapi/artist/list")
    return Http_Response(request, data.text)


def sub(request):
    # 收藏/取消收藏歌手
    query = request_query(request,
                          ["t", {"t": 1}],
                          ["id", "artistId"])
    query["artistIds"] = "[{}]".format(query["artistId"])
    t = "sub" if query.pop("t") == "1" else "unsub"
    data = send(query).POST("weapi/artist/"+t)
    return Http_Response(request, data.text)


def sublist(request):
    # 收藏的歌手列表
    query = request_query(request,
                          ['limit', {'limit': 30}],
                          ['offset', {'offset': 0}])
    query["total"] = True
    data = send(query).POST("weapi/artist/sublist")
    return Http_Response(request, data.text)


def topsong(request):
    # 热门50首歌
    query = request_query(request, "id")
    data = send(query).POST("weapi/artist/top/song")
    return Http_Response(request, data.text)


def toplist(request):
    # 歌手榜
    query = {"type": 1, "limit": 100, "offset": 0, "total": True}
    data = send(query).POST("weapi/toplist/artist")
    return Http_Response(request, data.text)
