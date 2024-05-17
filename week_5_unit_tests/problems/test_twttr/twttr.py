#author: Jorge Perez
import sys

def main():
    word_in = input("Input: ")
    print("Output:", shorten(word_in))

def shorten(word):
    new_word = ""
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            c = ""
        elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            c = ""
        new_word +=c
    return new_word

if __name__ == "__main__":
    main()
    sys.exit(100)
