def ok(x):
    for i in range(5):
        if x[i] == x[i + 1]:  # соседние буквы д.б. разными
            return False
        else:
            return True


from itertools import permutations

s = 'кабала'
# множество удаляет повторяющиеся перестановки
# (из-за двух 'а' и двух 'к' в s)
m = {x for x in permutations(s) if ok(x)}
print(len(m))
