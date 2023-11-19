import os
import sys
from decimal import Decimal


class CheckingError(Exception):
    pass


def checking_values(*args):
    """Проверка данных"""
    for elem in args:
        if elem.strip() == '':
            raise CheckingError('Есть незаполненные поля')
        try:
            float(elem)
        except ValueError:
            raise CheckingError(f'Вы ввели некорректные данные: "{elem}"')


def check_units_measure_length(length: str, check: bool) -> Decimal:
    """Проверка единиц измерения формы, перевод в десятичное число"""
    length = Decimal(length)
    if check:
        length = length / 1000
    return length


def round_the_number(number: Decimal, rounding: str) -> Decimal:
    """Округляет число"""
    return number.quantize(Decimal(rounding))


def resource_path(relative_path):
    """Получить абсолютный путь к картинке, для Pyinstaller"""
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("../data/images/")

    return os.path.join(base_path, relative_path)
