count = 0
max_good = 0

for i in range(2050, 9166+1):
    if i % 7 == 0 and i % 13 != 0 and i % 14 != 0 and i % 19 != 0 and i % 22 != 0:
        count += 1
        max_good = i

print(count, max_good)
