import math
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    #  Сформируйте нужную строку
    output = f'Привет, {name}! Тебе {age} лет.'
    print(output)

    #  Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    #  Сосчитайте периметр
    perimeter = 2 * (a + b)
    assert perimeter == 60

    #  Сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    #  Сосчитайте площадь
    area = math.pi * r ** 2
    assert area == 1661.9025137490005

    # Cосчитайте длину окружности
    length = 2 * math.pi * r
    assert length == 144.51326206513048
    print(f'Length: {length}')
    print(f'Area: {area}')


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # Создайте список
    list1 = random.sample(range(1, 100), 10)
    list1.sort()
    assert len(list1) == 10
    assert list1[0] < list1[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    list2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    #  Удалите повторяющиеся элементы
    list2 = list(set(list2))

    assert isinstance(list2, list)
    assert len(list2) == 10
    assert list2 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    #  Создайте словарь
    dict1 = dict(zip(first, second))
    print(dict1.values())

    assert isinstance(dict1, dict)
    assert len(dict1) == 5
