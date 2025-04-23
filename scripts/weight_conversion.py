# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (KG or Lbs): ").lower()  # prevent uppercase/lowercase

if unit == "kg":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "lbs":
    weight = weight / 2.205
    unit = "KG"
else:
    print(f"{unit} was not valid")
    exit()  # prevent uppercase/lowercase

print(f"Your weight is: {round(weight, 1)} {unit}")
