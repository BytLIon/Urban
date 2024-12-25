#Практическое задание по теме: "Словари и множества"
def program_10():
    my_dict = {"Maria": 1975, "Andrey": 1972, "Alexandra": -356, "Alexey": 1988, "Bair": 1977,
"Alexander": 1777, "Danek": 1937, "Ifrat": 1974, "Ekaterina": 1729, "Anton": 1991,}
    print("Словарь:", my_dict)
    print("Existing value:", my_dict["Maria"])
    print("Not existing value:", my_dict.get("Lion"))
    my_dict["Dens"], my_dict["Leon"] = 1966, 1977
    value = my_dict.pop("Maria")
    print("Deleted value:", value)
    print("Modified dictionary:", my_dict)



    my_set = {1, 1.0, "1", '1', 'one', "one", (1, )}
    print("Set:", my_set)
    my_set.add(('one',))
    my_set.add(('1.0',))
    my_set.discard(1.0)
    print("Modified set:", my_set)


#Дополнительное практическое задание по модулю: "Базовые структуры данных."
def program_11():
    grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
    students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
    grades = [sum(i) / len(i) for i in grades]
    students = sorted(students)
    dict_students = {i: j for i, j in zip(students, grades)}
    print(dict_students)



if __name__ == '__main__':
    program_10()
    program_11()