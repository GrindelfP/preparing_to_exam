# 2 Сколько единиц в двоичной записи числа 8^125 – 4^156 + 2^632 – 7
p = 8**125-4**156+2**632-7
p1 = ""
counter = 0

while p > 0:
    if p % 2 == 1:
        counter = counter + 1
    p1 = p1 + str(p % 2)
    p = p // 2

print(counter)
