# format specifiers =  {value:flags} format a value based on what flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 1200.34

print(f"Price 1 is ${price1:.2f}")       # decimal precision (2 digits)
print(f"Price 1 is ${price1:.1f}")       # decimal precision (1 digit)

print("\n")

print(f"Price 1 is ${price1:10}")        # 10 spaces to display the output
print(f"Price 1 is ${price1:<10}")       # left justified
print(f"Price 1 is ${price1:>10}")       # right justified
print(f"Price 1 is ${price1:^10}")       # center

print("\n")

print(f"Price 1 is ${price1:+}")         # prefix sign of the number
print(f"Price 2 is ${price2:+}")         # prefix sign of the number
print(f"Price 3 is ${price3:+}")         # prefix negative number
print(f"Price 3 is ${price3:,}")         # separetes thousands place