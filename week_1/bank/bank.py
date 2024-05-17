def hello_bill(hello):
    return hello.startswith("h")


sentence = input("Greeting: ").lower().strip()
sentence = sentence.replace(",","")
first_w = sentence.split(" ")

if hello_bill(sentence):
    if first_w[0] == "hello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")

