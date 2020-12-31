from django.shortcuts import render
from .__init__ import *
from requests import utils
from json import dumps, loads
from requests.models import Response

def home(requset):
    return Http_Response("", "这是用户API", "")


def login(request):
    # 用户登录
    query = request_query(request, "phone", "email",
                          "password", ["md5", {"md5": "false"}])
    query["password"] = MD5(query["password"]) if query.pop(
        "md5") == "false" else query["password"]
    if query["email"] == None:
        data: Response = send(dict(phone=query["phone"],
                         password=query["password"],
                         countrycode='86',
                         rememberLogin="true")).POST("weapi/login/cellphone", {'os':'pc'})
    else:
        data: Response = send(dict(username=query["email"],
                         password=query["password"],
                         rememberLogin='true')).POST("weapi/login", {"os": "pc"})
    cookies = utils.dict_from_cookiejar(data.cookies)
    saveFile("cookies", cookies)
    return Http_Response(request, data.text)


def sent(request):
    # 发送验证码
    query = request_query(request, ["phone", "cellphone"],
                          ["ctdoce", {"ctcode": 86}])
    data = send(query).POST("weapi/sms/captcha/sent")
    return Http_Response(request, data.text)


def verify(request):
    # 验证验证码
    query = request_query(request, ["phone", "cellphone"],
                          ["ctdoce", {"ctcode": 86}],
                          ["code", "captcha"])
    data = send(query).POST("weapi/sms/captcha/verify")
    return Http_Response(request, data.text)


def register(request):
    # 注册(修改密码)
    query = request_query(request,
                          ["code", "captcha"],
                          "phone", "password", "nickname",
                          ["md5", {"md5": "false"}])
    query["password"] = MD5(query["password"]) if query.pop(
        "md5") == "false" else query["password"]
    data = send(query).POST("weapi/register/cellphone")
    return Http_Response(request, data.text)


def checkphone(request):
    # 检测手机号码是否已注册
    query = request_query(request, ["phone", "cellphone"],
                          ["ctcode", {"countrycode": 86}])
    data = send(query, "eapi",
                url="/api/cellphone/existence/check").POST("http://music.163.com/eapi/cellphone/existence/check")
    return Http_Response(request, data.text)


def initname(request):
    # 初始化昵称
    query = request_query(request, ["name", "nickname"])
    data = send(query, "eapi",
                url="/api/activate/initProfile").POST("http://music.163.com/eapi/activate/initProfile")
    return Http_Response(request, data.text)


def rebind(request):
    # 手机号换绑
    query = request_query(request,
                          ["oldcode", "oldcaptcha"],
                          ["newcode", "captcha"], "phone",
                          ["ctcode", {"ctcode": 86}])
    data = send(query).POST("weapi/user/replaceCellphone")
    return Http_Response(request, data.text)


def logout(request):
    # 登出
    data = send().POST("weapi/logout", {"ua": "pc"})
    saveFile("cookies", "")
    return Http_Response(request, data.text)


def status(request):
    # 登录状态
    from re import findall, S, M
    data = send().GET("?").text
    try:
        body = findall(r"GUser=(.*?);.*?GBinds=(.*?);", data, S | M)[0]
        temp = findall(r'([a-zA-Z0-9_]*)(:"|:)(.*?)(",|,|})', body[0])
        bindings = loads(body[1])
        for i in range(0, 2):
            bindings[i]["tokenJsonStr"] = loads(bindings[i]["tokenJsonStr"])
        profile = "{"
        for i in temp:
            i = list(i)
            i[0] = '"{}"'.format(i[0])
            profile += "".join(i)
        res = {"code": 200,
               "profile": loads(profile),
               "bindings": bindings}
    except:
        res = {"status": 301, "body": {"code": 301}}
    return Http_Response(request, dumps(res))


def detail(request):
    # 用户详情
    query = request_query(request, "uid")
    cookie = getCookie()
    csrf = cookie["__csrf"] if "__csrf" in cookie else ""
    data = send({"csrf_token": csrf}).POST(
        "weapi/v1/user/detail/" + query["uid"])
    return Http_Response(request, data.text)


