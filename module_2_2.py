first = int(input('Укажите первое число > '))
second = int(input('Укажите второе число > '))
third = int(input('Укажите третье число > '))
if first == second == third:                                #все равны
    print('3')
elif first == second or first == third or second == third:  #2 из 3 равны
    print('2')
else:                                                       #все не равны
    print('0')