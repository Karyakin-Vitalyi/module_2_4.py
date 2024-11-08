# Домашняя работа "Цикл for. Элементы списка. Полезные функции в цикле"

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и составных чисел
primes = []
not_primes = []

# Перебор списка numbers
for num in numbers:
    if num < 2:
        continue
    is_prime = True  # Флаг для обозначения простого числа
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Если число делится нацело на что-то, кроме 1 и самого себя, то оно не простое
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Вывод списков простых и составных чисел
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
