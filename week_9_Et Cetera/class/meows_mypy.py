# $ mypy meows_mypy.py

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)

def meow2(n: int) -> str: # Specify the output type
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow2(number)
print(meows, end="")
