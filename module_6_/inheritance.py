#"Наследование классов"
class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print("Hello")

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    def about(self):
        print("I am student")

class Teacher(Human):
    pass



if __name__ == '__main__':
    human = Human()
    human.about()






