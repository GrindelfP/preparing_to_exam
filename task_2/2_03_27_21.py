for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((not (b <= a) and (c <= d)) != (a and b and c and not d)) == 1:
                    print(a, b, c, d)
