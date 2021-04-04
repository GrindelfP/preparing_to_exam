def div_count(number) -> int:
    div_quantity = 0
    for i in range (1, 10):
        if number % i == 0:
            div_quantity += 1

    return div_quantity


print(div_count(8))
