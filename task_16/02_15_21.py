def F(n):
    if n > 15:
        return n * n - 5
    elif n <= 15:
        return n * F(n + 2) + n * F(n + 3)
    # elif (n <= 30) and (n % 2 == 1):
    #     return 2 * F(n+2) + F(n+5)


# def G(n):
#     if n == 1:
#         return n
#     # elif (n > 3) and (n % 2 == 0):
#     #     return n + 3 + F(n - 1)
#     elif n > 1:
#         return F(n - 1) + 2 * G(n - 1)


print(F(1))
print(5 + 0 + 6 + 0 + 1 + 9 + 9 + 2 + 7 + 8)
result = F(1)
summary = 0
while result > 0:
    power = result % 10
    summary += power
    result = (result - power) / 10

print(summary)

# F = 0
# summary = 0
# for n in range(1, 1000):
#     result = F(n)
#     while result >= 1:
#         power = result % 10
#         summary += power
#         result = (result - power) / 10
#
#     if summary == 27:
#         F += 1
#
# print(F)
