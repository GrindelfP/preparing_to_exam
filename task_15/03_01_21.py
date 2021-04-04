# def div(f_n, s_n) -> bool:
#     division = f_n % s_n
#     if division == 0:
#         return True
#     else:
#         return False
#
#
def task15(x, A) -> bool:
    return (x and 29 != 0) <= ((x and 17 == 0) <= (x and A != 0))


# (X & 29 ¹ 0) ® ((X & 17 = 0) ® (X & A ¹ 0
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
