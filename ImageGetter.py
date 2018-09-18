# coding:utf-8

from requests_oauthlib import OAuth1Session
from configparser import ConfigParser
import json
import os
import sys
import urllib
import Consts

counter_image = 0
counter_video = 0
root_image = "./images/"
root_video = "./videos/"
page_size = 200

cfg = ConfigParser()
cfg.read(Consts.configFile)
token = cfg["token"]
screen_name = cfg["account"]["screen_name"]
oath_keys = {
    "consumer_key" : token[Consts.CK],
    "cousumer_secret" : token[Consts.CS],
    "access_token" : token[Consts.AT],
    "access_token_secret" : token[Consts.ATS]
}

def craete_oath_session():
    return OAuth1Session(
        token[Consts.CK],
        token[Consts.CS],
        token[Consts.AT],
        token[Consts.ATS]
    )

def get_favorite_tweets(page,screen_name):
    url = "https://api.twitter.com/1.1/favorites/list.json?"
    params = {
        "screen_name" : screen_name,
        "page" : page,
        "count" : page_size,
        "include_entities" : 1
    }
    oath = craete_oath_session()
    res = oath.get(url,params = params)

    if res.status_code != 200:
        print("Error : {0}".format(res.status_code))
        return None
    return json.loads(res.text)

def save_image(tweets):
    global counter_image
    global counter_video
    for tw in tweets:
        try:
            media = tw["extended_entities"]["media"]#画像・動画オブジェクトの取得
            for media_path in media:
                if media_path["type"] == "photo":#画像の時
                    save_path = root_image + tw["user"]["screen_name"]
                    os.makedirs(save_path,exist_ok=True)#ツイート主用のディレクトリがなければ作成
                    url = media_path["media_url"]
                    url_large = url + ":large"
                    save_file_path = save_path + "/" + os.path.basename(url)
                    if os.path.exists(save_file_path):
                        print("skip image : {url}".format(url=save_file_path))
                        break
                    with open(save_file_path,"wb") as f:
                        img = urllib.request.urlopen(url_large,timeout=20).read()
                        f.write(img)
                        counter_image += 1
                    print("saved image [{num: 4d}] : {url}".format(num=counter_image,url=save_file_path))

                elif media_path["type"] == "video":#動画の時
                    save_path = root_video + tw["user"]["screen_name"]
                    os.makedirs(save_path,exist_ok=True)#ツイート主用のディレクトリがなければ作成
                    #動画の中でbitrateが最大のmp4動画のurlを得る
                    url = max([i for i in media_path["video_info"]["variants"] if i["content_type"] == "video/mp4"],key=lambda e:e["bitrate"])["url"]
                    save_file_path = (save_path + "/" + os.path.basename(url)).split("?")[0]
                    if os.path.exists(save_file_path):
                        print("skip video {url}".format(url=save_file_path))
                        break
                    with open(save_file_path,"wb") as f:
                        vdo = urllib.request.urlopen(url,timeout=180).read()
                        f.write(vdo)
                        counter_video += 1
                    print("saved video [{num: 4d}] ; {url}".format(num=counter_video,url=save_file_path))

        except (KeyError,ValueError):
            pass


def get_medias(end):
    for i in range(0,end):
        save_image(get_favorite_tweets(i+1,screen_name))
    print("saved {num} images".format(num=counter_image))
    print("saved {num} videos".format(num=counter_video))

if __name__ == "__main__":
    get_medias(20)
