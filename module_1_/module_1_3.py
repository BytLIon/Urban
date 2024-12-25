#Практическая работа по уроку "Динамическая типизация"
def program_5():
    name, age,  is_student = "Lelysh", 25, True
    print("Name:", name)
    print("Age:", age)
    age += int(input())
    print("Age:", age)
    print("Is Student:", is_student)


#Практическое задание по теме "Переменные".
def program_6():
    number_completed_hw = 12
    number_hours_spent = 1.5
    course_name = "Python"
    print(f"Курс: {course_name}, всего задач:{number_completed_hw}, затрачено часов: {number_hours_spent}, среднее время выполнения {number_completed_hw / number_hours_spent} часа.")


#Практическое задание по уроку "Строки и индексация строк"
def program_7():
    example = input()
    print(example[0])
    print(example[-1])
    print(example[len(example) // 2:])
    print(example[::-1])
    print(example[1::2])



if __name__ == '__main__':
    program_5()
    program_6()
    program_7()