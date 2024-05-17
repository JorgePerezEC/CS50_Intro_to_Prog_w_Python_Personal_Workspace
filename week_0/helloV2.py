def main():
    # name = input("What's your name? ")
    # hello()
    x = int(input("X value: "))
    y = int(input("Y value: "))
    z = totalValue(x,y)
    print(f"Total amount: ${z:.2f}")

def hello(to="James"):
    print(f"Hi, {to.strip().title()}")

def totalValue(x,y=60):
    z = x + y
    return z

def square(x):
    y = pow(x, 2)

main()
