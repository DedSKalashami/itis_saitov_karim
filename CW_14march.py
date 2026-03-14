from functools import reduce
import numpy as np

temperatures = np.random.randint(-20, 40, 10000)

# print(temperatures)


# 1
def temperature_stream(data):
    for temperature in data:
        yield temperature


# 2
def cleaning_gen(data):
    for temp in data:
        if -15 <= temp <= 35:
            yield temp


# 3
clean_data = np.array(list(cleaning_gen(temperatures)))
mean_value = np.mean(clean_data)
std_value = np.std(clean_data)

normalized_data = map(lambda x: (x - mean_value) / std_value, cleaning_gen(temperature_stream(temperatures)))
# print(list(normalized_data))


# 4
transformed_data = map(lambda x: np.sin(x) + x**2, normalized_data)
# print(list(transformed_data))

counter_window = 0 # финал
# 5
def window_gen(data):
    global counter_window 
    window = []
    for temp in data:
        window.append(temp)
        if len(window) == 30:
            yield window
            window = []
            counter_window += 1

windows = window_gen(transformed_data)
# print(list(windows))

# 6
def window_analyzer(window):
    return {
        "mean": np.mean(window),
        "median": np.median(window),
        "std": np.std(window),
        "min": np.min(window),
        "max": np.max(window)
    }

windows_stats = list(map(window_analyzer, windows))
# print(window_stats)


# 7
anomalous_windows = list(filter(lambda w_stats: abs(w_stats["mean"]) > 1 or w_stats["std"] > 1, windows_stats) )
# print(anomalous_windows)


# 8
# counter_anomalous = len(anomalous_windows)
# ИЛИ
counter_anom = reduce(lambda counter, _: counter + 1, anomalous_windows, 0)
sum_mean = reduce(lambda sum_, stat: sum_ + stat["mean"], anomalous_windows, 0)
max_mean = reduce(lambda cur_max, stat: max(cur_max, stat["mean"]), anomalous_windows, -100)
# print(counter_anom, sum_mean, max_mean)


# Финальный вывод программы

print(counter_anom, sum_mean, max_mean)
print(f"Всего окон: {counter_window}")
print(f"Аномальных окон: {counter_anom}")
print(f"Максимальное среднее значение: {max_mean}")
print(f"Сумма средних значений: {sum_mean}")
