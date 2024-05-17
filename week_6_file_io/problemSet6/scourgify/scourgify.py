import sys
import csv

while True:
    try:
        if len(sys.argv) == 3:
            name, ext = sys.argv[1].split('.')
            name2, ext2 = sys.argv[2].split('.')
            if ext != 'csv' or ext2 != 'csv':
                sys.exit("Not a CSV file")
            else:
                # new_csv = []
                # f = open(sys.argv[1])
                # with f as file:
                #     reader = csv.reader(file)
                #     for row in reader:
                #         new_csv.append(row)
                # fix_csv = [['first','last','house']]

                # for row in new_csv[1:]:
                #     f, l = row[0].split(',')
                #     fix_csv.append([f.strip(),l.strip(),row[1]])
                # with open(sys.argv[2], "w") as file:
                #     for row in fix_csv:
                #         line = str(row).replace("[","")
                #         line = line.replace("]","")
                #         line = line.replace("'","")
                #         line = line.strip()
                #         file.write(f"{line}\n")
                listofdict = []
                f = open(sys.argv[1])
                with f as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        x, y = row["name"].split(', ')
                        listofdict.append({"first": y, "last": x, "house": row["house"]})
                with open(sys.argv[2], "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for i in range(len(listofdict)):
                        writer.writerow({"first": listofdict[i]["first"], "last": listofdict[i]["last"], "house": listofdict[i]["house"]})
                sys.exit()

        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])
    except ValueError:
        sys.exit("Not a CSV file")

