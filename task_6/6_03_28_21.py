for d in range (1, 200):
    d1 = d
    n = 0
    s = 24
    while s <= 1318:
        s = s + d1
        n = n + 15
    if n == 195:
        print(d1)
