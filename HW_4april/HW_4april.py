# Задание: Лог-файл событий пользователя
# Условие
# Есть текстовый файл с логами действий пользователя:
# [2025-03-21 14:23:05] user_123: login
# [2025-03-21 14:25:10] user_123: view_page
# [2025-03-21 15:10:55] user_123: logout
# [2025-03-21 16:00:00] user_456: loginimport re

from datetime import datetime
from collections import defaultdict
import time

# Сделать декоратор, который:
# логирует время выполнения функции
# пишет в консоль: “Функция X выполнена за Y секунд”
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} выполнена за {time.time() - start:.4f} секунд")
        return result

    return wrapper


# Распарсить строку лога:
# дата
# user_id
# действие
def parse_line(line):
    match = re.match(r'\[(.*?)\]\s+(user_\d+):\s+(\w+)', line)
    if not match:
        raise ValueError(f"Невалидная строка: {line.strip()}")

    date_str, user_id, action = match.groups()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"Неверная дата: {date_str}")

    return date, user_id, action



@timer
def process_logs():
    users = defaultdict(lambda: {
        "actions": 0,
        "time": 0,
        "login_time": None
    })
    try:
        with open("HW_4april.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("ошибка файл itis21.txt не найден")
        return {}
    for line in lines:
        parsed = parse_line(line)
        if not parsed:
            continue

        date, user_id, action = parsed

        users[user_id]["actions"] += 1

        if action == "login":
            # проверка на login с уже залогиненным пользователем
            if users[user_id]["login_time"] is not None:
                print(f"ошибка: у {user_id} уже есть login")
            users[user_id]["login_time"] = date


        elif action == "logout":
            # проверка на logout без login
            if users[user_id]["login_time"] is None:
                print(f"ошибка: logout без login у {user_id}")
                continue

            session_time = (date - users[user_id]["login_time"]).total_seconds()

            if session_time < 0:
                print(f"logout раньше login у {user_id}")
                users[user_id]["login_time"] = None
                continue

            users[user_id]["time"] += session_time
            users[user_id]["login_time"] = None

        # проверка на login без logout
    for user_id, data in users.items():
        if data["login_time"] is not None:
            print(f"Предупреждение: у {user_id} нет logout после login")

    return users



users = process_logs()

# сортировка
sorted_users = sorted(users.items(), key=lambda x: x[1]["time"], reverse=True)

# вывод
for user, data in sorted_users:
    print(user)
    print("  время:", data["time"])
    print("  действий:", data["actions"])
