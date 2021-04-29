def find(x, f):
    if x == f:
        return 1
    if x > f or x == 30:
        return 0
    if x < f:
        return find(x + 1, f) + find(x * 2, f) + find(x * 3, f)


print(find(2, 13) * find(13, 39))
