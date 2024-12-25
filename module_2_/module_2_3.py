"""
def program_14():
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    i = 0
    len_list = len(my_list)

    while i <= len_list and my_list[i] >= 0:
        if my_list[i] > 0:
            print(my_list[i])
        i += 1
"""
#"Стиль кода. Цикл While. 1.2"
def program_14():
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    i = 0
    len_list = len(my_list)

    while i <= len_list:
        if my_list[i] < 0:
            break
        elif my_list[i] == 0:
            i += 1
            continue
        else:
            print(my_list[i])
            i += 1



if __name__ == '__main__':
    program_14()