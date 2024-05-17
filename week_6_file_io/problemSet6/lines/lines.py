import sys

while True:
    try:
        if len(sys.argv) == 2:
            name, ext = sys.argv[1].split('.')
            if ext != 'py':
                sys.exit("Not a Python file")
            else:
                lines = 0
                with open(sys.argv[1], "r") as file:
                    for line in file:
                        # print(line)
                        # print(line.strip())
                        # print(len(line.strip()))
                        line = line.strip()
                        if line.startswith("#"):
                            lines += 0
                        elif len(line) == 0:
                            lines += 0
                        else:
                            lines += 1
                            # print("hello,", line.rstrip())
                    print(lines)
                    sys.exit()
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except ValueError:
        sys.exit("Not a Python file")

