def sum_numbers(numbers):
    total = sum(numbers)
    return total

# Get input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]

# Call the sum_numbers function with the user input
result = sum_numbers(numbers)
print(result)

