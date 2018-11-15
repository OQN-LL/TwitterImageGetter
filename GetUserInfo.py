import TwitterAPI
import json
from sys import argv

if __name__=="__main__":
    #if len(argv) < 2:
    #    print("Error")
    #    quit()

    user = TwitterAPI.get_user_info(2463424812)
    print(json.dumps(user,indent=2,ensure_ascii=False))
