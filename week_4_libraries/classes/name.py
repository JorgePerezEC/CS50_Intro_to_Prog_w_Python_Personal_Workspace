import sys
# try:
#     print("Hello " + sys.argv[1].capitalize() + " " + sys.argv[2].capitalize())
# except IndexError:
#     print("Too few arguments")


# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1],sys.argv[2])

# print("Hello, my name is", sys.argv[1])
for arg in sys.argv[1:-1]:
    print("Hello, my name is", arg.capitalize())

"""
python name.py "Jorge Perez"
result: Hello, my name is Jorge Perez
"""
