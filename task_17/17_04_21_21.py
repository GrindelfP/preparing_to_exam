def isprime(n) -> bool:
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


count = 0
minim = 50001
steps = 0

for i in range(10001, 50001):
    for u in range(1, i):
        steps += 1
        print(steps)
        if i % u == 0 and isprime(u):
            print("here")
            count += 1
        if u < minim:
            minim = u

print(count, minim)
