import numpy as np

'''
Часть 1 - Итераторы
Задача 1
Создайте класс EvenIterator, который возвращает чётные
числа от 2 до n.
Пример:
for x in EvenIterator(10):
    print(x)
Вывод:
2
4
6
8
10
Подсказка:
Нужно реализовать методы
__iter__()
__next__()
'''
print("ЗАДАЧА 1")

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


for x in EvenIterator(10):
    print(x)






'''
Задача 2
Создайте класс ReverseList, который итерируется по списку 
с конца.
Пример:
data = [10, 20, 30]
for x in ReverseList(data):
    print(x)
Вывод:
30
20
10
Часть 2 - NumPy
Импортируйте библиотеку:
import numpy as np
'''
print("ЗАДАЧА 2")

class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.data[self.index]
        self.index -= 1
        return result


data = [10, 20, 30]
for x in ReverseList(data):
    print(x)





'''
Задача 3
Дан массив:
arr = np.array([3, 7, 1, 9, 4])
Найдите:
максимальный элемент
среднее значение массива
'''
print("ЗАДАЧА 3")


arr = np.array([3, 7, 1, 9, 4])

max_elemnt = np.max(arr)
print("максимальный элемент: ", max_elemnt)

mid_value = np.mean(arr)
print("среднее значение массива: ", mid_value)






'''
Задача 4
Дан массив:
arr = np.array([2, 8, 4, 10, 3])
Получите все элементы больше 5.
'''
print("ЗАДАЧА 4")

arr = np.array([2, 8, 4, 10, 3])

arr_more_5 = arr[arr > 5]
print("все элементы больше 5: ", arr_more_5)





'''
Задача 5
Даны два массива:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
Найдите сумму массивов.
Ожидаемый результат:
[5 7 9]
'''
print("ЗАДАЧА 5")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

arr_sum = a + b
print("сумма массивов: ", arr_sum)





'''
Задача 6
Дан массив:
arr = np.array([1, 2, 3, 4])
Создайте новый массив, где каждый элемент умножен на 3.
'''
print("ЗАДАЧА 6")
arr = np.array([1, 2, 3, 4])

arr_mult_3 = arr * 3
# ИЛИ
arr_mult_3 = np.multiply(arr, 3)
print("новый массив, где каждый элемент умножен на 3: ", arr_mult_3)


