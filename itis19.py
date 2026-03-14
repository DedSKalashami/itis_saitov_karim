from functools import reduce

numbers = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30, 11, 6]


# 1) Напишите генератор greater_than_ten(numbers), который возвращает только числа больше 10.
def greater_than_ten(numbers):
    for num in numbers:
        if num > 10:
            yield num


# 2) Напишите генератор square_numbers(numbers), который возвращает квадраты чисел.
def square_numbers(numbers):
    for num in numbers:
        yield num ** 2


# 3) С помощью filter оставьте только чётные квадраты чисел.
even_squared = filter(lambda x: x % 2 == 0, square_numbers(greater_than_ten(numbers)))


# 4) Используя map, преобразуйте числа: число → строка вида "value=ЧИСЛО"
string_form = map(lambda x: f"value={x}", even_squared)

print(list(string_form))


# 5a) Используя reduce, найдите: сумму всех чисел списка
sum_numbers = reduce(lambda a, x: a + x, numbers)
print(sum_numbers)

# 5b) Используя reduce, найдите: максимальное число списка
max_number = reduce(lambda a, x: x if x > a else a, numbers)
print(max_number)


# 6) Напишите генератор multiples_of_three(n), который возвращает первые n чисел, кратных 3.
def multiples_of_three(n):
    count = 0
    for num in numbers:
        if num % 3 == 0:
            yield num
            count += 1
            if count == n:
                break

print("первые n(n=5) чисел, кратных 3", list(multiples_of_three(5)))


# 7) Напишите генератор word_generator(text), который возвращает слова строки по одному.
def word_generator(text):
    for word in text.split():
        yield word
text = "рфви а шотфвй кдд шойфвт йшвшщйьм йцтщ, ndandijnq"

print("слова строки по одному:")
for word in word_generator(text):
    print(word)

# 8) Используя map и filter, обработайте текст в следующей последовательности:
# a) оставить слова длиной > 4
# b) преобразовать в верхний регистр

words = word_generator(text)
filtered_words = filter(lambda word: len(word) > 4, words)
upper_filtered_words = map(lambda word: word.upper(), filtered_words)

print("a) cлова длиной > 4   b) в верхний регистр:", list(upper_filtered_words))

# я типа не прохоров но ок
# Напишите генератор fibonacci, который возвращает первые n чисел последовательности.

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(20)))
