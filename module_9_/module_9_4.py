#"Создание функций на лету"
from random import choice as random



class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random(self.words)



def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


if __name__ == '__main__':
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    print(list(map(lambda x, y: x == y, first, second)))


    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Странно')
    print(first_ball())
    print(first_ball())
    print(first_ball())