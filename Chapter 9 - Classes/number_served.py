# Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class . Print the
# number of customers the restaurant has served, and then change this
# value and print it again. Add a method called set_number_served() that
# lets you set the number of customers that have been served. Call this
# method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any
# number you like that could represent how many customers were served
# in, say, a day of business.

class Restaurant():
    """An attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurants(self):
        """Print description of restaurant."""
        print(self.restaurant_name.title() + " is a " +
            self.cuisine_type.title() + " type restaurant.")
        print("We served " + str(self.number_served) + " clients today.")

    def open_restaurant(self):
        """Print the hour when the restaurant opens."""
        print("The " + self.restaurant_name.title() + " opens at 10 AM.")

    def set_number_served(self, served):
        """Number the customers that have been served"""
        self.number_served = served

    def increment_number_served(self, increment):
        """Add the given amount to the served clients number"""
        self.number_served += increment


restaurant = Restaurant('hard rock cafe', 'mediteranean')

restaurant.describe_restaurants()

restaurant.open_restaurant()

restaurant.set_number_served(5)

restaurant.describe_restaurants()

restaurant.increment_number_served(1)

restaurant.describe_restaurants()