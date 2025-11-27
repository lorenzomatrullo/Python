# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[2])
print(credit_number[0:4])   # returns the first 4 digits
print(credit_number[:4])    # assumes the starting position will be the beginning of the string
print(credit_number[5:])    # returns all the digits after the 5th position
print(credit_number[-1])    # starts returning digits from the end of the string