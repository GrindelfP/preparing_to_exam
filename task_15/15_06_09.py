def task15(A, x) -> bool:
    return (x & 49 == 0) <= ((x & 28 != 0) <= (x & A != 0))


for A in range(1, 1000):
    fitting = True
    for x in range(1, 1000):
        if task15(A, x) == 0:
            fitting = False
            break

    if fitting:
        print(A)

"""Для какого наименьшего неотрицательного целого числа А формула
x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
тождественно истинна?"""
