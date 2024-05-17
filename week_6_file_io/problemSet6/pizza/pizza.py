import sys
import csv
from tabulate import tabulate

while True:
    try:
        if len(sys.argv) == 2:
            name, ext = sys.argv[1].split('.')
            if ext != 'csv':
                sys.exit("Not a CSV file")
            else:
                pizza_menu = []
                f = open(sys.argv[1])
                with f as file:
                    reader = csv.reader(file)
                    for row in reader:
                        pizza_menu.append(row)
                print(tabulate(pizza_menu, headers="firstrow", tablefmt="grid"))
                sys.exit()
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except ValueError:
        sys.exit("Not a CSV file")

