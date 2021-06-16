def distance_counter(operated_letter, operated_line):
    distance_between_letters = 0
    counter = []
    for letter in operated_line:
        if letter == operated_letter:
            index = operated_line.index(letter)
            counter.append(index)
            operated_line = operated_line.replace(letter, "-", 1)
            distance_between_letters = max(counter) - min(counter)

    return distance_between_letters


def sofar_3(operated_line):
    distances = [0]*26
    for letter in operated_line:
        if operated_line.count(letter) > 1:
            distance = distance_counter(operated_letter=letter, operated_line=operated_line)
            ascii_code_letter = ord(letter)
            distances[ascii_code_letter - ord("A")] = distance

    max_len = max(distances)

    return max_len


max_distance = 0
with open("materials/24_06_09.txt") as file:
    for line in file:
        if line.count("G") < 25:
            if sofar_3(operated_line=line) > max_distance:
                max_distance = sofar_3(operated_line=line)

print(max_distance)

"""Текстовый файл содержит строки различной длины. Общий объём файла не
превышает 1 Мбайт. Строки содержат только заглавные буквы латинского
алфавита (ABC…Z).
В строках, содержащих менее 25 букв G, нужно определить и вывести
максимальное расстояние между одинаковыми буквами в одной строке
Пример. Исходный файл:
GIGA
GABLAB
NOTEBOOK
AGAAA
В этом примере во всех строках меньше 25 букв G. Самое большое
расстояние между одинаковыми буквами – в третьей строке между буквами
O, расположенными в строке на 2-й и 7-й позициях. В ответе для данного
примера нужно вывести число 5."""
