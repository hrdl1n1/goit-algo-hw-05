import os
import sys
import pathlib
from collections import Counter
from typing import List

# Створюємо словник типів помилок
mistake_dict = {'ERROR', 'INFO', 'DEBUG', 'WARNING'}

# Функція для завантаження журналів з файлу
def load_logs(file_path: str) -> list:
    list_logs = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            for line in f.readlines():
                list_logs.append(parse_log_line(line))
        return list_logs
    else:
        print('Вказаний файл НЕ існує')


# Функція для розбору рядка журналу
def parse_log_line(line: str) -> dict:
    date, time, log, *message = line.split()
    mistake = ' '.join(message)
    dict_ = {'date': date, 'time': time, 'type': log, 'mistake': mistake}
    return dict_


# Функція для підрахунку кількості журналів за рівнями
def count_logs_by_level(list) -> dict:
    errors_dict = Counter([d['type'] for d in list])
    return errors_dict


# Функція для відображення кількості журналів за рівнями
def display_log_counts(errors_dict):
    print(f'Рівень логування | Кількість')
    print('_ _ _ _ _ _ _ _ _| _ _ _ _ _ ')
    for key, value in errors_dict.items():
        print(f'{key}\t\t | {value}')


# Функція для фільтрування журналів за рівнем з використанням filter
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda x: x['type'] == level, logs))


# Функція для сортування журналів за датою та часом з використанням sorted та lambda
def sort_logs_by_date(logs: List[dict]) -> List[dict]:
    return sorted(logs, key=lambda x: (x['date'], x['time']))


# Функція для отримання списку лише дат журналів з використанням map
def get_dates(logs: List[dict]) -> List[str]:
    return list(map(lambda x: x['date'], logs))


try:
    input = sys.argv[1]  # Отримуємо шлях до файлу з аргументів командного рядка
    address = pathlib.Path(input)  # Конвертуємо у об'єкт шляху
    dict_lines = load_logs(address)  # Завантажуємо журнали з файлу
    conuted_logs = count_logs_by_level(dict_lines)  # Підраховуємо кількість журналів за рівнями
    display_log_counts(conuted_logs)  # Відображаємо кількість журналів за рівнями

    log_level = sys.argv[2]  # Отримуємо рівень журналу з аргументів командного рядка
    if log_level.upper() in mistake_dict:  # Перевіряємо, чи введено коректний рівень журналу
        filtered_logs = filter_logs_by_level(dict_lines, log_level.upper())
        print(f'Деталі логів для рівня {log_level}:')
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['mistake']}")
    else:
        print('Некоректний параметр логування')  # Якщо рівень журналу введено некоректно, виводимо повідомлення
except IndexError:
    print("Введіть шлях до файлу та рівень журналу як аргументи командного рядка.")
except FileNotFoundError:
    print("Вказаний файл не існує.")
except Exception as e:
    print(f"Виникла помилка: {e}")