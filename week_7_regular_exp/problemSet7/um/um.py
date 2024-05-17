import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count_um = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(count_um)

if __name__ == "__main__":
    main()
