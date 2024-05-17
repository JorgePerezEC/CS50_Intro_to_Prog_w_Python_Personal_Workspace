# x = input("What's X? ")
# y = input("What's Y? ")

# z = int(x) + int(y)
# print(z)

print("Version 2")

# Version 2
# x = int(input("X value: "))
# y = int(input("Y value: "))

x = float(input("X value: "))
y = float(input("Y value: "))
print(x + y)
print(round(x + y))
z = round(x + y)
print(f"z = x + y = {z:,}")  #Allows to separate thousand units

# Division
div = x/y

print(div)
print(f"x/y= {div: .2f}")  #same of round(div,2)

# Version 3
# print(int(input("X value: ") + int(input("Y value: "))))
