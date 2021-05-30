def sum_of_digits(number) -> int:
    digits_sum = 0
    while number > 0:
        digit = number - (number // 10) * 10
        number = number // 10
        digits_sum = digits_sum + digit

    return digits_sum


counter = 0
min_number = 456789
for i in range(345678, 456790):
    if i % sum_of_digits(i) == 0:
        counter = counter + 1
        if i < min_number:
            min_number = i


print(counter, min_number)

# Определите количество принадлежащих отрезку [345 678; 456 789] натуральных чисел, которые делятся без остатка
# на сумму своих цифр, и наименьшее из таких чисел.
