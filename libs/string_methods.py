name = input("Enter your full name: ")

result = len(name)              # length
result = name.find("o")         # returns the 1st occurence of a given character
result = name.rfind("o")        # returns the last occurence of a given character
name = name.capitalize()        # returns the 1st letter capitalized
name = name.upper()             # makes all the letters uppercase
name = name.lower()             # makes all the letters lowercase
result = name.isdigit()         # returns TRUE or FALSE if the string ONLY contains digits
result = name.isalpha()         # returns TRUE or FALSE if the string ONLY contains alphabetical characters
result = name.count("o")        # returns how many occurences of the provided character
result = name.replace("o", "e") # replaces the 1st given character with the second


print(result)
print(name)

print(help(str))                # returns all the string methods available