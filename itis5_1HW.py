# Проект: «Библиотечная система»
# При запуске программа выдаёт меню. Пользователь вводит номер действия, и программа выполняет его.
import os
import csv

library = {
            "Война и мир": {
            "author": "Л. Толстой", 
            "year": 1869, 
            "reviews": [5, 4, 5],
            "rating": 4.67
        },
            "Преступление и наказание": {
            "author": "Ф. Достоевский", 
            "year": 1866, 
            "reviews": [5, 5, 4],
            "rating": 4.67
        },
            "Преступление и п": {
            "author": "Ф. Достоевский", 
            "year": 1850, 
            "reviews": [5, 4, 4],
            "rating": 4.33
        }
}



# 1 Добавить книгу (название, автор, год, список оценок читателей).
def book_addition():
    print("="*30)

#   ввод названия
    book_name_input = input("Введите название книги: ") 

#   ввод имени автора
    book_author_input = input("Введите автора книги: ") 

#   ввод года
    book_year_input = ""
    while book_year_input == "":
        try:
            book_year_input = int(input("Введите год книги: "))
        except ValueError:
            print("Введите число!")
            book_year_input = ""

#   ввод оценок
    book_reviews_input = ""
    flag = False
    while flag == False:
        try: 

            book_reviews_input = input("Введите оценки книги через пробел (1-5): ")

            book_reviews_input = [int(x) for x in book_reviews_input.split()]
            if all(int(x) <= 5 and int(x) >= 1 for x in book_reviews_input):
                flag = True
            else: 
                print("Введите числа 1-5 через пробел!")
                flag = False
        except ValueError:
            print("Введите числа 1-5 через пробел!")

# средняя оценка
    book_rating_input = round(sum(book_reviews_input) / len(book_reviews_input), 2)
    
# регистрация книги
    book = {
            book_name_input: {
            'author': book_author_input,
            'year': book_year_input,
            'reviews': book_reviews_input,
            'rating': book_rating_input
            }
    }
    library.update(book)
    print("="*30)
    print("Книга добавлена!")
    input("Нажмите Enter, чтобы продолжить")



# 2 Показать все книги.
def show_library():
    print("="*30)
    print("Библиотека: ")
    print("-"*30)
    for book_title, book_info in library.items():
        print(f"Название: {book_title}")
        print(f"Автор: {book_info['author']}")
        print(f"Год: {book_info['year']}")
        print(f"Отзывы: {book_info['reviews']}")
        print(f"Рейтинг: {book_info['rating']}")
        print("-" * 30)
    input("Нажмите Enter, чтобы продолжить")



# 3 Найти книгу по названию.
def book_finder_by_name():
    print("="*30)
    name_search = input("Введите название книги для поиска: ").lower()
    print("="*30)
    print("Все найденные результаты:")
    print("-" * 30)

    flag = False
    for book_name, book_info in library.items():
        if name_search in book_name.lower():
            flag = True
            print(f"Название: {book_name}",)
            print(f"Автор: {book_info['author']}")
            print(f"Год: {book_info['year']}")
            print(f"Отзывы: {book_info['reviews']}")
            print(f"Рейтинг: {book_info['rating']}")
            print("-" * 30)
    if flag == False:
        print("По запросу ничего не найдено!")
        print("-" * 30)
    input("Нажмите Enter, чтобы продолжить")



# 4 Удалить книгу.
def book_delete():
    print("="*30)
    name_del = input("Введите точное название книги, которую вы хотите удалить, соблюдая регистр и знаки препинания: ")
    try:
        del library[name_del]
        print('Книга удалена!')
    except KeyError:
        print('Книга не найдена!')
    input("Нажмите Enter, чтобы продолжить")



# 5 Добавить новую оценку книге.
def book_review_addition():
    print("="*30)
    name_review_add = input("Введите точное название книги, к которой вы хотите добавить оценку, соблюдая регистр и знаки препинания: ")

# если книги нет - сразу выброс
    if name_review_add not in library:
        print('Книга не найдена!')
        input("Нажмите Enter, чтобы продолжить")
        return

    book_info = library[name_review_add]
# проверка на правильный воод оценки
    flag = False
    while flag == False:
        try: 
            review_add = int(input("Введите оценку книге(1-5): "))
            if review_add >= 1 and review_add <= 5:
                flag = True
                book_info["reviews"].append(review_add)
            else:
                print("Введите число 1-5!")
                a = int("a")
        except ValueError:
            flag = False

    # изменение рейтинга с новой оценкой
    book_info["rating"] = round(sum(book_info["reviews"]) / len(book_info["reviews"]), 2)

    print("="*30)
    print("Оценка добавлена! (рейтинг изменился)")
    input("Нажмите Enter, чтобы продолжить")



# 6 Вывести список книг, выпущенных после определённого года.
def book_finder_by_year():
    print("="*30)

    flag = False
    while flag == False:
        try:
            year_finder = int(input("Введите год, после которого были выпущены искомые книги: "))
            flag = True
        except ValueError:
            print("Введите число(год)!")
            flag = False
    
    print("="*30)
    print("Все найденные результаты:")
    print("-" * 30)

    flag = False
    for book_name, book_info in library.items():
        if book_info["year"] >= year_finder:
            flag = True
            print(f"Название: {book_name}",)
            print(f"Автор: {book_info['author']}")
            print(f"Год: {book_info['year']}")
            print(f"Отзывы: {book_info['reviews']}")
            print(f"Рейтинг: {book_info['rating']}")
            print("-" * 30)
    if flag == False:
        print("По запросу ничего не найдено!")
        print("-" * 30)
    input("Нажмите Enter, чтобы продолжить")



