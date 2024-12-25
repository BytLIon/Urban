#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
def program_9():
    immutable_var = ('Проблема', 0, 1.5, [0, 1, 2], {0, 1, 2}, {0: "Проблема", 1: "Задача", 2: "Путь"}, (0, 1, 2), )
    mutable_list = ['Проблема', 0, 1.5, [0, 1, 2], {0, 1, 2}, {0: "Проблема", 1: "Задача", 2: "Путь"}, (0, 1, 2), ]

    print(immutable_var)
    #immutable_var[1] = 1

    print(mutable_list)
    mutable_list[1] = 1
    print(mutable_list)



if __name__ == '__main__':
    program_9()