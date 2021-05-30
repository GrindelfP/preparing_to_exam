# (Е. Джобс) Значение арифметического выражения: N^25 – 2*N^13 + 10 записали в системе счисления с основанием N.
# Определите основание системы счисления, если известно, что сумма разрядов в числе, представленном в этой системе
# счисления, равна 75.
for n in range(2, 1001):
    sum_of_digits = 0
    number_list = []

    number = n**25 - 2*n**13 + 10
    while number > 0:
        number_list.append(number % n)
        number = number // n
    number_list = number_list[::-1]
    for i in number_list:
        sum_of_digits = sum_of_digits + i
    if sum_of_digits == 75:
        print(n)


