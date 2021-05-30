count = 0
max_fitting = 0


def first_check(number) -> bool:
    first_digit = int(str(number)[0])
    second_digit = int(str(number)[1])
    third_digit = int(str(number)[2])
    forth_digit = int(str(number)[3])
    if first_digit > second_digit and first_digit > third_digit and first_digit > forth_digit:
        first_condition = True
    else:
        first_condition = False

    if len(str(number)) > 4:
        fifth_digit = int(str(number)[4])
        if first_digit > fifth_digit:
            first_condition = True
        else:
            first_condition = False

        if len(str(number)) > 5:
            sixth_digit = int(str(number)[5])
            if first_digit > sixth_digit:
                first_condition = True
            else:
                first_condition = False

    return first_condition


def second_check(number) -> bool:
    number = str(number)
    if number.count("5") == 2 or number.count("5") == 4 or number.count("5") == 6:
        second_condition = True
    else:
        second_condition = False

    return second_condition


def third_check(number) -> bool:
    first_digit = str(number)[0]
    second_digit = str(number)[1]
    if int(first_digit) == 5 and int(second_digit) == 0:
        third_condition = True
    else:
        third_condition = False

    return third_condition


for i in range(1007, 746001):
    if first_check(i) and second_check(i):
        count = count + 1
        if third_check(i):
            max_fitting = i


print(count, max_fitting)
