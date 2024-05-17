def main():
    calculate_amount()



def calculate_amount():
    menu_dict = {"Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00}
    x = 0
    total_price = 0.00
    while x == 0:
        try:
            user_input = input("Item: ").lower()
            for menu_op in menu_dict:
                if menu_op == user_input.title():
                    item_price = menu_dict[user_input.title()]
                    total_price = total_price + item_price
                    # print("Total: $",total_price, sep="")
                    # print("Total: $"+ str(round(total_price, 3)))
                    print("Total: ${:.2f}".format(total_price))

        except EOFError:
            print("")
            break


    return

main()
