# WHILE LOOP = execute some code WHILE some condition remains TRUE

# Name input
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

# Age input with validation
age = input("Enter your age: ")

while age == "" or not age.isdigit() or int(age) < 0:
    if age == "":
        print("You did not enter your age")
    elif not age.isdigit():
        print("Please enter a valid number")
    elif int(age) < 0:
        print("Age can't be negative")
    age = input("Enter your age: ")

age = int(age)
print(f"You are {age} years old")

# Food loop
food = input("Enter a food you like (q to quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")