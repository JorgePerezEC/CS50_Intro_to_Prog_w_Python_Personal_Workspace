students = []

with open("students.csv") as file: #"r" is default
    dict_students = {}
    for line in file:
        name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")
        student = {"name": name, "house": house} #declare a dict in only one line
        # student["name"] = name
        # student["house"] = house
        students.append(student)

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is in {student['house']}")

# def get_name(student):
#     # print(student)
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_name, reverse=False):
#     print(f"{student['name']} is in {student['house']}")

