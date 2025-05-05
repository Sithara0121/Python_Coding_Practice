try:
    pass
    # Code that may raise an exception
except ExceptionType as e:
    # Code that runs if an exception occurs
    print(f"An error occurred: {e}")
else:
    # Code that runs if no exception occurs
    print("No errors occurred.")
finally:
    # Code that always runs (clean-up code, e.g., closing files)
    print("Execution completed.")

#Example 1: Division by Zero (ZeroDivisionError)

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: division by zero
#Example 2: Handling File Not Found (FileNotFoundError)
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  # Output: [Errno 2] No such file or directory: 'non_existent_file.txt'
#Example 3: Handling ValueError (Invalid Conversion)
try:
    num = int("abc")  # This will raise a ValueError because 'abc' cannot be converted to an integer
except ValueError as e:
    print(f"Error: {e}")  # Output: invalid literal for int() with base 10: 'abc'
#Example with try-except-else-finally:
try:
    number = int(input("Enter a number: "))  # Get input from the user
    result = 10 / number  # Perform division
except ZeroDivisionError as e:
    print(f"Error: Cannot divide by zero. {e}")
except ValueError as e:
    print(f"Error: Invalid input. Please enter a valid number. {e}")
else:
    print(f"Result: 10 divided by {number} is {result}")
finally:
    print("Execution completed.")  # This will always run, regardless of whether an exception occurred or not
#Example Code for Exception Handling:
# --- Exception Handling in Python ---

# Example 1: ZeroDivisionError
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: division by zero

# Example 2: FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")  # Output: [Errno 2] No such file or directory: 'non_existent_file.txt'

# Example 3: ValueError (invalid integer conversion)
try:
    num = int("abc")  # This will raise a ValueError because 'abc' cannot be converted to an integer
except ValueError as e:
    print(f"Error: {e}")  # Output: invalid literal for int() with base 10: 'abc'

# Example 4: Handling multiple exceptions
try:
    number = int(input("Enter a number: "))  # Get input from the user
    result = 10 / number  # Perform division
except ZeroDivisionError as e:
    print(f"Error: Cannot divide by zero. {e}")
except ValueError as e:
    print(f"Error: Invalid input. Please enter a valid number. {e}")
else:
    print(f"Result: 10 divided by {number} is {result}")
finally:
    print("Execution completed.")  # This will always run, regardless of whether an exception occurred or not
