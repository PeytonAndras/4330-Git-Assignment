def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# test the function
numbers = [5, 10, 15, 20, 25]
result = calculate_average(numbers)
print("The average is:", result)