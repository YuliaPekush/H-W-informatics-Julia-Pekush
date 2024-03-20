def average_from_input():
    values = []

    while True:
        value = input("Введите значение (или нажмите Enter еще раз для запуска расчета: ")
        if value == "":
            break

        try:
            value = float(value)
            values.append(value)
        except ValueError:
            print("Ошибка, введено некорректное значение, введите число.")

    if not values:
        return 0

    total = sum(values)
    return total / len(values)

result = average_from_input()
print("Среднее арифметическое введенных значений:", result)

    
