def main():
    print("Amount Due: 50")
    change = calc_change()
    print("Change Owed: " + str(change))

def calc_change():
    coke_price = 50
    change = 0
    # money = int(input("Insert Coin: "))
    money = 0
    while coke_price > 0:

        money = int(input("Insert Coin: "))

        if money == 5 or money == 10 or money == 25:
            coke_price = coke_price - money

            if coke_price < 0:
                change = - coke_price
            elif coke_price > 0:
                print("Amount Due: " + str(coke_price))
            else:
                change = 0
        else:
            print("Amount Due: " + str(coke_price))

    return change

main()
