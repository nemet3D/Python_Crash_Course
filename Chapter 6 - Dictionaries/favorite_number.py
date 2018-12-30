# Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number . Then print each
# person’s name along with their favorite numbers.

favorite_numbers = {
    'john': ['5', '6'],
    'edward': ['7'],
    'phil': ['10', '25', '63'],
    'eli': ['13']
}

for name, numbers in favorite_numbers.items():
    if len(numbers) <= 1:
        print("\n" + name.title() + "'s favorite number is:")
        print("\t" + numbers[0].title())
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + number.title())