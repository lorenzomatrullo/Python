# dictionary = a collection pof {key:value} pairs
#              ordered and changeable. No Duplicates

# Define a dictionary called 'capitals' with countries as keys and capitals as values
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# Use the .get() method to retrieve the capital of the USA
print(capitals.get("USA"))

# Check if the capital of Russia exists in the dictionary
if capitals.get("Russia"):
    print("The capital exists")
else:
    print("That capital doesn't exist")

# Update the dictionary with a new country and its capital
capitals.update({"Germany": "Berlin"})

# Update the capital of the USA (change it from Washington D.C. to Detroit)
capitals.update({"USA": "Detroit"})


# Remove the entry for China from the dictionary
capitals.pop("China")


# Remove the last item added to the dictionary
capitals.popitem()


# Clear all items in the dictionary (empties the dictionary)
capitals.clear()


# Retrieve all the keys in the dictionary (returns a view object)
keys = capitals.keys()

for key in capitals.keys():
    print(key)


# Retrieve all the values in the dictionary (returns a view object)
values = capitals.values()

for value in capitals.values():
    print(value)


# Retrieve all key-value pairs in the dictionary as tuples
items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")