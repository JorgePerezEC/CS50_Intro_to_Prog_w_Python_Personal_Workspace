def main():
    name = input("What's your name? ")
    hey = hello(name)
    print(hey)


def hello(to="world"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
