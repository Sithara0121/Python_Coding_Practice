# --- Lists in Python ---

# Creating a list
my_list = [1, 2, 3, "hello", 4.5, True]
print("Original list:", my_list)

# Accessing elements by index
print("First element:", my_list[0])  # Output: 1
print("Fourth element:", my_list[3])  # Output: hello

# Slicing a list
print("Slice of list (1 to 4):", my_list[1:4])  # Output: [2, 3, 'hello']

# Modifying an element in the list
my_list[1] = 20
print("Modified list:", my_list)

# Adding an element to the list
my_list.append(100)
print("List after appending 100:", my_list)

# Inserting an element at a specific position
my_list.insert(2, "Python")
print("List after inserting 'Python' at index 2:", my_list)

# Removing an element by value
my_list.remove("hello")
print("List after removing 'hello':", my_list)

# Popping an element (removes and returns an item from the list)
popped_element = my_list.pop()
print("Popped element:", popped_element)  # Output: 100
print("List after pop:", my_list)

# Length of the list
print("Length of the list:", len(my_list))

# --- Tuples in Python ---

# Creating a tuple
my_tuple = (1, 2, 3, "hello", 4.5, True)
print("\nOriginal tuple:", my_tuple)

# Accessing elements by index
print("First element of tuple:", my_tuple[0])  # Output: 1
print("Fourth element of tuple:", my_tuple[3])  # Output: hello

# Slicing a tuple
print("Slice of tuple (1 to 4):", my_tuple[1:4])  # Output: (2, 3, 'hello')

# Length of the tuple
print("Length of the tuple:", len(my_tuple))

# --- List Comprehension in Python ---

# List comprehension: Squaring each number in a list
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print("\nSquares of numbers:", squares)  # Output: [1, 4, 9, 16, 25]

# List comprehension with condition: Get even numbers only
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [2, 4]

# --- Nested Lists and Tuples ---

# Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
print("\nNested List:", nested_list)
print("First element of nested list:", nested_list[0])  # Output: [1, 2]
print("Second element of first sublist:", nested_list[1][0])  # Output: 3

# Nested Tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested_tuple)
print("Second element of nested tuple:", nested_tuple[1])  # Output: (3, 4)
