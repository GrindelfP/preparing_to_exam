count = 0
min_good = []


for i in range(6391, 8185):
    if (i % 11 == 3) and (i % 17 == 11) and (i % 2 != 0) and (i % 13 != 0) and (i % 14 != 0) and (i % 34 != 0):
        count = count + 1
        min_good.append(i)
print(count, min_good[0])
