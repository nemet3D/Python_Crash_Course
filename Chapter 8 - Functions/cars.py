# Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a 
# model name. It should then accept an arbitrary number of keyword
# arguments. Call the function with the required information and two
# other name-value pairs, such as a color or an optional feature. Your
# function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information
# was stored correctly.

def make_car(brand, type, **other):
    """Build a dictionary containing everything we know about a user."""
    car = {}
    car['brand'] = brand
    car['type'] = type
    for key, value in other.items():
        car[key] = value
    return car

my_car = make_car('subaru', 'outback', color = 'blue', doors = 5, tow_package = True)

print(my_car)