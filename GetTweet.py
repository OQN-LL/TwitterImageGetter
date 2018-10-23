import TwitterAPI
import json
from sys import argv

if __name__=="__main__":
    if len(argv) < 2:
        print("Error")
        quit()
    tw = TwitterAPI.get_tweet(argv[1])
    print(json.dumps(tw,indent=2,ensure_ascii=False))
