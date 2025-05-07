# --- File Handling in Python ---

# Writing to a file (overwrites the file if it exists)
# The 'with' statement automatically closes the file after the block of code is executed.
with open("example.txt", "w") as file:
    file.write("This is the first line in the file.\n")  # Writing first line
    file.write("This is the second line.\n")  # Writing second line
    file.write("Python file handling is easy!\n")  # Writing third line

# Reading from the file
# Using 'with' ensures that the file is closed once done reading.
with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire content of the file
    print("File content:")
    print(content)  # Output: The content written earlier

# Appending data to the file
# Opens the file in append mode, so it adds new content at the end.
with open("example.txt", "a") as file:
    file.write("This is the appended line.\n")  # Adds a new line at the end of the file

# Reading line by line from the file
# Using a for loop to iterate through each line in the file
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end of each line

# Checking if the file exists and handling errors (using try-except)
# We try to open a file that doesn't exist to demonstrate error handling.
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")  # This will print if the file does not exist.
