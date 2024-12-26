class Human:
    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f"Hi, my name is {self.name}, my age is {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Age {self.name} is {self.age}")

    def __str__(self):
        return f"My name is {self.name}"

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __bool__(self):
        return bool(self.age)

    def __del__(self):
        print(f"{self.name} go to end")



class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print("I am new")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print("I am init")
        self.args = args
        for key, val in kwargs.items():
            setattr(self, key, val)



class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)



if __name__ == '__main__':
    #ex = Example('data', second=25, third=3.14)
    other = [1, 2, 3]
    user = {"name": "Den", "age": 25}

    user1 = User(*other, **user)
    user2 = User()
    print(user1)

    print(user1 is user2)
    print(id(user1), id(user2))


    #den_ = Human("Denis", 23)
    #max_ = Human("Max", 21)

    #print(den_.name, den_.age)
    #print(max_.name, max_.age)

    #max_.birthday()

