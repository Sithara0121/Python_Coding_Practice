# --- Data Types ---
# Integers
x = 10
print("Integer:", x)

# Floating Point Numbers
y = 3.14
print("Float:", y)

# Strings
name = "Alice"
print("String:", name)

# Booleans
is_active = True
print("Boolean:", is_active)

# --- Conditional Statements ---
# if, elif, else
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# --- Loops ---
# for loop
print("For loop output:")
for i in range(5):  # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)

# while loop
print("While loop output:")
i = 0
while i < 5:
    print(i)
    i += 1  # Increment i to avoid infinite loop

# break and continue
print("Using break and continue in loops:")
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)

# --- Functions ---
# Basic function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Function with return value
def add(a, b):
    return a + b

result = add(3, 4)
print("Add function result:", result)  # Output: 7

# Function with default argument
def multiply(a, b=2):
    return a * b

print(multiply(5))    # Output: 10 (uses default b=2)
print(multiply(5, 3)) # Output: 15 (uses provided b=3)

# Function with variable-length arguments (*args)
def sum_numbers(*args):
    return sum(args)

print("Sum of numbers:", sum_numbers(1, 2, 3, 4))  # Output: 10

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)  # Output: name: Alice, age: 30

# --- Scope of Variables ---
x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print("Inside function:", x)

my_function()  # Output: Inside function: 5
print("Outside function:", x)  # Output: Outside function: 10

# --- Lambda Functions ---
# Regular function
def square(x):
    return x * x

# Lambda function
square_lambda = lambda x: x * x

print("Square using regular function:", square(5))        # Output: 25
print("Square using lambda function:", square_lambda(5)) # Output: 25
