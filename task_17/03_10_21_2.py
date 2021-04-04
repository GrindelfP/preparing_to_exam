count = 0
count_common = 0
min_good = []

for i in range(10000, 20000):
    count = 0
    if i % 5 == 0:
        count = count + 1
    if i % 11 == 0:
        count = count + 1
    if i % 17 == 0:
        count = count + 1
    if i % 19 == 0:
        count = count + 1

    if count == 2:
        count_common = count_common + 1
        min_good.append(i)
print(count_common, min_good[0])
