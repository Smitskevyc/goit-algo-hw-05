import re
from typing import Callable

# Функція generator_numbers
def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    pattern = r'\b\d+\.\d+\b'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)  # Перетворюємо кожен знайдений рядок на число та повертаємо його

# Функція sum_profit
def sum_profit(text: str, func: Callable):
    return sum(func(text))  # Використовуємо генератор для підсумовування всіх чисел

# Приклад використання функцій
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
