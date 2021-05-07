# ege_statgrad_2010401
from collections import Counter


def find_less_G(string) -> int:
    frequency = []
    for line in string:
        let_count = line.count("G")
        frequency.append(let_count)
    index = frequency.index(min(frequency))

    return index


def find_most_occur_let(position, lines) -> str:
    doc = []
    alfabeth = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    counters = []
    for line in lines:
        doc.append(line)
    string = doc[position]
    list_of_letters = list(Counter(string))
    for i in list_of_letters:
        if i is int:
            counters.append(i)
    max_occur = max(counters)
    num_of_max_occur = counters.count(max_occur)

    return


with open("materials/24.txt", "r") as file:
    index_of_less_G = find_less_G(file)
    most_occur_let = find_most_occur_let(index_of_less_G, file)
