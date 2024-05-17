name = input("What's your name: ")

# if name == "Harry" or name == "Hermione":
#     print("Griffindor")
# # elif name == "Hermione":
# #     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who??")


# Match use

match name:
    case "Harry" | "Ron" | "Hermione" | "Neville":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    # case "Ron":
    #     print("Griffindor")
    case _:
        print(f"Who the hell is {name}??")
