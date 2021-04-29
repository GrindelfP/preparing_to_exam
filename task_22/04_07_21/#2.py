P = 16
S = 10*P
K = 0
while P < S:
    K = K + 1
    S = S - 2 * K
    P = P + K
print(K)