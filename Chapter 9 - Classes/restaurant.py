# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant():
    """An attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurants(self):
        """Print description of restaurant."""
        print(self.restaurant_name.title() + " is a " +
            self.cuisine_type.title() + " type restaurant.")

    def open_restaurant(self):
        """Print the hour when the restaurant opens."""
        print("The " + self.restaurant_name.title() + " opens at 10 AM.")

restaurant = Restaurant('hard rock cafe', 'mediteranean')

restaurant.describe_restaurants()

restaurant.open_restaurant()