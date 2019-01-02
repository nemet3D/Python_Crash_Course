# Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write class called IceCreamStand that inherits from the Restaurant
# class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171).
# Either version of the class will work; just pick the one you like
# better. Add an attribute called flavors that stores a list of ice
# cream flavors. Write a method that displays these flavors. Create an
# instance of IceCreamStand, and call this method.

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

class IceCreamStand(Restaurant):
    """Represent aspects of an ice cream stand."""

    def __init__(self, restaurant_name, cuisin_type):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisin_type)
        self.flavours = ['vanilla', 'strawberry']

    def display_flavours(self):
        """Print the different flavours of the ice cream stand."""
        print("This offers the following flavours: ")
        for flavour in self.flavours:
            print("\t" + flavour)


restaurant = Restaurant('hard rock cafe', 'mediteranean')

restaurant.describe_restaurants()

restaurant.open_restaurant()


restaurant = IceCreamStand('cream ice', 'ice cream stand')

restaurant.describe_restaurants()

restaurant.display_flavours()