from json import loads
from django.http import HttpResponse

BASE_URL = "https://music.163.com/"


def readFile(method, path, mode="r"):
    with open(path, mode) as f:
        if method == "read":
            return f.read()
        elif method == "readlines":
            return f.readlines()


def saveFile(path, content, mode="w"):
    with open(path, mode) as f:
        f.write(str(content))


def getCookie():
    return loads(
        readFile("read", "cookies").replace("'", '"').encode()
    )


def request_query(r, *args):
    # ["id",{"ids":800435}] ["id","ids"] "id"
    def check(txt):
        if type(txt) == int:
            return str(txt)
        return txt
    dic = {}
    try:
        info = loads(r.body)
    except:
        pass
    for i in [*args]:
        if type(i) == list:
            j = i[1]
            i = i[0]
        else:
            j = i
        if r.method == "POST":
            try:
                query = info[i] if r.body[0] == 123 else r.POST.get(i)
            except:
                query = None
        elif r.method == "GET":
            query = r.GET.get(i)
        try:
            if type(j) == dict:
                key = list(j.keys())[0]
                dic[key] = check(query if query else j[key])
            else:
                dic[j] = check(query)
        except:
            dic[i] = check(query)
    return dic


def Http_Response(r, text, type="application/json,charset=UTF-8"):
    try:
        query = request_query(r, "var", "cb")
    except:
        query = {"var": None, "cb": None}
    if query["var"] or query["cb"]:
        if query["var"]:
            text = "{}={}".format(query["var"], text)
        elif query["cb"]:
            text = "{}({})".format(query["cb"], text)
        type = "text/plain; charset=UTF-8"
    if type == "":
        return HttpResponse(text)
    return HttpResponse(text, content_type=type)


def getFLAC(mid):
    import requests
    from base64 import b64encode
    from Cryptodome.Cipher import DES
    data = "wy_999_" + mid + ".flac"
    key = bytes([36, 16, 93, 156, 78, 66, 218, 32])
    iv = bytes([55, 183, 236, 79, 36, 99, 167, 56])
    generator = DES.new(key, DES.MODE_CBC, iv)
    pad = 8 - len(data) % 8
    pad_str = ""
    for _ in range(pad):
        pad_str = pad_str + chr(pad)
    result = b64encode(generator.encrypt((data + pad_str).encode()))
    return requests.get("http://114.67.65.49/api/music/?type=url&key=" + b64encode(result).decode()).text
