# 3 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [394441; 394505],
# числа, имеющие максимальное количество различных делителей.
# Если таких чисел несколько, то найдите минимальное из них. Выведите количество делителей найденного числа
# и два наибольших делителя в порядке убывания.

def sofar(number) -> list:
    dividers = []
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers.append(divider)

    return dividers


max_dividers = 0
for oper_number in range(394441, 394506):
    if len(sofar(oper_number)) > max_dividers:
        max_dividers = len(sofar(oper_number))

max_dividers_number = []
for oper_number in range(394441, 394506):
    if len(sofar(oper_number)) == max_dividers:
        max_dividers_number.append(oper_number)

fitting_number = max_dividers_number[0]
dividers_of_fitting = sofar(fitting_number)

print(len(dividers_of_fitting), dividers_of_fitting[len(dividers_of_fitting)-1],
      dividers_of_fitting[len(dividers_of_fitting)-2])
