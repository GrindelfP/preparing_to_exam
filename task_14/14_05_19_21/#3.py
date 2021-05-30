# 3 Число 430 записали в системах счисления с основаниями от 2 до 10 включительно. При каких основаниях цифры этого
# числа расположены слева направо в порядке убывания? В ответе укажите сумму всех подходящих оснований.
for base in range(2, 11):
    new_number = []
    number = 430
    while number > 0:
        new_number.append(number % base)
        number = number // base
    new_number = new_number[::-1]

    fitting_bases = []
    counter = 0
    for n in range(1, len(new_number)):
        if new_number[n] < new_number[n - 1]:
            counter = counter + 1
            if counter == len(new_number) - 1:
                fitting_bases.append(base)

    sum_of_bases = 0
    for base_2 in fitting_bases:
        sum_of_bases = sum_of_bases + base_2

print(sum_of_bases)
