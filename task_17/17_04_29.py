# # 1
# k = 0
# max = 0
# for i in range(8812, 12286):
#     if (i % 8 == 0 or i % 19 == 0) and (i % 4 != 0 and i % 9 != 0 and i % 14 != 0 and i % 16 != 0):
#         k = k + 1
#         max = i
#
# print(k, max)


# # 2
# k = 0
# min = 10415
# for i in range(4668, 10415):
#     if (i % 3 == 0 or i % 11 == 0) and (i % 2 != 0 and i % 13 != 0 and i % 22 != 0 and i % 33 != 0):
#         k = k + 1
#         if i < min:
#             min = i
#
# print(k, min)


# 3
k = 0
min = 10415
for i in range(1740, 14455):
    if (i % 4 == 0 and i % 5 == 0) and (i % 8 != 0 and i % 12 != 0 and i % 16 != 0 and i % 30 != 0):
        k = k + 1
        if i < min:
            min = i

print(k, min)
