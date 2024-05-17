while True:
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
    except ValueError:
        print("x is no an integer ")
    else:
        break

print(f"x: {x}")
