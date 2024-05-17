def main():
    count_inputs()

def count_inputs():
    grocery_lst = {}
    while True:
        try:
            item_user = input().strip().lower()

            # for item_user in grocery_lst:
            if item_user in grocery_lst:
                grocery_lst[item_user] += 1
            else:
                grocery_lst[item_user] = 1

            # print(grocery_lst)

        except EOFError:
            sorted_dict = dict(sorted(grocery_lst.items()))
            for item in sorted_dict:
                print(str(sorted_dict[item]) + " " + item.upper())
            break

main()
