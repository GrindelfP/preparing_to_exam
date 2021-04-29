def div(f_n, s_n) -> bool:
    division = str(f_n % s_n)
    if division == 0:
        return True
    else:
        return False


def task15(x, A) -> bool:
    return div(A, 45) and (div(750, x) <= (not div(A, x) <= (not div(120, x))))


for A in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        if not task15(x, A):
            flag = False
            break

    if flag:
        print(A)
