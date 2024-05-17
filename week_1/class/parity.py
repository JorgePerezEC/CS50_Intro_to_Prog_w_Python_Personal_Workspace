def main():
    x = int(input("X: "))
    if is_even_elegant(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_even_elegant(n):
    # return True if n % 2 == 0 else False
    return n % 2 == 0

main()
# number = int(input("Type a int number: "))

# parity = number % 2

# if parity == 0:
#     print("You type an even number")
# else:
#     print("You type an odd number")
