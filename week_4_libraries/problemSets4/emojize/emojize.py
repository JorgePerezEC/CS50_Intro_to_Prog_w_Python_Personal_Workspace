import emoji

def main():
    empoji_in = input("Input: ")
    print("Output:", emoji.emojize(empoji_in, language='alias'))
    # print(emoji.emojize('Python is :thumbs_up:', language='alias'))

main()
