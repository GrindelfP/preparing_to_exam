def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif (n <= 30) and (n % 2 == 0):
        return f(n + 1) + 3 * f(n + 4)
    elif (n <= 30) and (n % 2 == 1):
        return 2 * f(n + 2) + f(n + 5)


count = 0
summary = 0
for n in range(1, 1000):
    result = f(n)
    while result > 0:
        countable = result % 10
        summary = summary + countable
        result = result // 10
        print(summary)
        if summary == 27:
            count += 1

print(count)

# summary = 0
# result = 123
# count = 0
# while result > 0:
#     countable = result % 10
#     summary = summary + countable
#     result = result // 10
# if summary == 6:
#     count += 1
#
# print(summary, count)
