# 77
with open("materials/k8-1.txt", "r") as file:
    string = file.readline()
    k = 1
    k_max = 1
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            k = k + 1
            if k > k_max:
                k_max = k
        else:
            k = 1

print(k_max)


# 133
with open("materials/24-j2.txt", "r") as file:
    string = file.readline()
    k = 1
    k_max = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            k = k + 1
            if k > k_max:
                k_max = k
        else:
            k = 1

print(k_max)
