def main():
    user_input = input("Type your input: ")
    convert(user_input)

def convert(in_string):

    in_string = in_string.replace(":(","🙁")
    in_string = in_string.replace(":)","🙂")
    print(in_string)

main()
