def main():
    sentence = input("Greeting: ")
    sentence = sentence.replace(",","")
    amount = value(sentence)
    print(f"${amount}")


def value(greeting):
    greeting = greeting.lower().strip()
    first_w = greeting.split(" ")
    if greeting.startswith("h"):
        if first_w[0] == "hello":
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()
