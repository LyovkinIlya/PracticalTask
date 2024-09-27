#Словарь:
my_dict = {'Ilya': 2001, 'Danil': 2002, 'Roman': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ilya'])
print('Not existing value:', my_dict.get('Max'))
my_dict.update({'Diana': 1999, 'Maria': 1998})
del_val = my_dict.pop('Roman')
print('Deleted value:', del_val)
print('Modified dictionary:', my_dict)
#Множество:
my_set = {100, True, True, 'book', 100, 'book'}
print('Set:', my_set)
my_set.add((1, 2))
my_set.add(0.5)
my_set.discard(True)
print('Modified set:', my_set)