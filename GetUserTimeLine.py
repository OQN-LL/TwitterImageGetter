#coding : utf-8
import TwitterAPI
from sys import argv



if __name__=="__main__":
    if len(argv) < 2:
        print("a")
        quit()
    
    for i in range(20):
        print(TwitterAPI.get_user_timeline(i+1,argv[1]))
