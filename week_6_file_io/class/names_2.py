# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     if len(line) > 1:
#         print("Hello," , line.rstrip())

"""
# VERSION 2
names = []
with open("names.txt", "r") as file:
    for line in file:
        if line != "":
            names.append(line)
            # print("hello,", line.rstrip())
    for name in sorted(names):
        print("hello,", name.rstrip()) # Too large
"""

with open("names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        if len(line) >= 2 and line.rstrip() == "Harry":
            print("You are the chosen,", line.rstrip())
