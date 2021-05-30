def f(n):
    if n < 3:
        return n + 1
    elif (n >= 3) and (n % 2 == 0):
        return n+2*f(n+2)
    elif (n >= 3) and (n % 2 == 1):
        return f(n-2)+n-2


count = 0
for n in range(1, 1000):
    result = f(n)
    while result > 0:
        result = result // 10
        count = count + 1
    if count == 3:
        print(count)
