def formatting(list_):
    list_un = []                               # Убирает вложенные списки
    for k in list_:
        list_un.extend(k)

    str_ = str(list_un)                        # Готовый список в строку
    str_ = str_.replace("[", "", ) # Убираем из строки всё лишнее,
    str_ = str_.replace("]", "", ) # форматируя ее в нужный вид,
    str_ = str_.replace(" ", "", ) # состоящий только из цифр без
    str_ = str_.replace(",", "", ) # запятых и т.д.
    print(f'Пароль для {n}: {str_}')

n = int(input('Введите число из первой вставки >> '))
list_1_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_result = []
for a in list_1_20:                            # Получаем список с вложенными парами чисел,
    for b in list_1_20:                        # подходящие под условия
        if a != b and n % (a + b) == 0:
                list_result.append([a, b])
for i in list_result:                          # Оставляем только уникальные пары чисел
    for j in list_result:
        if i == j[::-1]:
            list_result.remove(j)

formatting(list_result)                        # Выводим строку с ответом без лишних знаков