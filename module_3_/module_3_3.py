#"Распаковка позиционных параметров"
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



if __name__ == '__main__':
    values_dict = {"a": {1,}, "b": [1, ], "c": (1,)}
    values_list = [1, "1", True]
    values_list_2 = [{1,}, True]


    print_params()
    print_params(b=25)
    print_params(c=[1, 2, 3])

    print_params(*values_list)
    print_params(**values_dict)

    print_params(*values_list_2, 42)
