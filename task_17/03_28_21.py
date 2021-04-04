count = 0
summary = ""
max_good = None


def binar(num) -> int:
    num = bin(num)
    num = num.replace("0", "", 1)
    num = int(num.replace("b", "", 1))

    return num


def digits_sum(num) -> int:
    sum = 0
    while num > 1:
        digit = num - num // 10 * 10
        sum = sum + digit
        num = num // 10
    sum = sum + num

    return sum


for i in range(31, 2047+1):
    number = binar(i)
    last_digit = number - number//10*10
    if last_digit == 0 and digits_sum(number) == 5 and i % 10 != 0:
        count = count + 1
        max_good = i

print(count, max_good)
