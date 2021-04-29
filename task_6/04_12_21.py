for i in range(0, 1000):
    s = i
    s = 10*s + 5
    n = 1
    while s < 2021:
        s = s + 2*n
        n = n + 1
    if n == 11:
        print(i)

