# 1
def f(n):
    if n > 2:
        return f(n - 1) + f(n - 2)
    else:
        return 1


print(f(5))


# 2
def F(n):
    if n > 2:
        return F(n-1)+G(n-1)+F(n-2)
    else:
        return n


def G(n):
    if n > 2:
        return G(n-1)+F(n-1)+G(n-2)
    else:
        return n+1


print(G(5))


# 3
def f(n):
    if n <= 2:
        return 2
    elif n > 2:
        return f(n - 1) + 3 * f(n - 2)


print(f(5))
