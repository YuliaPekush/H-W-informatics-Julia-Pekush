def convert_to_decimal(number_24):
    decimal_result = 0
    base = 24
    for digit in number_24:
        decimal_result = decimal_result * base + int(digit, base=base)
    return decimal_result
number_24 = input("Введите число в 24 системе счисления: ")
decimal_result = convert_to_decimal(number_24)
print(f"Результат в 10 системе: {decimal_result}")
