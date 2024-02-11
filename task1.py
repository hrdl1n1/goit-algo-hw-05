def caching_fibonacci():
    cache = {}  # Створення порожнього словника кешу

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевірка, чи вже є значення у кеші
            return cache[n]
        else:
            # Обчислення числа Фібоначчі рекурсивно
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci  # Повернення внутрішньої функції fibonacci


# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Поверне 55
print(fib(20))  # Поверне 6765