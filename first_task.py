def caching_fibonacci():
    # Створюємо порожній словник для кешування значень
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]
        
        # Якщо немає, обчислюємо та зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання функції
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
