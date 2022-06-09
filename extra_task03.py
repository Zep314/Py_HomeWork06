# Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. 
# Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.
# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность 
# являются пятиугольными числами и значение D = |Pk − Pj| минимально, 
# и дайте значение D в качестве ответа.

import math
from itertools import combinations_with_replacement as combinations

def genP(n): # генерируем 5-ти значное число
    return n*(3*n-1)//2

def isP(n): # проверяем, является ли число 5-ти значным (взял из википедии)
    return ((math.sqrt(24*n+1)+1)/2).is_integer()

def is_D_number(a,b): # проверяем условие задачи
    return isP(a+b) and isP(abs(a-b)) and a!=b


#============== самма программа ==============

MAX_NUM = 100 # будем полагать, что числа где то тут...

list1 = [genP(i) for i in range(1,MAX_NUM)]

# # брутфорс - полный перебор (плохо...)
# flag = False
# for i in range(len(list1)-1):
#     for j in range(i+1,len(list1)):
#         if is_D_number(list1[i],list1[j]): # не факт, что комбинация оптимальна...
#             flag = True  
#             break
#     if flag: break

# if flag:
#     print(f'i={i} {list1[i]} {isP(list1[i])} {(math.sqrt(24*list1[i]+1)+1)/2}')
#     print(f'j={j} {list1[j]} {isP(list1[j])} {(math.sqrt(24*list1[j]+1)+1)/2}')
#     print(f'Найдены числа! {list1[i]} и {list1[j]} {is_D_number(list1[i],list1[j])}')
# else:
#     print('Числа не нашлись')

# ПРОДВИНУТОЕ РЕШЕНИЕ!
print('=======================================')
list2 = set(abs(a - b) for a, b in combinations(list1, 2) if is_D_number(a,b))
# специально не оборачивал в min сразу - хотелось посмотреть, что это за числа
print(list(list2))
print(min(list2))

