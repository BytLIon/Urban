#"Создание исключений"
class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = int(__vin)
        self.__numbers = str(__numbers)
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)


    def __is_valid_vin(self, __vin):
        if isinstance(self.__vin, int):
            if self.__vin >= 1000000 and self.__vin <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')


    def __is_valid_numbers(self, numbers):
        if isinstance(self.__numbers, str):
            if len(self.__numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                return True
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')










