import inflect

def main():
    p = inflect.engine()
    lst_names = []
    while True:
        try:
            # print(lst_names)
            name = input("Name: ")
            if name != "":
                lst_names.append(name)
            else:
                continue
        except EOFError:
            print("\nAdieu, adieu, to", p.join(lst_names))
            break
main()




# JOIN WORDS INTO A LIST:

# mylist = p.join(("apple", "banana", "carrot"))
# # "apple, banana, and carrot"

# mylist = p.join(("apple", "banana"))
# # "apple and banana"

# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# # "apple, banana and carrot"
