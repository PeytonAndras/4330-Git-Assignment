# take input from the user
n = int(input("Enter the number of terms: "))

# initialize the first two terms of the sequence
fibonacci_sequence = [0, 1]

# generate the Fibonacci sequence
for i in range(2, n):
    next_term = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(next_term)

# print the Fibonacci sequence
print("Fibonacci sequence:")
for term in fibonacci_sequence:
    print(term)