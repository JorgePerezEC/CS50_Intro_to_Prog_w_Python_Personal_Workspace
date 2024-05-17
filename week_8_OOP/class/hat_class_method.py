import random

class Hat:
    def __init__(self):
        self.houses = ["Griffyndor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):#Instance method

        print(name, "is in", random.choice(self.houses))

class Hat_class_method:

    #Class local variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod #Class method
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

hat = Hat()
hat.sort("Harry")

Hat_class_method.sort("Harry")
