from requests import get
from json import loads
from os import mkdir,path as p

path = 'download/'
BASE_URL = 'http://music.dsb.ink/api/'
DATE_URL = BASE_URL + 'comment/song?id='
INFO_URL = BASE_URL + 'song/detail?id='
SONG_URL = BASE_URL + 'song/test?id='
LYRIC_URL = BASE_URL + 'song/lyric?id='


headers = {
    'Proxy-Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }


class FLAC:
    def __init__(self,info):
        from mutagen.flac import FLAC as flac
        self.p = path + name
        audio = flac(self.p)
        for key, value in info.items():
            audio[key] = value
        self.id = info['description']
        self.audio = audio


    def picture(self,url):
        from mutagen.flac import Picture
        image = Picture()
        image.type = 3
        image.mime = 'image/jpeg'
        image.desc = 'front cover'
        image.data = get(url).content
        self.audio.add_picture(image)

    def lyric(self):
        try:
            self.audio['lyrics'] = getLyric(self.id)
        except:
            pass

    def save(self):
        self.audio.save()

class MP3:
    def __init__(self,info):
        from mutagen.mp3 import MP3 as mp3
        from mutagen.easyid3 import EasyID3
        from mutagen.id3 import ID3
        EasyID3.RegisterTextKey('description',"COMM")
        p = path + name
        audio = mp3(p,ID3=EasyID3)
        for key, value in info.items():
            try:
                audio[key] = value
            except:
                pass
        audio.save()
        self.audio = ID3(p)
        self.id = info['description']

    def picture(self,url):
        from mutagen.id3 import APIC
        self.audio.add(
            APIC(
                mime='image/jpeg',
                data=get(url).content
            )
        )

    def lyric(self):
        from mutagen.id3 import USLT
        try:
            self.audio.add(
                USLT(
                    text=getLyric(self.id),
                    encoding=3
                )
            )
        except:
            pass

    def save(self):
        self.audio.save()

def ProgressBar(percent, name, s='', total_length=0):
    bar = '#' * int(percent / 100 * total_length)
    bar = '\r【' + name + '】' + bar.ljust(total_length) + ' {:>4.1f}%|'.format(percent) + s
    print(bar, end='', flush=True)


def checkPath(s):
    if not p.exists(s):
        mkdir(s)

def getDate(date):
    from time import localtime,strftime
    if date == 0:
        comment = loads(get(DATE_URL + id).text)
        total = comment['total']
        if total > 20:
            comment = loads(get(DATE_URL + id + '&offset=' + str(int(total/20)*20)).text)
        date = comment['comments'][-1]['time']
    return strftime("%Y-%m-%d", localtime(int(date/1000)))

def getArtists(ar):
    s = ''
    for i in ar:
        s+=i['name']+'/'
    return s[:-1]

def getLyric(id):
    try:
        return loads(get(LYRIC_URL + id).text)['lrc']['lyric']
    except:
        return ''


def saveMusic(url,name):
    from contextlib import closing
    checkPath(path)

    with closing(get(url,headers=headers,stream=True)) as response:
        chunk_size = 1024
        temp = 0
        length = int(response.headers['Content-Length'])
        with open(path + name,'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                temp += chunk_size
                file.write(data)
                ProgressBar(float('%.1f' % (temp / length * 100)), name , '100%', 30)

def idParse(id):
    from re import search
    if id[:4] == 'http':
        return search('id=(\d+)',id).group(1)
    return id


if __name__ == '__main__':
    id = 'http://music.163.com/song?id=1381365569&userid=506530110'
    id = idParse(id)
    info = loads(get(INFO_URL + id).text)['songs'][0]
    song = loads(get(SONG_URL + id).text)['data'][0]
    date = getDate(info['publishTime'])
    detail = dict(
        title=info['name'],
        artist=getArtists(info['ar']),
        album=info['al']['name'],
        date=date,
        description=id,
        year=date[:4],
        encoder=''
    )
    type = song['type'].lower()
    songURL = song['url']
    songSize = song['size']
    picURL = info['al']['picUrl'] + '?param=260y260'
    name = '{}-{}.{}'.format(detail['title'],detail['artist'],type).replace('/','+')

    saveMusic(songURL,name)

    if type == 'mp3':
        music = MP3(detail)
    elif type == 'flac':
        music = FLAC(detail)

    music.picture(picURL)
    music.lyric()
    music.save()