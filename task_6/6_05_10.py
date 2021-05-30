max_one = 0

for i in range(1, 100000):
    s = i
    n = 1
    while s < 47:
        s = s + 4
        n = n * 2
    if n == 64:
        if i > max_one:
            max_one = i

print(max_one)

# Определите, при каком наибольшем введённом значении переменной s программа выведет число 64.
