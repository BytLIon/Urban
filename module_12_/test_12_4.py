#Логирование
import logging
import unittest
from runner import Runner  # Импортируем класс Runner из runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Тестовый Бегун", -5)  # передаем отрицательное значение
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  # передаем неверный тип
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()