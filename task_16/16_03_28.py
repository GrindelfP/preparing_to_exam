# F(n) = 1, при n £ 1,
#
# F(n) = 3 + F(n / 2 – 1), когда n > 1 и чётное,
#
# F(n) = n + F(n + 2) , когда n > 1 и нечётное.

def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return 3 + F(n / 2 - 1)
    elif n > 1 and n % 2 == 1:
        return n + F(n + 2)


for n in range(1, 1000):
    if F(n) == 19:
        print(n)
