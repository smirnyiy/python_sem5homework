# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

str_for_com = input('Введите текст для сжатия: ')


def compr(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding


print(compr(str_for_com))

def rec(t):
    sym = ''
    res = ''
    for i in range(len(t)):
        if t[i].isdigit():
            sym += t[i]
        else:
            res = res + t[i] * int(sym)
            sym = ''
    return res

print(rec(compr(str_for_com)))  
