#"Перегрузка операторов"
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            print(*[i for i in range(1, new_floor + 1)], sep='\n')

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            return "Value Error"

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            return "Value Error"

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        else:
            return "Value Error"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return "Value Error"


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return "Value Error"


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return "Value Error"


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return "Value Error"


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return "Value Error"


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return "Value Error"






if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print("\n", 1)
    print(h1)
    print(h2)

    print("\n", 2)
    print(h1 == h2)  # __eq__

    print("\n", 3)
    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    print("\n", 4)
    h1 += 10  # __iadd__
    print(h1)

    print("\n", 5)
    h2 = 10 + h2  # __radd__
    print(h2)

    print("\n", 6)
    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__



