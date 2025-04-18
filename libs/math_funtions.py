import math

x = 3.14
y = -4
z = 9

result = round(x)       # rounds the number
result = abs(y)         # absolute value of a number
result = pow(4, 2)      # "x to the power of y"
result = max(x, y, z)   # returns the maximum value
result = min(x, y, z)   # returns the minimum value

print(result)


# from now on these functions will only work if you implemented "math"
print(math.pi)
print(math.e)
result = math.sqrt(z)
result = math.ceil(x)   # rounds the number up
result = math.floor(x)  # rounds the number down