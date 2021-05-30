k2 = k31 = k62 = 0
n = int(input())
for i in range(0, n):
    x = int(input())

    if x % 62 == 0:
        k62 = k62 + 1

    elif x % 31 == 0:
        k31 += 1

    elif x % 2 == 0:
        k2 += 1

s = k2 * k31 + k62*(n - k62) + k62*(k62 - 1) // 2

print(s)