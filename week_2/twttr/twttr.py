#author: Jorge Perez
import sys

def main():
    word_in = input("Input: ")
    delete_vowels(word_in)

def delete_vowels(word):
    new_word = ""
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            c = ""
        elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            c = ""
        new_word +=c
    print("Output: " + new_word)

main()
