# ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, 
# которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную 
# с помощью Rot13 . Если в строку включены числа или специальные символы, 
# они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает 
# эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'+ \
          'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'+ \
          'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
          'abcdefghijklmnopqrstuvwxyz'  

def enc(text, key = 13):
    ret = ''
    for ch in text:
        if ch in alfavit:
            ret += alfavit[(alfavit.find(ch)+key) % len(alfavit)]
        else: ret += ch
    return ret

def dec(text, key = 13):
    ret = ''
    for ch in text:
        if ch in alfavit:
            ret += alfavit[(alfavit.find(ch)-key) % len(alfavit)]
        else: ret += ch
    return ret


s = 'ПривеТ ДрУг!!!!'
print(s)
print(dec(enc(s)))
