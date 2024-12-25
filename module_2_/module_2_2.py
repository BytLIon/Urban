#"Условная конструкция. Операторы if, elif, else"
def program_13():
    first, second, third = int(input("Enter the first number ")), int(input("Enter the second number ")), int(input("Enter the third number "))
    if first == second == third:
        print("The number of identical numbers is equal to", 3)
    elif first != second != third != first:
        print("The number of identical numbers is equal to", 0)
    else:
        print("The number of identical numbers is equal to", 2)



if __name__ == '__main__':
    program_13()