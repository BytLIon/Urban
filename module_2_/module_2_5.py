def program_16(n, m, value):
    return [[value,] * m] * n


#"Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix



if __name__ == '__main__':
    a, b, c = int(input("Строк: ")), int(input("Столбцов:")), int(input("Значение: "))
    my_matrix = get_matrix(a, b, c)
    print(my_matrix)
