
from TwitterAPI import update_profile
from random import choice
import re

profile_temp = "名前 : __「」 ()_ ⋀|__ , __OQN__ アカウントの名前は30分に1回変わります({cnt}種)"

if __name__ == "__main__":
    with open("profile_list.txt", "r") as f:
        names = re.sub(r"\n$", "", f.read()).split("\n")
    update_profile(profile_temp.format(cnt=len(names)), choice(names))
