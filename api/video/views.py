from .__init__ import *


def home(request):
    return Http_Response("", "这是视频API", "")


def url(request):
    # 获取视频URL
    query = request_query(request, "id", ["res", {"resolution": 1080}])
    query["ids"] = '["{}"]'.format(query.pop("id"))
    data = send(query).POST("weapi/cloudvideo/playurl")
    return Http_Response(request, data.text)


def detail(request):
    # 获取视频详情
    query = request_query(request, "id")
    data = send(query).POST("weapi/cloudvideo/v1/video/detail")
    return Http_Response(request, data.text)


def lists(request):
    # 获取视频标签列表
    data = send().POST("weapi/cloudvideo/group/list")
    return Http_Response(request, data.text)


def group(request):
    # 获取视频标签下的视频
    query = request_query(request,
                          ["id", "groupId"],
                          ["offset", {"offset": 0}],
                          ["res", {"resolution": 1080}])
    query["needUrl"] = True
    data = send(query).POST("weapi/videotimeline/videogroup/get")
    return Http_Response(request, data.text)


def related(request):
    # 相关视频
    query = request_query(request, "id")
    query["type"] = 0 if query["id"].isdigit() else 1
    data = send(query).POST("weapi/cloudvideo/v1/allvideo/rcmd")
    return Http_Response(request, data.text)


def sub(request):
    # 收藏与取消收藏视频
    query = request_query(request, "id", ["t", {"t": 1}])
    t = "sub" if query.pop("t") == "1" else "unsub"
    data = send(query).POST("weapi/cloudvideo/video/" + t)
    return Http_Response(request, data.text)
