import TwitterAPI
import json
from sys import argv

if __name__=="__main__":

    blocks = TwitterAPI.get_block_list(skip_status=False)["ids"]
    for i in blocks:
        info = TwitterAPI.get_user_info(i)
        print(json.dumps(info,indent=2,ensure_ascii=False))
