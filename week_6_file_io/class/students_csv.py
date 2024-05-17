import csv

students = []

with open("students.csv") as file:
    reader  = csv.reader(file)
    dic_reader = csv.DictReader(file)
    for row in reader:
          students.append({"name": row["name"], "home": row["home"]})
    # Version 1
    # for name, home in reader:
    #     students.append({"name": name, "home": home})
        # Version 2
    # for row in reader:
    #     students.append({"name": row[0], "home": row[1]})
# print(students)
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is in {student['house']}")
