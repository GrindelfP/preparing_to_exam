summ = 0
max_good = 0


for i in range(3394, 8600):
    if (i % 3 == 1) and (i % 7 == 5):
        summ = summ + i
        print(summ)
        max_good = i

print(summ, max_good)
