def count_sum_of_digits(number) -> int:
    sum_of_digits = 0
    while number > 0:
        sum_of_digits = sum_of_digits + (number - number//10*10)
        number = number//10

    return sum_of_digits


counter = 0
min_number = 234567+1
for operated_number in range(123456, 234567+1):
    if operated_number % count_sum_of_digits(operated_number) == 0:
        counter = counter + 1

        if operated_number < min_number:
            min_number = operated_number

print(counter, min_number)

"""Определите количество принадлежащих отрезку [123 456; 234 567]
натуральных чисел, которые делятся без остатка на сумму своих цифр, и
наименьшее из таких чисел. В ответе запишите два целых числа: сначала
количество, затем наименьшее число."""
