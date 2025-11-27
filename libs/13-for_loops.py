# for loops = exeecute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)


for y in reversed (range(1, 11)):                 # backwards
    print(y)


for z in range(1, 11, 2):                            # added a step to skip positions
    print(z)


credit_card = "1234-5678-9012-3456"

for number in credit_card:
    print(number)