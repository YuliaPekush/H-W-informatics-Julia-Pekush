def from_octal(octal_str):
    return int(octal_str, 8)
def from_base_37(base_37_str):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZa'
    return sum(alphabet.index(c) * (37 ** i) for i, c in enumerate(reversed(base_37_str)))
def from_ternary(ternary_str):
    return int(ternary_str, 3)
def from_base_15(base_15_str):
    return int(base_15_str, 15)
def to_base_24(number):
    alphabet = '0123456789ABCDEFGHIJKLMN'
    if number < 24:
        return alphabet[number]
    else:
        return to_base_24(number // 24) + alphabet[number % 24]

result = from_octal('105') + from_base_37('5F') * from_ternary('1011') ** from_base_15('BA')
result_in_base_24 = to_base_24(result)
count_H = result_in_base_24.count('H')
print("Result:", {count_H})
    
