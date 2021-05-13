# ДЕЛ(70, A) /\ (ДЕЛ(x, 28) → (¬ДЕЛ(x, A) → ¬ДЕЛ(x, 21)))
def div(f_n, s_n) -> bool:
    division = f_n % s_n
    if division == 0:
        return True
    else:
        return False


def task15(x, A) -> bool:
    return div(70, A) and (div(x, 28) <= ((not div(x, A)) <= (not div(x, 21))))


for A in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not task15(x, A):
                flag = False
                break
        if not flag:
            break

    if flag:
        print(A)
