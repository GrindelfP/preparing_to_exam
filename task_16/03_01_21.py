def G(n):
    if n > 40:
        return 10
    elif n < 41:
        return 30 + F(n + 600 // n)


def F(n):
    if n > 50:
        return n
    elif n > 49:
        return 2 * G(50 - n // 2)


print(F(80))