def playlist(request):
    # 用户歌单
    query = request_query(request, "uid",
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/user/playlist")
    return Http_Response(request, data.text)


def level(request):
    query = request_query(request, "uid")
    cookie = getCookie()
    csrf = cookie["__csrf"] if "__csrf" in cookie else ""
    data = send({"csrf_token": csrf}).POST(
        "weapi/user/level"
    )
    return Http_Response(request, data.text)


def album(request):
    # 已购专辑
    query = request_query(request,
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/digitalAlbum/purchased")
    return Http_Response(request, data.text)


def refresh(request):
    # 刷新登录
    data = send({}).POST("weapi/login/token/refresh")
    cookies = utils.dict_from_cookiejar(data.cookies)
    saveFile("cookies", cookies)
    return Http_Response(request, data.text)


def signin(request):
    # 每日签到
    query = request_query(request, ["type", {"type": "0"}])
    data = send(query).POST("weapi/point/dailyTask")
    return Http_Response(request, data.text)


def fm(request):
    # 私人FM
    data = send({}).POST("weapi/v1/radio/get")
    return Http_Response(request, data.text)


def trash(request):
    # FM垃圾桶
    query = request_query(request, ["id", "songId"])
    data = send(query).POST(
        "weapi/radio/trash/add?alg=RT&songId="+query["songId"]+"&time=25")
    return Http_Response(request, data.text)


def likelist(request):
    # 喜欢的音乐列表
    query = request_query(request, "uid")
    query["limit"] = 1
    query["offset"] = 0
    data = loads(send(query).POST("weapi/user/playlist").text)
    query = {"id": data["playlist"][0]["id"], "s": 0, "n": 10000}
    data = send({"url": BASE_URL + "api/v3/playlist/detail",
                 "params": query}, "linuxapi").POST("")
    return Http_Response(request, data)


def subcount(request):
    # 获取用户信息 , 歌单，收藏，mv, dj 数量
    data = send({}).POST("weapi/subcount")
    return Http_Response(request, data.text)


def record(request):
    # 获取用户播放记录
    query = request_query(request, "uid", ["type", {"type": 1}])
    data = send(query).POST("weapi/v1/play/record")
    return Http_Response(request, data.text)


def radio(request):
    # 用户电台用户创建的电台
    query = request_query(request, ["uid", "userId"])
    data = send(query).POST("weapi/djradio/get/byuser")
    return Http_Response(request, data.text)


def dj(request):
    # 获取用户创建的电台的详细信息
    query = request_query(request, "uid",
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    uid = query.pop("uid")
    data = send(query).POST("weapi/dj/program/" + uid)
    return Http_Response(request, data.text)


def follows(request):
    # 获取用户关注列表
    query = request_query(request, "uid",
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    uid = query.pop("uid")
    query["order"] = True
    data = send(query).POST("weapi/user/getfollows/"+uid)
    return Http_Response(request, data.text)


def fans(request):
    # 获取用户粉丝
    query = request_query(request, ["uid", "userId"],
                          ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    query["total"] = True
    data = send(query).POST("weapi/user/getfolloweds")
    return Http_Response(request, data.text)


def event(request):
    # 获取用户动态
    query = request_query(request, "uid",
                          ["time", {"time": -1}],
                          ["limit", {"limit": 30}])
    query["getcounts"] = True
    query["total"] = True
    uid = query.pop("uid")
    data = loads(send(query).POST("weapi/event/get/" + uid).text)
    for i in data["events"]:
        try:
            i["json"] = loads(i["json"])
        except:
            pass
    return Http_Response(request, dumps(data))


def events(request):
    # 获取动态消息
    query = request_query(request,
                          ["time", {"lasttime": -1}],
                          ["limit", {"pagesize": 30}])
    data = loads(send(query).POST("weapi/v1/event/get").text)
    for i in data["event"]:
        try:
            i["json"] = loads(i["json"])
        except:
            pass
    return Http_Response(request, dumps(data))


def event_forward(request):
    # 转发用户动态
    query = request_query(request,
                          ["uid", "eventUserId"],
                          ["evid", "id"],
                          ["content", {"forwards": ""}])
    data = send(query).POST("weapi/event/forward", {"os": "pc"})
    return Http_Response(request, data.text)


def event_del(request):
    # 删除用户动态
    query = request_query(request, ["evid", "id"])
    data = send(query).POST("weapi/event/delete")
    return Http_Response(request, data.text)


def event_share(request):
    # 分享歌曲、歌单、mv、电台、电台节目到动态
    query = request_query(request,
                          # song,playlist,mv,djprogram,djradio
                          ["type", {"type": "song"}],
                          ["msg", {"msg": ""}],
                          ["id", {"id": ""}])
    data = send(query).POST("weapi/share/friends/resource")
    return Http_Response(request, data.text)


def follow(request):
    # 关注 / 取消关注用户
    query = request_query(request, ["t", {"t": 1}], "uid")
    query["t"] = "follow" if query["t"] == "1" else "delfollow"
    data = send().POST("weapi/user/{}/{}".format(query["t"],
                                                 query["uid"]), {"os": "pc"})
    return Http_Response(request, data.text)


def cloud(request):
    # 获取云盘歌曲id
    query = request_query(request, ["limit", {"limit": 30}],
                          ["offset", {"offset": 0}])
    data = send(query).POST("weapi/v1/cloud/get")
    return Http_Response(request, data.text)
# 恭喜你发现了一个并没有什么卵用的彩蛋
# flag{I_aM_S0_6oR1n9}


def cloud_detail(request):
    # 云盘歌曲详情
    query = request_query(request, "id")
    info = {"songIds": query["id"].split(",")}
    data = send(info).POST("weapi/v1/cloud/get/byids")
    return Http_Response(request, data.text)


def cloud_del(request):
    # 删除云盘歌曲
    query = request_query(request, "id")
    data = send({"songIds": [query["id"]]}).POST("weapi/cloud/del")
    return Http_Response(request, data.text)


def setting(request):
    # 设置
    data = send().POST("weapi/user/setting")
    return Http_Response(request, data.text)


def getarea(request):
    # 获取地区参数
    data = send().POST("weapi/appcustomconfig/get")
    return Http_Response(request, data.text)


def update(request):
    # 更新用户信息
    query = request_query(request, "gender", "province",
                          "city", "birthday", "nickname", "signature")
    query["avatarImgId"] = "0"
    data = send(query).POST("weapi/user/profile/update")
    return Http_Response(request, data.text)


def star(request):
    # 资源点赞( MV,电台,视频)
    types = {
        "1": 'R_MV_5_',   # M V
        "4": 'A_DJ_1_',   # 电台
        "5": 'R_VI_62_',  # 视频
        "6": 'A_EV_2_'    # 动态
    }
    query = request_query(request,
                          ["t", {"t": 1}],
                          ["type", {"type": 1}], "id")
    tp = types[query["type"]]
    if tp == "A_EV_2_":
        info = {"threadId": query["id"]}
    else:
        info = {"threadId": tp + query["id"]}
    t = "like" if query["t"] == "1" else "unlike"
    data = send(info).POST("weapi/resource/" + t, {"os": "pc"})
    return Http_Response(request, data.text)
