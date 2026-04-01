import math

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)   # ❌ crash if list is empty

def find_max(numbers):
    max_val = 0   # ❌ wrong if all numbers are negative
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def divide(a, b):
    return a / b   # ❌ no zero division handling

def factorial(n):
    if n == 0:
        return 0   # ❌ incorrect, should be 1
    return n * factorial(n - 1)   # ❌ no negative input check

def process_data(data):
    result = []
    for item in data:
        if type(item) == int:   # ❌ bad type checking
            result.append(item * 2)
        else:
            result.append(item)
    return result

def read_file(filename):
    f = open(filename, "r")   # ❌
    data = f.read()
    return data

# Test execution
nums = []
print("Average:", calculate_average(nums))   # ❌ triggers error

print("Max:", find_max([-5, -10, -3]))       # ❌ wrong result

print("Divide:", divide(10, 0))              # ❌ crash

print("Factorial:", factorial(-3))           # ❌ infinite recursion

print("Processed:", process_data([1, "a", 3]))

print("File content:", read_file("test.txt"))  # ❌ may leak file handle
