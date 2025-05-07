# --- Dictionaries in Python ---

# Creating a dictionary with key-value pairs
person = {
    "name": "Alice",    # key: "name", value: "Alice"
    "age": 30,          # key: "age", value: 30
    "city": "New York"  # key: "city", value: "New York"
}

print("Original dictionary:", person)  # Prints the dictionary

# Accessing values by key
print("Name:", person["name"])  # Accesses the value for key "name"
print("Age:", person["age"])    # Accesses the value for key "age"

# Adding a new key-value pair to the dictionary
person["email"] = "alice@example.com"  # Adding a new key "email" with value
print("Updated dictionary with new email:", person)

# Modifying an existing value
person["age"] = 31  # Updating the value for key "age"
print("Modified dictionary with updated age:", person)

# Removing a key-value pair using 'del'
del person["city"]  # Removes the key "city" and its associated value
print("Dictionary after removing 'city':", person)

# Using the get() method (safe way to access a value)
# Returns the value if the key exists, otherwise returns the default value ("Not available" here)
print("City:", person.get("city", "Not available"))  # Default message when "city" doesn't exist

# Checking if a key exists in the dictionary
if "age" in person:  # Checks if "age" is a key in the dictionary
    print("Age is in the dictionary.")

# Length of the dictionary (returns number of key-value pairs)
print("Length of dictionary:", len(person))  # Returns the number of key-value pairs

# Iterating through keys and values using .items()
print("Iterating through the dictionary:")
for key, value in person.items():  # Iterates through key-value pairs in the dictionary
    print(key, ":", value)  # Prints each key-value pair


# --- Empty Dictionary Example ---

# Create an empty dictionary using curly braces or dict() constructor
empty_dict1 = {}         # Empty dictionary using {}
empty_dict2 = dict()     # Empty dictionary using dict()

# Check if both dictionaries are empty
print("\nIs empty_dict1 empty?", not empty_dict1)  # Checks if the dictionary is empty
print("Is empty_dict2 empty?", not empty_dict2)  # Checks if the dictionary is empty

# Add key-value pairs to the empty dictionaries
empty_dict1["name"] = "Alice"  # Adds key "name" with value "Alice"
empty_dict2["age"] = 30        # Adds key "age" with value 30

# Print the dictionaries after adding items
print("empty_dict1 after adding item:", empty_dict1)  # Prints the updated dictionary
print("empty_dict2 after adding item:", empty_dict2)  # Prints the updated dictionary


# --- Nested Dictionaries ---

# Nested dictionary (dictionary within a dictionary)
people = {
    "Alice": {   # Key "Alice" maps to a dictionary
        "age": 30, 
        "city": "New York"
    },
    "Bob": {     # Key "Bob" maps to a dictionary
        "age": 25,
        "city": "Los Angeles"
    }
}

# Accessing nested dictionary values
print("\nAlice's information:", people["Alice"])  # Prints Alice's sub-dictionary
print("Bob's city:", people["Bob"]["city"])  # Prints Bob's city by accessing nested dictionary


# --- Dictionary Comprehensions ---

# Creating a dictionary using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}  # Creates a dictionary with numbers as keys and squares as values
print("\nSquares of numbers using comprehension:", squares)

# Filtering with a condition in dictionary comprehension
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}  # Filters to only include even numbers
print("Even squares:", even_squares)  # Prints the dictionary with even squares


# --- More Dictionary Methods ---

# Dictionary with some values
my_dict = {"a": 1, "b": 2, "c": 3}  # Simple dictionary with keys "a", "b", "c"

# Keys: Returns all the keys in the dictionary
print("\nKeys:", my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# Values: Returns all the values in the dictionary
print("Values:", my_dict.values())  # Output: dict_values([1, 2, 3])

# Items: Returns all key-value pairs as tuples
print("Items:", my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Popping an item (removes and returns an item by key)
popped_item = my_dict.pop("b")  # Removes and returns the item for key "b"
print("Popped item:", popped_item)  # Output: 2
print("Dictionary after pop:", my_dict)  # Output: {'a': 1, 'c': 3}

# Clearing all items in the dictionary
my_dict.clear()  # Clears all the items in the dictionary
print("Dictionary after clear:", my_dict)  # Output: {}
