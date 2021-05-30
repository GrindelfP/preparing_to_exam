# ДЕЛ(A, 40) /\ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))

def task15(A, x) -> bool:
    return ((A % 40 == 0) and (780 % x == 0)) <= ((not A % x) <= (not 180 % x))


for A in range(1, 1000):
    fitting = True
    for x in range(1, 1000):
        if task15(A, x) == 0:
            fitting = False
            break

    if fitting:
        print(A)
