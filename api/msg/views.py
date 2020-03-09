from .__init__ import *


def home(request):
    return Http_Response("", "这是消息API", "")


def private(request):
    # 私信
    query = request_query(request, ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/msg/private/users")
    return Http_Response(request, data.text)


def history(request):
    # 私信历史
    query = request_query(request,
                          ["uid", "userId"],
                          ["limit", {"limit": 30}],
                          ["time", {"time": 0}])
    query["total"] = "true"
    data = send(query).POST("weapi/msg/private/history")
    return Http_Response(request, data.text)


def sendmsg(request):
    # 发送私信
    query = request_query(request, ["id", {"id": ""}], "msg", "uid")
    query["type"] = "text" if query["id"] == "" else "playlist"
    query["userIds"] = '[{}]'.format(query.pop("uid"))
    data = send(query).POST("weapi/msg/private/send")
    return Http_Response(request, data.text)


def comment(request):
    # 评论通知
    query = request_query(request, "uid",
                          ["limit", {"limit": 30}],
                          ["time", {"beforeTime": -1}])
    query["total"] = "true"
    data = send(query).POST("weapi/v1/user/comments/" + query["uid"])
    return Http_Response(request, data.text)


def forwards(request):
    # @我通知
    query = request_query(request, ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = "true"
    data = send(query).POST('weapi/forwards/get')
    return Http_Response(request, data.text)


def notices(request):
    # 通知
    query = request_query(request, ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = "true"
    data = send(query).POST('weapi/msg/notices')
    return Http_Response(request, data.text)
