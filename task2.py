import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b(?:\d+\.\d+|\d+\b\.\d+)\b'  # Враховуємо десяткові дроби та числа перед крапкою
    # Пошук у тексті за допомогою регулярних виразів
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Викликаємо функцію generator_numbers та обчислюємо суму чисел
    return sum(func(text))

# Приклад використання:
text = "The profit for this quarter is 100.25 300.75 50.5"
total_profit = sum_profit(text, generator_numbers)
print("Total profit:", total_profit)