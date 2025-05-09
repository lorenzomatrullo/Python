# keyword arguments = an argument preceded by an  identifier
#                     helps with readbility
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 1, area = 123, first = 456, last = 7890)

print(phone_num)