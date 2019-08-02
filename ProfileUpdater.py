from TwitterAPI import update_name
from random import choice
import re


if __name__ == "__main__":
    with open("profile_list.txt", "r") as f:
        names = re.sub(r"\n$", "", f.read()).split("\n")
    print(choice(names))
    # update_name("test")
