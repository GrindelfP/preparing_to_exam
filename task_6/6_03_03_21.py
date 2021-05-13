for s in range(0, 1000):
    s_1 = s
    n = 100
    while s_1 - n >= 100:
        s_1 = s_1 + 20
        n = n + 40
    if s_1 != s:
        print(s)
        break
