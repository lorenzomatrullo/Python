# CONDITIONAL EXPRESSIONS (ternary operators) = shortcut to if/else statement when assigning/returning a value

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)