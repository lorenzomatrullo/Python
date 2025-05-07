# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                   inner loop:


for x in range(3):
    for y in range(1, 10):
        print(y, end="")            # end="" makes all the number to be on the same line
    print()