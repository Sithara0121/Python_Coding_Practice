# --- Sets in Python ---
# A set in Python is an unordered collection of unique elements. Sets are 
# similar to lists or dictionaries, but unlike lists, they do not allow duplicate values. 
# Sets are useful when you need to store a collection of items and do not want any duplicates.

# Key Properties of Sets:
# Unordered: Sets do not maintain the order of elements.

# Unique: Sets do not allow duplicate elements.

# Mutable: You can add or remove elements from a set.
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)  # Adds 6 to the set
print("Set after adding 6:", my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from the set
my_set.remove(2)  # Removes 2 from the set
print("Set after removing 2:", my_set)  # Output: {1, 3, 4, 5, 6}

# Using discard() (won't raise an error if element is not found)
my_set.discard(10)  # 10 is not in the set, no error raised
print("Set after discard 10:", my_set)  # Output: {1, 3, 4, 5, 6}

# Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Union of set1 and set2
print("Union of set1 and set2:", union_set)  # Output: {1, 2, 3, 4, 5}

# Set Intersection
intersection_set = set1 & set2  # Intersection of set1 and set2
print("Intersection of set1 and set2:", intersection_set)  # Output: {3}

# Set Difference
difference_set = set1 - set2  # Elements in set1 but not in set2
print("Difference between set1 and set2:", difference_set)  # Output: {1, 2}

# Set Comprehension (Squaring numbers)
squares = {x**2 for x in range(1, 6)}  # Set of squares of numbers 1 to 5
print("Squares of numbers:", squares)  # Output: {1, 4, 9, 16, 25}

# Checking membership in a set
print(3 in my_set)  # Output: True (3 is in my_set)
print(10 in my_set)  # Output: False (10 is not in my_set)
