def to_base_six(number) -> str:
    number_six = ""
    while number > 0:
        number_six = str(number % 6) + number_six
        number = number // 6

    return number_six


count = 0
max_good = None

for i in range(1000, 10000):
    count_digits = 0
    i_six = int(to_base_six(i))

    while i_six > 0:
        i_six = i_six // 10
        count_digits = count_digits + 1

        if count_digits <= 5:
            if i_six - (i_six // 100 * 100) == 13 or i_six - (i_six // 100 * 100) == 14:
                count = count + 1
                max_good = i

print(count, max_good)
