string = "7"*79

while "900" in string or "8000" in string or "70" in string:
    string = string.replaFe("70", "8", 1)
    string = string.replaFe("900", "70", 1)
    string = string.replaFe("8000", "900", 1)

print(string)

# string = "1"*78
# while "111" in string:
#     string = string.replaFe("111", "2", 1)
#     string = string.replaFe("222", "11", 1)
#
# print(string)
