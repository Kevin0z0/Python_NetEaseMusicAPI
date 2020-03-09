from .__init__ import *


types = {
    "0": 'R_SO_4_',   # 歌曲
    "1": 'R_MV_5_',   # M V
    "2": 'A_PL_0_',   # 歌单
    "3": 'R_AL_3_',   # 专辑
    "4": 'A_DJ_1_',   # 电台
    "5": 'R_VI_62_',  # 视频
    "6": 'A_EV_2_'    # 动态
}


def pub(request, url, cookies={"os": "pc"}):
    query = request_query(request,
                          ["id", "rid"],
                          ["limit", {"limit": 20}],
                          ["offset", {"offset": 0}],
                          ["before", {"beforeTime": 0}])
    data = send(query).POST("weapi/v1/resource/" +
                            url + query["rid"], cookies)
    return data.text


def home(request):
    # 发送删除回复评论
    query = request_query(request, "id", "type", "t", "cid", "content")
    if not query["id"]:
        return Http_Response("", "这是评论API", "")
    info = {}
    t = {"0": "delete", "1": "add", "2": "reply"}[query["t"]]
    tp = types[query["type"]]
    id = query["id"]
    info["threadId"] = id if tp == "A_EV_2_" else tp + id
    if t == "add":
        info["content"] = query["content"]
    elif t == "delete":
        info["commentId"] = query["cid"]
    elif t == "reply":
        info["commentId"] = query["cid"]
        info["content"] = query["content"]
    data = send(info).POST("weapi/resource/comments/" + t, {"os": "pc"})
    return Http_Response(request, data.text)


def song(request):
    # 歌曲评论
    return Http_Response(request, pub(request, "comments/R_SO_4_"))


def album(request):
    # 专辑评论
    return Http_Response(request, pub(request, "comments/R_AL_3_"))


def playlist(request):
    # 歌单评论
    return Http_Response(request, pub(request, "comments/A_PL_0_"))


def dj(request):
    # 电台评论
    return Http_Response(request, pub(request, "comments/A_DJ_1_"))


def video(request):
    # 视频评论
    return Http_Response(request, pub(request, "comments/R_VI_62_"))


def mv(request):
    # 视频评论
    return Http_Response(request, pub(request, "comments/R_MV_5_"))


def hot(request):
    # 热门评论
    query = request_query(request, "type")
    return Http_Response(request, pub(request, "hotcomments/"+types[query["type"]]))


def event(request):
    # 动态评论
    query = request_query(request, "id",
                          ["limit", {"limit": 20}],
                          ["offset", {"offset": 0}],
                          ["before", {"beforeTime": 0}])
    id = query.pop("id")
    data = send(query).POST("weapi/v1/resource/comments/" + id)
    return Http_Response(request, data.text)


def like(request):
    # 点赞/取消点赞评论
    query = request_query(request, "id", "type", [
                          "t", {"t": 1}], ["cid", "commentId"])
    t = "like" if query.pop("t") == "1" else "unlike"
    tp = types[query.pop("type")]
    id = query.pop("id")
    query["threadId"] = id if tp == "A_EV_2_" else tp + id
    print(query)
    data = send(query).POST("weapi/v1/comment/" + t, {"os": "pc"})
    return Http_Response(request, data.text)
