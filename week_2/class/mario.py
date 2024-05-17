def main():
    print_square2(3)

def print_square(size):
    for i in range(size):
        print("#"*size)

def print_square2(size):
    for i in range(size):
        for j in range(size):
            # "Print brick
            print("#", end = "")

        print()

main()

