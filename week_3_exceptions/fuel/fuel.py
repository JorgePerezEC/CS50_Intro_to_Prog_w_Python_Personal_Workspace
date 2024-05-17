def main():
    x = get_fraction()
    if 1 >= x >= 0.99:
        print("F")
    elif 0 <= x <= 0.01:
        print("E")
    else:
        print(f"{int(x*100)}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x_formated = int(x)
            y_formated = int(y)
            if round(x_formated/y_formated,2) > 1:
                pass
            else:
                return round(x_formated/y_formated,2)
        except ValueError:
            # print("x is not an integer")
            pass
        except ZeroDivisionError:
            pass


main()
