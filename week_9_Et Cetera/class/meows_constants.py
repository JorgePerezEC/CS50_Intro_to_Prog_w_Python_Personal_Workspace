MEOWS = 3

MEOWS = 4 # In python we can change constants values

for _ in range(MEOWS):
    print("meow")

class Cat:
    MEOWS = 2

    def meow(self):
        for _ in range(MEOWS):
            print("Meow")


cat = Cat()
cat.meow()
