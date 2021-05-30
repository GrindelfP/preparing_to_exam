count = 0
summary = ""
max_good = None

for i in range(2095, 19403):
    i_less = i // 10
    i_str = str(i)
    if i % 10 == 1:
        if i_less % 10 == 2 and int(i_str[0]) > (i - i_less * 10):
            new_i = i
            count = count + 1
            max_good = i

print(count, max_good)
