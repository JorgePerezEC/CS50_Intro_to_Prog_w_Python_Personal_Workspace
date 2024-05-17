def main():
    name = input("camelCase: ")
    name_snake_version = snake_conv(name)
    print("snake_case: " + name_snake_version)

def snake_conv(inp):
    isCapital = False
    f_word = ""
    for c in inp:
        # print(c, end ="")
        if c.isupper():
            isCapital = True
        else:
            isCapital = False

        if isCapital:
            c = c.replace(c, "_"+c.lower())

        f_word += c
    return f_word

main()
