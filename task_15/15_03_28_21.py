# (¬ДЕЛ(x, A) Ú ДЕЛ(x, 36) Ù ДЕЛ(x, 126)) Ù ( A > 10
def div(f_n, s_n) -> bool:
    division = f_n % s_n
    if division == 0:
        return True
    else:
        return False


def task15(x, A) -> bool:
    return (not div(x, A) or div(x, 36) and div(x, 126)) or (A > 1000)


for A in range(1000, 10000):
    flag = True
    for x in range(0, 100000):
        if not task15(x, A):
            flag = False
            break
    if flag:
        print(A)
