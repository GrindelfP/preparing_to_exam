min_x = 10000

for i in range(1, 10001):
    for j in range(1, 10001):
        s = i
        x = j
        s = 100*s + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1

        if n == 15:
            if x < min_x:
                min_x = x

print(min_x)

# Известно, что при вводе некоторых положительных значений переменных s и x данная программа выводит число 15.
# Определите, при каком наименьшем введённом значении переменной x это возможно.
