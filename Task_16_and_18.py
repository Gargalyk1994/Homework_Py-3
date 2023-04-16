#Написать программу, которая при вводе числа, имеющегося в списке выводит сколько раз встречается
# это число, но если числа в списке нет, то прога выводит ближайшее по значению число
import random

size = int(input('Введите размер списка: '))
my_list = []
for _ in range(size):
    my_list.append(random.randint(1, 99))
# или my_list =[random.randint(0,100) for _ in range(size)]
print(my_list)
num = int(input('Введите искомое число: '))
count = 0
index = 0
min_value = abs(num - my_list[0])
for i in range(size):
    if num == my_list[i]:
        count += 1
    elif abs(num - my_list[i]) <= min_value: # abs() - это модуль числа, преобразует отрицательное в положительное
            min_value = abs(num - my_list[i])
            index = i
            # print(min_value)

print(f'Число {num} встречается {count} раз')
print(f'Ближайшее к числу {num} : число {my_list[index]}')



