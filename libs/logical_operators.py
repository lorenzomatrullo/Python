# LOGICAL OPERATORS = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temperature = 25

### or
is_raining = True

if temperature > 35 or temperature < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


### and
is_sunny = True

if temperature >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temperature <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temperature > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")


### not
if temperature >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temperature <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temperature > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")