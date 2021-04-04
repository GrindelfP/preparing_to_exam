string = "0"+"1"*15+"2"*10+"3"*60

while "30" in string or "101" in string or "202" in string:
    string = string.replace("30", "01", 1)
    string = string.replace("101", "02", 1)
    string = string.replace("202", "03", 1)

print(string)
