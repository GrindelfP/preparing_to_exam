min_x = 10000
for i in range(1, 10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        M = M + 1
        if x % 2 != 0:
            L = L + 1
        x = x // 2
    if L == 5 and M == 8:
        if i < min_x:
            min_x = i

print(min_x)

# Укажите наименьшее число x, при вводе которого алгоритм печатает сначала 5, а потом 8.
