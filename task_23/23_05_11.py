def minor(x, f):
    if x == f:
        return 1
    elif x < f:
        return 0
    elif x > f:
        return minor(x - 2, f) + minor(x - 5, f)


print(minor(23, 2))

# Исполнитель Минус преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Вычесть 2
# 2. Вычесть 5
# Первая команда уменьшает число на экране на 2, вторая уменьшает это число на 5.
# Программа для исполнителя Минус – это последовательность команд.
# Сколько существует программ, которые число 23 преобразуют в число 2?
