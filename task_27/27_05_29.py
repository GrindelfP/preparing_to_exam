r0 = r1 = r2 = r3 = r4 = r5 = 0

n = int(input())

for i in range(0, n):
    x = int(input())
    if x % 6 == 0:
        r0 = r0 + 1
    if x % 6 == 1:
        r1 = r1 + 1
    if x % 6 == 2:
        r2 = r2 + 1
    if x % 6 == 3:
        r3 = r3 + 1
    if x % 6 == 4:
        r4 = r4 + 1
    if x % 5 == 0:
        r5 = r5 + 1

s = n*(n-1)//2 - (r2*r4 + r1*r5 + r0*(r0-1)//2 + r3*(r3-1)//2)

print(s)
