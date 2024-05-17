import csv

name = input("Whjat's your name?")
home = input("Whjat's your home?")

with open('students.csv', "a") as file:
    # writer =csv.writer(file)
    # writer.writerow(
    #     [name,home]
    # )
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
