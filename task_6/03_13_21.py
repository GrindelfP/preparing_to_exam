for s in range(0, 100):
    s1 = s
    s1 = (s1+1) // 7
    n = 36
    while s1 < 2050:
        s1 = s1 * 2
        n = n + 3
    if s1 != s:
        print(s)
        break
