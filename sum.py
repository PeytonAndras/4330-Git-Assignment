# prompt the user to enter numbers separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# split the numbers into a list
number_list = numbers.split()

# initialize the sum
sum = 0

# iterate over the list of numbers and add them to the sum
for num in number_list:
    sum += int(num)

# Print the sum
print("The sum is:", sum)