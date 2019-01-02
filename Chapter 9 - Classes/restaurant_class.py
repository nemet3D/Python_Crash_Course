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