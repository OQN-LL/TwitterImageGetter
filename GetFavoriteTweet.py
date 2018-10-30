import TwitterAPI
import json
from sys import argv

if __name__=="__main__":
    if len(argv) < 2:
        print("Error")
        quit()

    for i in range(20):
        for tw in TwitterAPI.get_favorite_tweets(i+1,argv[1]):
            try:
                #media = tw["extended_entities"]["media"]#["video_info"]
                print(json.dumps(tw,indent=2,ensure_ascii=False))
            except:
                pass
