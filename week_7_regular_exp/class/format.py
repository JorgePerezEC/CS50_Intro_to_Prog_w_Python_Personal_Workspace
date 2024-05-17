import re

name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# print(matches)

if matches:= re.search(r"^(.+), *(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"
    #same
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"hello, {name}")



# print(f"Hello, {name}")

# if "," in name:
#     last, first = name.split(',')
#     name = f"{first} {last}"


# print(f"Hello, {name}")
