#"Система регистрации на классах"
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователь с атрибутами: логинб пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Выберите действие: \n1 - Вход\n2 - Регистрация\n")

        if choice == 1:
            login = input("Login: ")
            password = input("Password: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Go to Ok {login}")
                    break
                else:
                    print(f"Go to lose {login}")
            else:
                print("User lose")

        if choice == 2:
            user = User(input("Login: "), password := input("Password: "), password2 := input("Password: "))
            if password != password2:
                print("Password is not equals")
                continue
            database.add_user(user.username, user.password)
        print(database.data)


