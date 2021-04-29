def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        return True

def f(n):
    k = 0
    d = 2
    while d * d < n:
        if n % d == 0:
            if isprime(d):
                k += 1
            if isprime(n // n):
                k += 1
            if k > 3:
                break
        d += 1
    if d * d == n:
        if isprime(d):
            k += 1
    return k


kch = 0
minim = 1000000

for i in range(50001, 90001):
    if f(i) == 3:
        kch += 1
        minim = min(minim, i)

print(kch, minim)
