# Задание: «Меню кафе»
# Программа должна помочь владельцу кафе управлять меню и заказами.
# Все действия оформляются как отдельные функции, где обязательно хотя бы в половине случаев используются lambda и встроенные функции.
# Требования
# Сохранить меню в виде словаря:

menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}
# coffee, tea, sandwich, cake, juice


# Вывести всё меню, отсортированное:
# по названию блюда (алфавит)
# по цене (от дешёвого к дорогому)
# Использовать sorted + lambda.

def show_menu():


    list_menu = list(menu.items())

    # меню, отсортированное по алфавиту
    print("Меню, отсортированное по алфавиту:")
    alphabet_sorted_menu = sorted(list_menu, key=lambda x: x[0])
    for dish, price in alphabet_sorted_menu:
        print(f"{dish} : {price}")

    print("-" * 30)

    # меню, отсортированное по цене
    print("Меню, отсортированное по цене:")
    price_sorted_menu = sorted(list_menu, key=lambda x: x[1])
    for dish, price in price_sorted_menu:
        print(f"{dish} : {price}")

    print("=" * 30)
    input("Нажмите Enter, чтобы продолжить")



# Посчитать среднюю цену блюда в меню.
# Использовать sum, len и lambda (например, внутри map).

def average_price():


    list_menulist_menu = list(menu.items())
    list_price = list(map(lambda item: item[1], menu.items()))
    average_price = sum(list_price) / len(list_price)
    print(f"Средняя цена меню: {average_price}")

    print("=" * 30)
    input("Нажмите Enter, чтобы продолжить")



# Добавить новые блюда в меню через ввод от пользователя. Если блюдо уже есть, заменить цену.
# Использовать dict.update и lambda.


def menu_add():


    # название ввод
    new_dish = input("Введите название нового блюда на английском языке: ").lower()

    # цена ввод
    price_for_new_dish = ""
    while price_for_new_dish == "":
        try:
            price_for_new_dish = int(input("Введите цену нового блюда: "))
        except ValueError:
            print("Введите число!")
            price_for_new_dish = ""

    # добавление в меню
    menu_add = {new_dish: price_for_new_dish}
    menu.update(menu_add)
    print("Блюдо добавлено!")

    print("=" * 30)
    input("Нажмите Enter, чтобы продолжить")



# Удалить блюдо из меню (с проверкой, что оно существует).
# Использовать if … else в одну строку.

def menu_delete():


    name_del = input("Введите точное название блюда, которое вы хотите удалить: ").lower()
    # однострочники воняют 
    menu.pop(name_del) if name_del in menu else print("Блюдо не найдено!")
    print("Блюдо удалено!") if name_del in menu else None
    print("="*30)
    input("Нажмите Enter, чтобы продолжить")



# Показать все блюда дешевле определённой цены N.
# Использовать filter + lambda.

def menu_finder_by_price():

    list_menulist_menu = list(menu.items())
    N = int(input("Введите значение: "))
    
    list_dishes, list_prices = zip(*list_menulist_menu)
    list_prices = list(list_prices)

    list_found = list(filter(lambda x: x < N, list_prices))
    list_dishes = []

    print("Список блюд дешевле выбраного значения: ")
    for key, value in menu.items():
        if value in list_found:
            list_dishes.append((key,value))

    for dish, price in list_dishes:
        print(f"{dish} : {price}")

    print("="*30)
    input("Нажмите Enter, чтобы продолжить")



# Найти самое дешёвое и самое дорогое блюдо.
# Использовать min и max с lambda.

def max_min_menu_position():


    list_menu = list(menu.items())
    cheapest_dish = max(list_menu, key=lambda x: x[1])
    mostExpensive_dish = min(list_menu, key=lambda x: x[1])
    
    print(f"Самое дорогое блюдо {mostExpensive_dish[0]} : {mostExpensive_dish[1]}")
    print(f"Самое дешевое блюдо {cheapest_dish[0]} : {cheapest_dish[1]}")

    print("=" * 30)
    input("Нажмите Enter, чтобы продолжить")


