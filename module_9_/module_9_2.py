#"Списковые, словарные сборки"


if __name__ == '__main__':

    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    first_result = [len(i) for i in first_strings if len(i) >= 5]
    print(first_result)

    second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
    print(second_result)

    third_strings = first_strings + second_strings
    third_result = {i:len(i) for i in third_strings if not len(i) % 2}
    print(third_result)