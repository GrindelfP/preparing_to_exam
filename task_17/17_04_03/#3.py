count = 0
min_good = 0

for y in range(3521, 13019+1):
    if y % 9 == 0 and y % 15 == 0 and y % 6 != 0 and y % 12 != 0 and y % 17 != 0 and y % 21 != 0:
        count += 1
        new_min_good_1 = y
        if min_good == 0 or new_min_good_1 < min_good:
            min_good = new_min_good_1

print(count, min_good)
