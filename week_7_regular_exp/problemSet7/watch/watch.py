import re
import sys
#Author: Jorge Perez

def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r".+(?:https?://)(?:www\.)?youtube\.com(?:/embed)/([a-z0-9]+)(?:\" ?.+)$",s, re.IGNORECASE)
    if matches:
        # print(matches.groups())
        matches = f"https://youtu.be/{matches.group(1)}"
        return matches
    else:
        return None

if __name__ == "__main__":
    main()
