# Users: Make a class called User . Create two attributes called
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. Make
# another method called greet_user() that prints a personalized greeting
# to the user. Create several instances representing different users,
# and call both methods for each user.

class User():
    """For users."""

    def __init__(self, first_name, last_name):
        """Initialize user's first name and last name."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print the summary of a user's information."""
        print("\nUser's first and last name: " + self.first_name.title() +
            " " + self.last_name.title())

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print("\nWelcome " + self.first_name.title() + " " + 
            self.last_name.title() + "!")

user_01 = User('albert', 'einstein')

user_02 = User('marie', 'curie')

user_01.describe_user()

user_02.describe_user()

user_01.greet_user()

user_02.greet_user()
