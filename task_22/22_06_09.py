for i in range(6, 1001):
    x = i
    a = 3*x + 23
    b = 3*x - 17
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    if a == 10:
        print(x)

