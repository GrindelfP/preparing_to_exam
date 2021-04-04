for n in range(1, 1000):
    def F(n):
        if n == 0:
            return 0
        elif n > 0 and n % 2 == 0:
            return n / 2
        elif n > 0 and n % 2 == 1:
            return 1 + F(n - 1)


    if F(n) == 12:
        print(n)
