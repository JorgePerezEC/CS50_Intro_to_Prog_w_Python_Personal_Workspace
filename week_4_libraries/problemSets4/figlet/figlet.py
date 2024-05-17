from pyfiglet import Figlet
import sys
from random import choice


f = Figlet()
font_list = f.getFonts()

if len(sys.argv) == 3:

    if sys.argv[1] != "-f" and sys.argv[1] != "-font":
        sys.exit("Invalid usage")
    else:
        font_exist = False
        # f = Figlet()
        # font_list = f.getFonts()

        for font in font_list:
            # print(font, sys.argv[2])
            if font == sys.argv[2]:
                # print("Existe")
                font_exist = True

        if font_exist:
            text = input("Input: ")
            fig = Figlet(font = sys.argv[2])
            print(fig.renderText(text))
        else:
            sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    text = input("Input: ")
    font_random = choice(font_list)
    # print(font_list)
    # print("random: ", font_random)
    fig = Figlet(font = font_random)
    print(fig.renderText(text))
else:
    sys.exit("Invalid usage")


