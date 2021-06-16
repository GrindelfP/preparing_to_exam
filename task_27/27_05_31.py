k29 = 0
counter = 0
buffer = []

n = int(input())
for i in range(0, 5):
    buffer.append(int(input()))

for i in range(5, n):
    if buffer[0] % 19 == 0:
        counter = counter + 1

        x = int(input())
        if x % 29 == 0:
            counter = counter + (i - 5 + 1)
        else:
            counter = counter + k29
        for j in range(0, 4):
            buffer[j] = buffer[j + 1]
            buffer[4] = x

print(counter)
