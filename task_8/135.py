alphabet = "запись"
alphabet_2 = "запис"
F = 0

for i in alphabet_2:
    for j in alphabet:
        for k in alphabet:
            for l in alphabet:
                for m in alphabet:
                        t = i + j + k + l + m
                        if (t.find("аь") and t.find("иь")) == 0:
                            F += 1

print(F)
