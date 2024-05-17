def main():
    sentence = input("Greeting: ").lower().strip()
    sentence = sentence.replace(",","")
    amount = value(sentence)
    print(f"${amount}")


def value(greeting):
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