# Сделать список только напитков (coffee, tea, juice) и отсортировать их по цене.
# Использовать filter + sorted + lambda.

def menu_drinks():


    list_of_all_drinks = ['water', 'coffee', 'tea', 'juice', 'soda', 'milkshake', 'lemonade', 'hot chocolate',
                    'beer', 'wine', 'smoothie', 'cocktail', 'iced tea', 'iced coffee' 'cider', 'sparkling water', 'energy drink']
    list_of_drinks = list(filter(lambda x: x[0] in list_of_all_drinks, [x for x in list(sorted(menu.items(), key=lambda x: x[1]))]))

    print("Список напитков:")
    for dish, price in list_of_drinks:
        print(f"{dish} : {price}")


    print("=" * 30)
    input("Нажмите Enter, чтобы продолжить")


#   Сформировать заказ: 

# Сформировать заказ:
from functools import reduce

def order():


# пользователь вводит список блюд через запятую.
    order_input = input("Введите блюда через запятую: ").strip()
    

# Если заказ пустой — вывести: «Вы ничего не выбрали».
    if not order_input:
        print("Вы ничего не выбрали!")
        return
    

# Убрать пробелы и тд
    dishes = list(map(lambda x: x.strip().lower(), order_input.split(',')))


# Проверить, есть ли блюда в меню
    order = dict(map(lambda dish: (dish, menu[dish]), 
                    filter(lambda dish: dish in menu, dishes)))
    
    invalid_dishes = list(filter(lambda dish: dish not in menu, dishes))
    if invalid_dishes:
        print(f"Следующие блюда не найдены в меню: {', '.join(invalid_dishes)}")
    
# Проверка плохого заказа
    if not order:
        print("Нет блюд из меню в заказе!")
        return
    
# Показать заказ в красивом виде:
# Ваш заказ:
# 1. Coffee — 120 руб.
# 2. Cake — 150 руб.
# Итого: 270 руб.
# Использовать enumerate + lambda.
    print("======= ВАШ ЗАКАЗ ========")
    list(map(lambda item: print(f"{item[0]+1}. {item[1][0].capitalize()} — {item[1][1]} руб."), 
             enumerate(order.items())))
    
# Посчитать общую стоимость заказа.
# Использовать reduce + lambda.
    total = reduce(lambda x, y: x + y, 
                  map(lambda item: item[1], order.items())) if order else 0
    print("-"*30)
    print(f"Итого: {total} руб.")
    
# Проверить заказ:
# Если сумма больше 500, вывести: «Поздравляем, у вас скидка 10%!».
    (lambda total: 
        print("Поздравляем, у вас скидка 10%!", "\n", f"Итого со скидкой: {total * 0.9} руб.")
        if total > 500 else None)(total)
    

    print("="*30)
    input("Нажмите Enter, чтобы продолжить")



# запуск проги
menu_actions = {
    '1': show_menu,
    '2': average_price,
    '3': menu_add,
    '4': menu_delete,
    '5': menu_finder_by_price,
    '6': max_min_menu_position,
    '7': menu_drinks,
    '8': order,
    '9': exit,
}

program = True
while program:
    
    print("=" * 30)
    print("ГЛАВНОЕ МЕНЮ")
    print("=" * 30)
    print("1. Показать меню",
          "2. Вывести среднюю цену блюд",
          "3. Добавить блюдо в меню",
          "4. Удалить блюдо из меню",
          "5. Список блюд дешевле выбраного значения",
          "6. Самое дорогое и дешевое блюдо в меню",
          "7. Список напитков, отсортированный по цене",
          "8. Сделать заказ",
          "9. Выход из программы", sep="\n")
    print("=" * 30)

    choice = input("Выберите действие (1-9): ").strip()

    print("=" * 30)
    if choice in menu_actions:
        result = menu_actions[choice]()
        if result is False:
            break
    else:
        print("Неверный выбор! Пожалуйста, введите число от 1 до 10")
        input("Нажмите Enter, чтобы продолжить")


# ЙОУ