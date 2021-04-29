# from ege_statgrad
# def find(x, f) -> int:
#     if x == f:
#         return 1
#     if x > f or x == 30:
#         return 0
#     if x < f:
#         return find(x+1, f) + find(x*2, f) + find(x*3, f)
#
#
# print(find(2, 12) * find(12,36))


# 127_Jobs
# def find(x, f) -> int:
#     if x == f:
#         return 1
#     if x > f:
#         return 0
#     if x < f:
#         return find(x*2, f) + find(x*3, f)
#
#
# print(find(8, 96) * find(96, 3456))


# 128_Jobs
# def find(x, f) -> int:
#     if x == f:
#         return 1
#     if x > f or x == 43:
#         return 0
#     if x < f:
#         return find(x+2, f) + find(x+x-1, f) + find(x+x+1, f)
#
#
# print(find(7, 63))


# 129_Jobs
def find(x, f) -> int:
    if x == f:
        return 1
    if x > f:
        return 0
    if x < f:
        return find(x+2, f) + find(x+3, f) + find(int("1"+str(x)), f)


print(find(3, 12) * find(12, 25))

