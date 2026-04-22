# Задание: AdvancedStudentAnalytics (ООП + pandas)
# Контекст
# Есть файл students_extended.csv со следующими колонками:
# name - имя
# group - группа
# math, physics, cs - оценки
# attendance - посещаемость (%)
# city - город
# enrollment_year - год поступления
# scholarship - есть ли стипендия (True/False)
# project_score - оценка за проект (может быть NaN)
# Общие требования
# Вся логика должна быть реализована внутри одного класса
# DataFrame передаётся только при инициализации
# Никаких вычислений вне методов класса
# Методы должны:
# возвращать данные (DataFrame / Series / dict)
# не печатать внутри (print — только снаружи)

import pandas as pd


# Часть 1. Создание класса и подготовка данных


# Создать класс и метод:
class AdvancedStudentAnalytics:
    def __init__(self, df):
        self.df = df.copy()
        self._validate_columns() # ДОП ЗАДАНИЕ
        self._prepare_data()



    def _prepare_data(self):
        # Заполнить project_score медианой
        median_score = self.df['project_score'].median()
        self.df['project_score'] = self.df['project_score'].fillna(median_score)

        # Создать столбец average_grade
        self.df['average_grade'] = self.df[['math', 'physics', 'cs']].mean(axis=1)

        # Создать performance_level:
        # high ≥ 85
        # medium 70–84
        # low < 70
        def get_performance_level(avg):
            if avg >= 85:
                return 'high'
            if avg >= 70:
                return 'medium'
            return 'low'
        self.df['performance_level'] = self.df['average_grade'].apply(get_performance_level)

        # Создать risk_level:
        # high risk: attendance < 60 или average < 65
        # medium risk: attendance 60–75
        # low risk: иначе
        def get_risk_level(row):
            if row['attendance'] < 60 or row['average_grade'] < 65:
                return 'high risk'
            if 60 <= row['attendance'] <= 75:
                return 'medium risk'
            return 'low risk'

        self.df['risk_level'] = self.df.apply(get_risk_level, axis=1)

# ДОП ЗАДАНИЕ:
    def _validate_columns(self):
        required_columns = {
            "name",
            "group",
            "math",
            "physics",
            "cs",
            "attendance",
            "city",
            "enrollment_year",
            "scholarship",
            "project_score"
        }

        current_columns = set(self.df.columns)
        missing_columns = required_columns - current_columns

        if missing_columns:
            raise ValueError(f"Отсутствуют обязательные колонки: {missing_columns}")


# Часть 2. Методы класса


    # 1. top_students(n)
    # Возвращает топ-N студентов по среднему баллу
    def top_students(self, n):
        sorted_df = self.df.sort_values(by="average_grade", ascending=False)
        return sorted_df.head(n)

    # 2. group_stats()
    # Возвращает статистику по группам:
    # средний балл
    # средняя посещаемость
    # количество студентов
    def group_stats(self):
        return self.df.groupby('group').agg({
            'average_grade': 'mean',
            'attendance': 'mean',
            'name': 'count'
        }).rename(columns={'name': 'count'})

    # 3. at_risk_students()
    # Возвращает студентов с высоким риском
    def at_risk_students(self):
        return self.df[self.df['risk_level'] == 'high risk']

    # 4. scholarship_analysis()
    # Сравнение студентов (средний балл и посещаемость):
    # со стипендией
    # без
    def scholarship_analysis(self):
        return self.df.groupby('scholarship')[['average_grade', 'attendance']].mean()

    # 5. city_performance()
    # Возвращает (по оценкам):
    # лучший город
    # худший город
    def city_performance(self):
        city_avg = self.df.groupby('city')['average_grade'].mean()
        return {'best': city_avg.idxmax(), 'worst': city_avg.idxmin()}

    # 6. hidden_top_students()
    # Студенты:
    # average_grade > 85
    # но без стипендии
    def hidden_top_students(self):
        condition = (self.df["average_grade"] > 85) & (self.df["scholarship"] == False)
        return self.df[condition]

    # 7. lazy_geniuses()
    # Студенты:
    # average_grade > 85
    # attendance < 60
    def lazy_geniuses(self):
        return self.df[(self.df['average_grade'] > 85) & (self.df['attendance'] < 60)]


# ДОП ЗАДАНИЕ
    def performance_distribution(self):
        distribution = self.df["performance_level"].value_counts(normalize=True) * 100
        return distribution.to_dict()

    def recommendations(self):
        advice = []

        high_risk_count = self.at_risk_students().shape[0]
        hidden_top_count = self.hidden_top_students().shape[0]
        lazy_genius_count = self.lazy_geniuses().shape[0]

        if high_risk_count > 0:
            advice.append("увеличить посещаемость и усилить контроль студентов из группы риска")
        if hidden_top_count > 0:
            advice.append("пересмотреть систему стипендий")
        if lazy_genius_count > 0:
            advice.append("обратить внимание на сильных студентов с низкой посещаемостью")
        if not advice:
            advice.append("текущие показатели стабильны, критических рекомендаций нет")

        return advice


# Часть 3. Метод-композиция


    # Создать метод: def full_analysis(self):
    # Метод должен:
    # Использовать другие методы класса
    # Не дублировать их логику
    # Возвращать единый результат (например, dict)
    # В результат включить:
    # топ-3 студента
    # статистику по группам
    # количество студентов с высоким риском
    # количество “скрытых отличников”
    # количество “ленивых гениев”
    # лучший и худший город
    # анализ стипендий
    def full_analysis(self):
        full_result = {
            "top_3": self.top_students(3),
            "groups": self.group_stats(),
            "at_risk_count": self.at_risk_students().shape[0],
            "hidden_tops": self.hidden_top_students().shape[0],
            "lazy_count": self.lazy_geniuses().shape[0],
            "cities": self.city_performance(),
            "scholarship_stats": self.scholarship_analysis(),
            "performance_distribution": self.performance_distribution(),
            "recommendations": self.recommendations()
        }
        return full_result

# Часть 4. Использование

if __name__ == "__main__":
    df = pd.read_csv("students_extended.csv")
    analytics = AdvancedStudentAnalytics(df)

    print(analytics.top_students(3))
    print()
    print(analytics.group_stats())
    print()
    print(analytics.full_analysis())
    print()
    print(analytics.performance_distribution())
    print()
    print(analytics.recommendations())
