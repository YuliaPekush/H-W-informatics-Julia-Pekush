x = int(input('Enter the number:'))
a = 0
while x > 0:
    a += x % 10
    x //= 10
print('The summ:', a)
