# 1 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [126849; 126871],
# числа, имеющие ровно 4 различных делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.

def count_dividers(number) -> list:
    dividers = []
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers.append(divider)

    return dividers


for operated_number in range(126849, 126872):
    if len(count_dividers(operated_number)) == 4:
        print(operated_number, count_dividers(operated_number))


# 2 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [190061; 190080],
# числа, имеющие ровно 4 различных НЕЧЁТНЫХ делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке убывания.

def count_dividers(number) -> list:
    dividers = []
    for divider in range(1, number + 1):
        if number % divider == 0 and divider % 2 != 0:
            dividers.append(divider)
    return dividers


for operated_number in range(190061, 190081):
    if len(count_dividers(operated_number)) == 4:
        lst = count_dividers(operated_number)
        lst.reverse()
        print(operated_number, lst)
