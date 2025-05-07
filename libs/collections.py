# COLLECTION = a single "variable" used to store multiple values
#   List    = []  ordered and changeable. Duplicates allowed.
#   Set     = {}  unordered and immutable, but items can be added/removed. NO duplicates.
#   Tuple   = ()  ordered and unchangeable. Duplicates allowed. FASTER.



# --- List Operations ---
fruits = ["apple", "orange", "banana", "coconut"]

# Accessing elements
print(fruits[0])  # First element
print(fruits[1])  # Second element
print(fruits[0:3])  # Slice (from 0 to 2)

# Loop through the list
for fruit in fruits:
    print(fruit)

# List Methods:
fruits.append("grape")  # Add to the end
print(fruits)

fruits.remove("banana")  # Remove specific element
print(fruits)

fruits.insert(1, "kiwi")  # Insert at a specific index
print(fruits)

fruits.sort()  # Sort the list
print(fruits)

fruits.reverse()  # Reverse the list
print(fruits)

# --- Set Operations ---
fruits = {"apple", "orange", "banana", "coconut"}

# Display the set (order is not guaranteed)
print(fruits)

# Common Set Methods:
fruits.add("grape")  # Add an element
print(fruits)

fruits.remove("banana")  # Remove an element
print(fruits)

fruits.discard("kiwi")  # Remove an element safely (no error if not found)
print(fruits)

# Union, Intersection, and Difference operations:
another_set = {"pear", "orange", "grape"}
print(fruits.union(another_set))  # Union of two sets
print(fruits.intersection(another_set))  # Common items
print(fruits.difference(another_set))  # Items in fruits but not in another_set



# --- Tuple Operations ---
fruits = ("apple", "orange", "banana", "coconut")

# Accessing elements
print(fruits)
print("apple" in fruits)  # Check if "apple" is in the tuple

# Common Tuple Methods:
# Since tuples are immutable, they don't have methods like append/remove
# However, you can count occurrences or find an index:
print(fruits.count("apple"))  # Count occurrences of "apple"
print(fruits.index("banana"))  # Find the index of "banana"
