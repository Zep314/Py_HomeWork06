# Число 197 называется круговым простым числом, потому что все перестановки его 
# цифр с конца в начало являются простыми числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

# Сколько существует круговых простых чисел меньше миллиона?

import time

def isSimple(n):
    if n % 2 == 0: # если четное, и не двойка
        return n == 2
    d = 3 
    while d * d <= n and n % d != 0: # ищем наименьший делитель n
        d += 2 # простые числа всегда нечетные, потому шаг = 2
    return d * d > n

def AllShift(n): # Сдвигаем цифры числа по кругу и формируем из этих чисел список
    ret = []
    string = str(n)
    for i in range(len(string)):
        string = string[-1]+string[:-1] # вот он, сдвиг
        ret.append(int(string))
    return ret

def isAroundNum(n): # проверяем, являяется ли число круговым
    if str(n).find('0') > -1: # если есть цифра 0 в числе - то выкидываем его сразу
        return False
    flag = True
    for num in AllShift(n):
        if not isSimple(num): 
            flag = False
            break
    return flag

def CountArounNums(limmit):
    return sum([1 for i in range(2,limmit+1) if isAroundNum(i)])

start_time = time.time()
print(CountArounNums(100))
print(CountArounNums(1000000))
print(f'Программа работала {time.time() - start_time} секунд [{time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time))}]')
# программа работает ~20 секунд на долхом ноуте (на хорошущем - 3 секунды) - насчитало 55 штук
