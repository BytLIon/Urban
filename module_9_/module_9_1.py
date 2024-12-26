#"Введение в функциональное программирование"
def apply_all_func(int_list, *functions):

    results = dict()

    for fun in functions:
        res = fun(int_list)
        results[fun.__name__] = res

    return results



if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))









