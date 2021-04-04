count = 0
summary = ""
min_good = None


def number_count(number):
    counter = 0
    while number > 0:
        number = number // 10
        counter = counter + 1

    return counter


for i in range(3466, 9081):
    if len(str(i)) != (len(oct(i)) - 2) and (i % 7 == 1) and (i % 7 == 5):
        count = count + 1
        min_good = i

print(count, min_good)
