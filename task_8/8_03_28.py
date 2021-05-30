alphabet = "андрей"
F = 0
for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                for m in alphabet:
                    for n in alphabet:
                        t = i + j + k + l + m + n
                        if t.find("а") >= 1 and t.find("й") <= 1:
                            F += 1

print(F)
