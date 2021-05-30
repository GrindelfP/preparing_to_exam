# 1 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [586132; 586430],
# числа, имеющие максимальное количество различных делителей. Найдите минимальное и максимальное из таких чисел.
# Для каждого из них в отдельной строчке выведите количество делителей и два наибольших делителя в порядке убывания

def sofar(number) -> list:
    dividers = []
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers.append(divider)

    return dividers


max_dividers = 0
for oper_number in range(586132, 586431):
    if len(sofar(oper_number)) > max_dividers:
        max_dividers = len(sofar(oper_number))

max_dividers_number = []
for oper_number in range(586132, 586431):
    if len(sofar(oper_number)) == max_dividers:
        max_dividers_number.append(oper_number)

fitting_number_min = max_dividers_number[0]
fitting_number_max = max_dividers_number[len(max_dividers_number)-1]
dividers_of_min_fitting = sofar(fitting_number_min)
dividers_of_max_fitting = sofar(fitting_number_max)

print(fitting_number_min, len(dividers_of_min_fitting), dividers_of_min_fitting[len(dividers_of_max_fitting) - 1],
      dividers_of_min_fitting[len(dividers_of_max_fitting) - 2])
print(fitting_number_max, len(dividers_of_max_fitting), dividers_of_max_fitting[len(dividers_of_max_fitting) - 1],
      dividers_of_max_fitting[len(dividers_of_max_fitting) - 2])


# 2 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [394480; 394540],
# числа, имеющие максимальное количество различных делителей. Выведите информацию о таких числах,
# расположив их в порядке возрастания. Для каждого числа выведите его порядковый номер,
# количество делителей и два наибольших делителя в порядке убывания
def sofar(number) -> list:
    dividers = []
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers.append(divider)
    return dividers


list_of_numbers = []
max_dividers = 0
for oper_number in range(394480, 394541):
    list_of_numbers.append(oper_number)
    if len(sofar(oper_number)) > max_dividers:
        max_dividers = len(sofar(oper_number))

max_dividers_number = []
for oper_number in range(394480, 394541):
    if len(sofar(oper_number)) == max_dividers:
        max_dividers_number.append(oper_number)

greatest = ""
lesser = ""

for number in max_dividers_number:
    position_last_divider = len(sofar(number)) - 1
    position_pre_last_divider = len(sofar(number)) - 2

    number_of_dividers = len(sofar(number))
    greatest = sofar(number)[position_last_divider]
    lesser = sofar(number)[position_pre_last_divider]

    print(number, list_of_numbers.index(number) + 1, number_of_dividers, greatest, lesser)


# 3 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [194441; 196500]
# числа (в порядке возрастания) с нечётным количеством делителей. Для каждого такого числа выведите его порядковый номер
# (начиная с единицы), само число, количество его делителей и делитель, квадрат которого равен этому числу.
def sofar(number) -> list:
    dividers = []
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers.append(divider)
    return dividers


list_of_numbers = []
numbers_odd_dividers = []
max_dividers = 0
for oper_number in range(194441, 196501):
    list_of_numbers.append(oper_number)
    if len(sofar(oper_number)) % 2 != 0:
        numbers_odd_dividers.append(oper_number)

for number in numbers_odd_dividers:
    position_last_divider = len(sofar(number)) - 1
    position_pre_last_divider = len(sofar(number)) - 2

    number_of_dividers = len(sofar(number))
    greatest = sofar(number)[position_last_divider]
    lesser = sofar(number)[position_pre_last_divider]

    print(list_of_numbers.index(number) + 1, number, number_of_dividers, number**0.5)
