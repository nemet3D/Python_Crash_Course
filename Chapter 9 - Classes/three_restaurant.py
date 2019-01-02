# Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call
# describe_restaurant() for each instance.

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

restaurant_01 = Restaurant('hard rock cafe', 'mediteranean')

restaurant_02 = Restaurant('rick', 'american')

restaurant_03 = Restaurant('mum and pop', 'dinner')

restaurant_01.describe_restaurants()

restaurant_02.describe_restaurants()

restaurant_03.describe_restaurants()

