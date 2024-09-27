#Словарь:
my_dict = {'Ilya': 2001, 'Danil': 2002, 'Roman': 2000}
print('Dict:', my_dict)                          #словарь my_dict
print('Existing value:', my_dict['Ilya'])        #одно значение по существующему ключу
print('Not existing value:', my_dict.get('Max')) #одно по отсутствующему ключу
my_dict.update({'Diana': 1999, 'Maria': 1998})   #две новые пары
del_val = my_dict.pop('Roman')                   #удаление одной пары
print('Deleted value:', del_val)                 #вывод удаленной пары
print('Modified dictionary:', my_dict)           #измененный словарь my_dict
#Множество:
my_set = {100, True, True, 'book', 100, 'book'}
print('Set:', my_set)                            #множество my_set
my_set.add((1, 2))                               # два новых..
my_set.add(0.5)                                  # ..элемента
my_set.discard(True)                             #удаление элемента
print('Modified set:', my_set)                   #измененное множество my_set