numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:                # Перебираем список numbers
    if i > 1:                    # Исключаем 1 из списка
        is_prime = True          # flag
        for j in range(2, i):    # Перебираем j от 2 до i(не включительно)
            if i % j == 0:       # Проверка на простое число
                is_prime = False
                break
        if is_prime:
            primes.append(i)     # Дополняем список простыми числами
        else:
            not_primes.append(i) # Дополняем список Не простыми числами
print(primes)
print(not_primes)