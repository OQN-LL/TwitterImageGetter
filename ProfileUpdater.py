from TwitterAPI import update_profile
from random import choice
import re


if __name__ == "__main__":
    with open("profile_list.txt", "r") as f:
        profiles = re.sub(r"\n$", "", f.read()).split("\n")
    print(choice(profiles))
    # update_profile("test")
