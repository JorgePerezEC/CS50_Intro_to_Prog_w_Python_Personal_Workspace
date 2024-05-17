def main():
    user_input = input("Fraction: ")
    # x = get_fraction()
    value = convert(user_input)
    # print("F:",value)
    letter = gauge(value)
    print(letter)

def gauge(percentage):
    if 1 >= percentage >= 0.99:
        return "F"
    elif 0 <= percentage <= 0.01:
        return "E"
    else:
        return f"{int(percentage*100)}%"

# def convert(fraction):
#     x, y = fraction.split('/')
def convert(fraction):
    while True:
        # try:
        #     x, y = fraction.split('/')
        #     x_formated = int(x)
        #     y_formated = int(y)
        #     if round(x_formated/y_formated,2) > 1:
        #         pass
        #     else:
        #         return round(x_formated/y_formated,2)
        # except ValueError:
        #     # print("x is not an integer")
        #     pass
        # except ZeroDivisionError:
        #     pass
        # while True:

        try:
            x, y = fraction.split('/')
            x_formated = int(x)
            y_formated = int(y)
            result = round(x_formated / y_formated, 2)
            if result > 1:
                fraction = input("Fraction: ")
                pass
            else:
                return result
            # print(result)
            # if 0 <= result <= 1:
            #     return result

        except ValueError:
            # print("x is not an integer")
            fraction = input("Fraction: ")
            pass
        except ZeroDivisionError:
            fraction = input("Fraction: ")
            pass


if __name__ == "__main__":
    main()
