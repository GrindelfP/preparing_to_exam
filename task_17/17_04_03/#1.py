count = 0
max_good = 0

for i in range(9913, 13894+1):
    if i % 7 == 0 and i % 3 == 0 and i % 4 != 0 and i % 17 != 0 and i % 23 != 0 and i % 42 != 0:
        count += 1
        max_good = i

print(count, max_good)
