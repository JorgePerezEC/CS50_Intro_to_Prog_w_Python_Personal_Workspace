class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def deposit(self, extra_cookies):
        if self.size + extra_cookies > self.capacity:
            raise ValueError("Insuficient Jar capacity")
        self.size = self.size + extra_cookies

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Insuficient cookies")
        self.size = self.size - n

    def __str__(self):
        return f"{'🍪' * self.size}"

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError("Empty value of capacity")
        if not isinstance(int(capacity), int):
            raise ValueError("Capacity only could be a int")
        if int(capacity) < 0:
            raise ValueError("Capacity cannot be a negative number")
        self._capacity = int(capacity)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

def main():
    try:
        jar = Jar((input("Jar capacity: ")))
        jar.deposit(20)
        print(jar)
        jar.withdraw(10)
        print(jar)
        print("*************")
        jar2 = Jar()
        print(jar2)

    except ValueError as ex:
        print(ex)


if __name__ == "__main__":
    main()

