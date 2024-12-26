#"Генераторные сборки"


if __name__ == '__main__':

    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    first_result = [len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b)]
    print(first_result)

    second_result = [True if len(first[i]) == len(second[i]) else False for i in range(len(first))]
    print(second_result)
