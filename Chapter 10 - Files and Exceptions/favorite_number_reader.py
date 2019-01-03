import json

filename = 'number.txt'
with open(filename) as f_obj:
    number = json.load(f_obj)

print("I know your favorite number: " + str(number) + "!")