# 7 Показать все книги с рейтингом выше определённого порога.
def book_finder_by_rating():
    print("="*30)

    flag = False
    while flag == False:
        try:
            rating_finder = float(input("Введите число-порог(не обязательно целое, через точку), чтоб отобразить книги с рейтингом выше этого порога: "))
            flag = True
        except ValueError:
            print("Введите число(рейтинг)!")
            flag = False
    
    print("="*30)
    print("Все найденные результаты:")
    print("-" * 30)

    flag = False
    for book_name, book_info in library.items():
        if book_info["rating"] >= rating_finder:
            flag = True
            print(f"Название: {book_name}",)
            print(f"Автор: {book_info['author']}")
            print(f"Год: {book_info['year']}")
            print(f"Отзывы: {book_info['reviews']}")
            print(f"Рейтинг: {book_info['rating']}")
            print("-" * 30)
    if flag == False:
        print("По запросу ничего не найдено!")
        print("-" * 30)
    input("Нажмите Enter, чтобы продолжить")



# 8 Экспортировать книги в CSV-вид (название;автор;год;оценки).
def library_export():
    print("="*30)
    
    filename = input("Введите имя файла для экспорта (например, library.csv): ").strip()

    if not filename.endswith('.csv'):
        filename += '.csv'

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['Название', 'Автор', 'Год', 'Оценки'])
            for book_title, book_info in library.items():
                reviews_str = ' '.join(str(x) for x in book_info['reviews'])
                writer.writerow([book_title, book_info['author'], book_info['year'], reviews_str])
    
    except Exception as e:
        print(f"Произошла ошибка при экспорте: {e}")
    else:
        print(f"Данные успешно экспортированы в файл '{filename}'!")
        print(f"Экспортировано книг: {len(library)}")
    
    finally:
        print("="*30)
        input("Нажмите Enter, чтобы продолжить")




# 9 Импортировать книги из CSV.
def library_import():
    print("="*30)
    filename = input("Введите имя файла для импорта (например, library.csv): ").strip()
    
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден!")
        input("Нажмите Enter, чтобы продолжить")
        return

    books_added = 0
    books_updated = 0

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            
            header = next(reader, None)
            
            for row in reader:
                # Проверяем, что в строке достаточно данных
                if len(row) < 4:
                    print(f"Пропущена строка с недостаточным количеством данных:")
                    continue
                
                title, author, year_str, reviews_str = row
                
                # Обрабатываем год
                try:
                    year = int(year_str)
                except ValueError:
                    print(f"Ошибка в данных года для книги '{title}'. Год установлен в 0.")
                    year = 0
                
                # Обрабатываем оценки
                try:
                    reviews_list = [int(x) for x in reviews_str.split()]
                except ValueError:
                    print(f"Ошибка в данных оценок для книги '{title}'. Оценки не добавлены.")
                    reviews_list = []
                
                # Рассчитываем рейтинг
                rating = round(sum(reviews_list) / len(reviews_list), 2) if reviews_list else 0.0
                
                # Создаем или обновляем книгу в библиотеке
                # Если книга с таким названием уже есть - она будет обновлена
                if title in library:
                    books_updated += 1
                else:
                    books_added += 1
                
                library[title] = {
                    'author': author,
                    'year': year,
                    'reviews': reviews_list,
                    'rating': rating
                }
    
    except Exception as e:
        print(f"Произошла ошибка при импорте: {e}")

    else:
        print(" Импорт завершен успешно!")
        print(f" Добавлено новых книг: {books_added}")
        print(f" Обновлено существующих: {books_updated}")
    
    finally:
        print(f" Всего книг в библиотеке: {len(library)}")
        print("Операция импорта завершена.")
        print("="*30)
        input("Нажмите Enter, чтобы продолжить")



# 10 Выход.
def exit():
    print("="*30)
    print("Программа завершена.")
    print("="*30)
    return False



# запуск проги
menu_actions = {
    '1': book_addition,
    '2': show_library,
    '3': book_finder_by_name,
    '4': book_delete,
    '5': book_review_addition,
    '6': book_finder_by_year,
    '7': book_finder_by_rating,
    '8': library_export,
    '9': library_import,
    '10': exit
}

program = True
while program:
    
    print("=" * 30)
    print("ГЛАВНОЕ МЕНЮ")
    print("=" * 30)
    print('1. Добавить книгу (название, автор, год, список оценок читателей)',
          '2. Показать все книги',
          '3. Найти книгу по названию',
          '4. Удалить книгу',
          '5. Добавить новую оценку книге',
          '6. Вывести список книг, выпущенных после определённого года',
          '7. Показать все книги с рейтингом выше определённого порога',
          '8. Экспортировать книги в CSV-вид (название;автор;год;оценки)',
          '9. Импортировать книги из CSV',
          '10. Выход', sep='\n')
    print("=" * 30)
    
    choice = input("Выберите действие (1-10): ").strip()
    
    if choice in menu_actions:
        result = menu_actions[choice]()
        if result is False:
            break
    else:
        print("Неверный выбор! Пожалуйста, введите число от 1 до 10")
        input("Нажмите Enter, чтобы продолжить")


# ЙОУ