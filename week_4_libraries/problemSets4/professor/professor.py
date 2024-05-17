import random

def main():
    lvl = get_level()
    generate_integer(lvl)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                continue
        except ValueError:
            pass

def generate_integer(level):
    op = 0
    count_err = 0
    count_ex = 0
    while op < 10:
        try:
            if level == 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            elif level == 2:
                x = random.randint(10, 99)
                y = random.randint(10, 99)
            elif level == 3:
                x = random.randint(100, 999)
                y = random.randint(100, 999)
            sum = x + y
            # sum_user = int(input(f"{x} + {y} = "))
            while count_err < 3:
                sum_user = int(input(f"{x} + {y} = "))
                if sum_user != sum:
                    print("EEE")
                    count_err += 1
                else:
                    count_ex += 1
                    break
            if count_err == 3:
                print(f"{x} + {y} = {sum}")
            op += 1
            count_err = 0
            continue

        except ValueError:
            pass
    print("Score: " + str(count_ex) )

if __name__ == "__main__":
    main()
