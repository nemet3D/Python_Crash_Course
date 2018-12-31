# Multiples of Ten: Ask the user for a number, and then report whether
# the number is a multiple of 10 or not.

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print("\nYour number is a multiple of 10.")
else:
    print("\nYour number is not divisible by 10.")