# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]

#How to asign every house to his respective student

students = {
    "Hermione" : "Griffindor",
    "Harry" : "Griffindor",
    "Ron" : "Griffindor",
    "Draco" : "Slytherin",
}

# print(students)

# for student in students:
#     print(student , students[student], sep=": ")

students_lst = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students_lst:
    print(student["name"])
