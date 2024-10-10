def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#   1.Функция с параметрами по умолчанию:
print_params(b = 25)         # 1 25 True
print_params(c = [1,2,3])    # 1 строка [1, 2, 3]
print_params()               # 1 строка True
#print_params(1, 'pen', False, 25.5)   Выдает ошибку, потому что не совпадает кол-во параметров

#   2.Распаковка параметров:
values_list = [True, 100, 'char']
values_dict = {'a': 'symbol', 'b': False, 'c': 1.5}
print_params(*values_list)   # True 100 char
print_params(**values_dict)  # symbol False 1.5

#   3.Распаковка + отдельные параметры:
values_list_2 = ['word', 0]
print_params(*values_list_2, 42) # word 0 42