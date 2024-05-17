#author: Jorge Perez

def main():
    word_in = input("Input: ")
    print(shorten(word_in))

def shorten(word):
    new_word = ""
    for c in word:
        if c == "a" or c == "e" or c == "i" or c == "o":
            c = ""
        elif c == "A" or c == "E" or c == "I" or c == "O":
            c = ""
        new_word +=c
    return f"Output: {new_word}"

if __name__ == "__main__":
    main()
