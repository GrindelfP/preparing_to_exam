alphabet = "тимофе"
F = 0
for i in "тимофей":
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                for m in alphabet:
                    for n in alphabet:
                        t = i + j + k + l + m + n
                        if t.count("т") >= 1:
                            F += 1

print(F)
