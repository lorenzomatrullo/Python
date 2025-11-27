# Lists of grocery items
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# Two ways to define the groceries list
groceries = [fruits, vegetables, meats]
groceries1 = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]

# Printing the contents of the grocery lists
# Fruits
print(groceries[0])          # Output: ['apple', 'orange', 'banana', 'coconut']
print(groceries[0][0])       # Output: 'apple'
print(groceries[0][1])       # Output: 'orange'
print(groceries[0][2])       # Output: 'banana'
print(groceries[0][3])       # Output: 'coconut'

# Vegetables
print(groceries[1])          # Output: ['celery', 'carrots', 'potatoes']
print(groceries[1][0])       # Output: 'celery'
print(groceries[1][1])       # Output: 'carrots'
print(groceries[1][2])       # Output: 'potatoes'

# Meats
print(groceries[2])          # Output: ['chicken', 'fish', 'turkey']
print(groceries[2][0])       # Output: 'chicken'
print(groceries[2][1])       # Output: 'fish'
print(groceries[2][2])       # Output: 'turkey'

print("\nPrinting all the categories together:")
for collection in groceries:
    print(collection)


print("\nPrinting all the foods together:")
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()