# solution one:


# def div_count(number) -> bool:
#    div_quantity = 0
#    result = False
#    for u in range(1, number):
#        if number % u == 0:
#            div_quantity += 1
#        if div_quantity == 17:
#            result = True
#            break

#    return result


# count = 0
# min_good = 0

# for i in range(10001, 50001):
#    if div_count(i):
#        count += 1
#        new_min_good = i
#        if min_good == 0 or new_min_good < min_good:
#            min_good = new_min_good

# print(count, min_good)


# solution two:

count = 0
min_good = 0
div_count = 0

for i in range(10001, 50001):
    for u in range(1, i):
        if i % u == 0:
            div_count += 1
    if div_count > 17:
        count += 1
    new_min_good = i
    if min_good == 0 or new_min_good < min_good:
        min_good = new_min_good

print(count, min_good)
