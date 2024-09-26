immutable_var = (1, True, 'moon', 2.5)
print(immutable_var)
# immutable_var[0] = 2
# immutable_var[1] = False
# immutable_var[2] = 'sun'
# immutable_var[3] = 5.0
# print(immutable_var)
# При попытке изменить элементы кортежа консоль выдаёт ошибку:
# 'tuple' object does not support item assignment, означающую, что
# кортеж относится к неизменяемым типам данных.
mutable_list = [1, True, 'moon', 2.5]
mutable_list[0] = 2
mutable_list[1] = False
mutable_list[2] = 'sun'
mutable_list[3] = 5.0
print(mutable_list)
