x = float(input("Введите число: "))
if x.is_integer():
    l = int(x) % 10
else:
    x_str = str(x)
    d = x_str.split(".")[1]
    l = int(d[-1])
print("Последняя цифра числа:", l)
