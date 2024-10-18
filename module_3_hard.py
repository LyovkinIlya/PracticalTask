def calculate_structure_sum(arg):
    """
    Перебирает все элементы коллекции.
    Если элемент числового типа (тип bool тоже), прибавляет его к сумме.
    Если строкового типа, прибавляет кол-во символов строки.
    Если элемент является словарем, возвращает его в виде кортежа рекурсией обратно в функцию и суммирует.
    Во всех остальных случаях, когда элемент - список, множество или кортеж,
    пропускает уже этот элемент через функцию и прибавляет к сумме.
    Возвращает сумму.
    """
    summa = 0
    for i in arg:
        if isinstance(i, (int, float)):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, dict):
            summa += calculate_structure_sum(i.items())
        else:
            summa += calculate_structure_sum(i)
    return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) #99