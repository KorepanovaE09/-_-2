import pytest
from my_lib import Fibonnachi, bubble_sort, calculate

def test_fibonnachi():
    assert Fibonnachi(0) == [0]  # Проверка для N = 0
    assert Fibonnachi(1) == [0, 1]  # Проверка для N = 1
    assert Fibonnachi(5) == [0, 1, 1, 2, 3]  # Проверка для N = 5

def test_fibonnachi_negative_N():
    with pytest.raises(ValueError):
        Fibonnachi(-1)  # Проверка, что функция вызывает ValueError при отрицательном N

# Тесты для функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([4, 2, 1, 3]) == [1, 2, 3, 4]  # Проверка на сортировку списка
    assert bubble_sort([]) == []  # Проверка на пустой список
    assert bubble_sort([1, 1, 1, 1]) == [1, 1, 1, 1]  # Проверка на список с одинаковыми элементами
    assert bubble_sort([-4, 7, 1, 0, -2]) == [-4, -2, 0, 1, 7]  # Проверка на сортировку отрицательных чисел

# Тесты для функции calculate
def test_calculate_addition():
    assert calculate(2, 3, "+") == 5  # Проверка операции сложения
    assert calculate(0, 0, "+") == 0  # Проверка сложения нулевых значений

def test_calculate_subtraction():
    assert calculate(7, 2, "-") == 5  # Проверка операции вычитания
    assert calculate(0, 0, "-") == 0  # Проверка вычитания нулевых значений

def test_calculate_multiplication():
    assert calculate(4, 2, "*") == 8  # Проверка операции умножения
    assert calculate(0, 5, "*") == 0  # Проверка умножения на ноль

def test_calculate_division():
    assert calculate(10, 2, "/") == 5  # Проверка операции деления
    assert calculate(4, 5, "/") == 0.8 # Проверка деления меньшего на большее

def test_calculate_division_negative():
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, "/") == float("inf")  # Проверка деления на ноль