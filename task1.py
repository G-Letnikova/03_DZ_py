# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
# -----------------------------------------------------------------------------------

from random import randint
from math import fabs
count = 0
number = int(input('введите число:'))
len_array = int(input('введите количество эл-тов массива:'))
lst = [randint(1, 101) for x in range(len_array)]
print(lst)
a = int(fabs(lst[0] - number))
etalon = lst[0]
for i in range(len_array):
    if int(fabs(lst[i] - number)) < a:
        a = int(fabs(lst[i] - number))
        etalon = lst[i]
    if int(lst[i]) == number:
        count += 1
print(f'число {number} встречается {count} раз' if count != 0 else f'ближайшее число к {number} --> {etalon}')