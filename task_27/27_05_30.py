rest = [0]*80

n = int(input())

for i in range(0, n):
    x = int(input())
    rest[x%80] = rest[x%80] + 1

summ = 0
for i in range(1, 40):
    summ = summ + rest[i]*rest[80-i]

fin_summ = rest[0]*(rest[0]-1)//2 + rest[40]*(rest[40]-1)//2 + summ

print(fin_summ)