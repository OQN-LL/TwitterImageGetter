# coding:utf-8

from requests_oauthlib import OAuth1Session
from configparser import ConfigParser
import json
import os
import sys
import urllib
import Consts

counter = 0
root = "./images/"

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
        "count" : 200,
        "include_entities" : 1
    }
    oath = craete_oath_session()
    res = oath.get(url,params = params)

    if res.status_code != 200:
        print("Error : {0}".format(res.status_code))
        return None
    return json.loads(res.text)

def save_image(tweets):
    global counter
    for tw in tweets:
        try:
            images = tw["extended_entities"]["media"]#画像のパスの取得
            save_path = root + tw["user"]["screen_name"]#ツイート主のscreen_nameを取得
            os.makedirs(save_path,exist_ok=True)#ツイート主用のディレクトリがなければ作成

            for img_path in images:
                url = img_path["media_url"]
                url_large = url + ":large"
                save_file_path = save_path + "/" + os.path.basename(url)
                with open(save_file_path,"wb") as f:
                    img = urllib.request.urlopen(url_large,timeout=20).read()
                    f.write(img)
                    counter += 1
                    print("saved [{num: 4d}] : {url}".format(num=counter,url=save_file_path))

        except KeyError:
            pass


if __name__ == "__main__":

    for i in range(1,20):
        save_image(get_favorite_tweets(i,screen_name))
    print("saved {num} images".format(num=counter))
