with open("materials/24_05_11_21.txt", "r") as file:
    string = file.readline()
    counter = 0
    counter_max = 0
    for i in range(1, len(string)):
        if string[i] != "Y" and string[i - 1] != "Z" and string[i - 2] != "Z" and string[i - 3] != "X":
            counter = counter_max + 1
            if counter > counter_max:
                counter_max = counter


print(counter_max)

# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди
# которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
