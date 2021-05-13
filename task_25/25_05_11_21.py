def sofar_2(number) -> int:
    min_divider = number
    max_divider = 2
    for divider in range(2, number):
        if number % divider == 0:
            if min_divider > divider:
                min_divider = divider
            if max_divider < divider:
                max_divider = divider

    sum_of_dividrs = min_divider + max_divider

    return sum_of_dividrs


counter = 0
fitting_numbers = []
for operated_number in range(452021, 500000):
    if sofar_2(operated_number) % 7 == 3:
        fitting_numbers.append(operated_number)
        if counter < 5:
            counter = counter + 1
        elif counter == 5:
            break

for number in fitting_numbers:
    print(number, sofar_2(number))


# Пусть M – сумма минимального и максимального натуральных делителей
# целого числа, не считая единицы и самого числа. Если таких делителей
# у числа нет, то считаем значение M равным нулю.
# Напишите программу, которая перебирает целые числа, большие 452 021,
# в порядке возрастания и ищет среди них такие, для которых значение M
# при делении на 7 даёт в остатке 3. Вывести первые 5 найденных чисел
# и соответствующие им значения M.
# Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке
# сначала выводится само число, затем – значение М.
# Строки выводятся в порядке возрастания найденных чисел.
