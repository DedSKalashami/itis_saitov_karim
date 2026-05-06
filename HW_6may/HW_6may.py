
# Часть 1 - Threading
# Задание
# Нужно создать функцию обработки “заказа”.
# Логика функции:
# Функция должна:
# принимать order_id
# имитировать ожидание (пауза 1-2 секунды)
# выполнять небольшую CPU-нагрузку:
# пройтись по диапазону чисел (примерно 100k–500k)
# выполнить простые математические операции (например квадрат, остаток, суммирование)
# вывести результат обработки заказа
# Что реализовать:
# синхронное выполнение 5 заказов
# выполнение 5 заказов через threading
# замер времени

import asyncio
import threading
import time
from multiprocessing import Pool, Process


def processing_order(order_id): # принимать order_id
    print(f"Thread {order_id} started")
    time.sleep(1) # имитировать ожидание (пауза 1-2 секунды)
    for i in range(200_000):
        a = ((i**2) + 10) % 7 # выполнять небольшую CPU-нагрузку:
    return f"Thread {order_id} finished" # вывести результат обработки заказа



def run_threading():
    print("синхронное выполнение 5 заказов:")
    time_start = time.time()
    processes = [processing_order(i) for i in range(1,6)] # без Threading
    time_end = time.time()
    print(time_end - time_start) # вывести результат обработки заказа

    print()

    print("выполнение 5 заказов через threading:")
    time_start = time.time()
    # типо так???
    t1 = threading.Thread(target = processing_order, args=(1,))
    t2 = threading.Thread(target = processing_order, args=(2,))
    t3 = threading.Thread(target = processing_order, args=(3,))
    t4 = threading.Thread(target = processing_order, args=(4,))
    t5 = threading.Thread(target = processing_order, args=(5,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    time_end = time.time()
    print(time_end - time_start)

    print()
    print()
    print()
    print()
    print()



# Часть 2 - Multiprocessing
# Задание
# Создать функцию “тяжёлых вычислений”.
# Логика функции:
# Функция должна:
# принимать число n
# выполнять большой цикл (миллионы итераций)
# в цикле выполнять математические операции:
# умножение
# остаток от деления
# возведение в степень (простое)
# возвращать итоговый результат
# Что реализовать:
# запуск последовательно
# запуск через multiprocessing Pool (несколько процессов)

# Создать функцию “тяжёлых вычислений”.
def hard_compute(n): # принимать число n
    a = 0
    for i in range(1, 9999): # выполнять большой цикл (миллионы итераций)
        for j in range(1, 9999): # в цикле выполнять математические операции:
            a += i * j # умножение
            a += i % a # остаток от деления
            a += j ** 3 # возведение в степень (простое)
    return a # возвращать итоговый результат


def run_multiprocessing():
    print("я не понимаю почему последовательно занимает меньше времени")
    print("запуск последовательно:")

    time_start = time.time()
    hard_compute(1)
    hard_computation(2)
    hard_computation(3)
    hard_computation(4)
    time_end = time.time()
    print(time_end - time_start)

    print()

    print("запуск через multiprocessing Pool:")

    time_start = time.time()
    with Pool() as p:
        result = p.map(hard_compute, range(1, 6))

    print(result)

    time_end = time.time()
    print(time_end - time_start)

    print()
    print()
    print()

def hard_computation(n):
    a = 0
    for i in range(1, 1_000_001):
        a += n * i
        a += n % i
        a += i**2
    return a


def test_processing():
    print("БЕЗ pool:")
    time_start = time.time()

    hard_compute(1)
    hard_compute(2)
    hard_compute(3)
    hard_compute(4)
    hard_compute(5)

    time_end = time.time()
    print(time_end - time_start)
    print()

    print("С pool:")
    time_start = time.time()

    with Pool() as p:
        result = p.map(hard_computation, range(1, 6))

    print(result)

    time_end = time.time()
    print(time_end - time_start)






# Часть 3 - Async
# Задание
# Создать асинхронную функцию “запроса к сервису”.
# Логика функции:
# функция async
# принимает user_id
# делает “ожидание ответа” (async sleep 1-2 секунды)
# после ожидания выполняет вычисления:
# пройтись по диапазону чисел (средний размер, ~300k–700k)
# посчитать простую агрегирующую функцию (сумма / остаток / фильтрация)
# вернуть результат
# Что реализовать:
# 10 асинхронных задач
# запуск через asyncio.gather
# замер времени

async def processing(user_id):
    await asyncio.sleep(2) # делает “ожидание ответа” (async sleep 1-2 секунды)
    a = 0
    for i in range(500_000):# пройтись по диапазону чисел (средний размер, ~300k–700k)
        a += i + (a % 7) # посчитать простую агрегирующую функцию (сумма / остаток / фильтрация)
    return a


async def run_async_processing():
    time_start = time.time()
    print("async:")

    # 10 асинхронных задач
    processes = await asyncio.gather(
        processing(1),
        processing(2),
        processing(3),
        processing(4),
        processing(5),
        processing(6),
        processing(7),
        processing(8),
        processing(9),
        processing(10),
    )

    time_end = time.time()
    print(time_end - time_start)

    print()
    print()
    print()




# Часть 4 - Смешанный сценарий
# (сравнение всех подходов)
# Задание
# Создать одну функцию “универсальной задачи”.
# Логика функции:
# принимает task_id
# выполняет:
# ожидание (1 секунда)
# CPU-часть (цикл со сложением / математикой)
# ещё одно ожидание (1 секунда)
# финальная обработка результата
# Что реализовать:
# Эту функцию запустить 5 раз в 3 режимах:
# последовательно (sync)
# threading
# multiprocessing




def universal_task(task_id):
    time.sleep(1)

    for i in range(400_000):
        a = i**2

    time.sleep(1)
    return f"Thread {task_id} finished"


def universal_processing():
    time_start = time.time()

    print("последовательно (sync): ")
    universal_task(1)
    universal_task(2)
    universal_task(3)
    universal_task(4)
    universal_task(5)

    time_end = time.time()
    print(time_end - time_start)
    print()

    print("Threading: ")
    time_start = time.time()

    t1 = threading.Thread(target=universal_task, args=(1,))
    t2 = threading.Thread(target=universal_task, args=(2,))
    t3 = threading.Thread(target=universal_task, args=(3,))
    t4 = threading.Thread(target=universal_task, args=(4,))
    t5 = threading.Thread(target=universal_task, args=(5,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    time_end = time.time()
    print(time_end - time_start)
    print()

    print("multiprocessing: ")

    time_start = time.time()

    p1 = Process(target = universal_task, args = (1,))
    p2 = Process(target = universal_task, args = (2,))
    p3 = Process(target = universal_task, args = (3,))
    p4 = Process(target = universal_task, args = (4,))
    p5 = Process(target = universal_task, args = (5,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    time_end = time.time()
    print(time_end - time_start)
    print()


if __name__ == "__main__":
    print("Часть 1 - Threading")
    run_threading()
    print("Часть 2 - Multiprocessing ")
    run_multiprocessing()
    print("Часть 3 - Async")
    asyncio.run(run_async_processing())
    print("Часть 4 - Смешанный сценарий ")
    universal_processing()
