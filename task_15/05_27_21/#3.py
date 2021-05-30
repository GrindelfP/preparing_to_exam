def task15(x, A) -> bool:
    return (((x & 13 != 0) or (x & A != 0)) <= (x & 13 != 0)) or ((x & A != 0) and (x & 39 == 0))


for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not task15(x, A):
            flag = False
            break

    if flag:
        print(A)
