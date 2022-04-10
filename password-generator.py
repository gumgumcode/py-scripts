from random import randint, choice

length = int(input('Enter the length of the password: '))
uppercase_allowed = input('Upper case allowed? Y/N ').upper()
lowercase_allowed = input('Lower case allowed? Y/N ').upper()
numbers_allowed = input('Numbers allowed? Y/N ').upper()
symbols_allowed = input('Symbols allowed? Y/N ').upper()

ranges = []

if uppercase_allowed != "N":
    ranges.append((65,90))
if lowercase_allowed != "N":
    ranges.append((97, 122))
if numbers_allowed != "N":
    ranges.append((49, 57))
if symbols_allowed != "N":
    ranges.append((35, 38))

password = ''
for c in range(length):
    r = choice(ranges)
    ascii_code = randint(*r)
    char = chr(ascii_code)
    password += char

print()
print(password)
print()