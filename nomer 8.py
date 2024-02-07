def sum_of_digits(n):
    return sum(map(int, str(n)))
numbers = input("Enter numbers:").split()
max_sum = max(sum_of_digits(int(num)) for num in numbers)
max_sum_numbers = [num for num in numbers if sum_of_digits(int(num)) == max_sum]
print("Answer is:", *max_sum_numbers)
