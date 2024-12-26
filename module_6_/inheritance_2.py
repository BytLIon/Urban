#"Наследование классов"
class Human:
    def __init__(self, name, group):
        super().__init__(group)
        self.name = name
        super().about()

    def info(self):
        print(f"Hi, I am {self.name}")


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f"{self.name} in group {self.group}")

class  Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()



if __name__ == '__main__':
    student = Student("Max", "MGU", "Python")







