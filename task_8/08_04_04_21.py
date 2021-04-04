alphabet = "1234"
F = 0
for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                for m in alphabet:
                    t = i + j + k + l + m
                    if t.count("1") == 2:
                        F += 1

print(F)
