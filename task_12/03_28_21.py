for i in range (50, 100):
    string_1 = "1"*i
    string = "1"*i

    while "111" in string:
        string = string.replace("111", "2", 1)
        string = string.replace("222", "1", 1)

    if string == "22":
        print(string_1.count("1"))
