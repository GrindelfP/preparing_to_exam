for i in range(1, 1001):
    for x_1 in range(1, 1001):
        y = i
        x = x_1
        if y > x:
            z = x
            x = y
            y = z
        a = x
        b = y
        while b > 0:
            r = a % b
            a = b
            b = r
        if a == 11 and x == 66:
            print(y)
