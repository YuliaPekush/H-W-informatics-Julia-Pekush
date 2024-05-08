def count_zeros():
    result = 64 * 3**19

    ternary_result = ""
    while result > 0:
        ternary_result = str(result % 3) + ternary_result
        result //= 3

    zero_count = ternary_result.count("0")

    return zero_count

print("Кол-во нулей:", count_zeros())
