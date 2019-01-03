# Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a
# separate program that reads in this value and prints the message, “I
# know your favorite number! It’s _____ .”

import json

filename = 'number.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(int(favorite_number), f_obj)
        print("I know your favorite number: " + str(favorite_number) + "!")
else:
    print("Your favorite number is : " + str(number) + "!")