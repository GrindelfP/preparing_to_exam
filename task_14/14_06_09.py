n = 729**8 - 3**18 + 85
counter = 0
while n > 0:
    if n % 9 == 0:
        counter = counter + 1
    n = n // 9

print(counter)


"""Значение выражения 729^8 – 3^18 + 85 записали в системе счисления
с основанием 9. Сколько раз в этой записи встречается цифра 0?"""
