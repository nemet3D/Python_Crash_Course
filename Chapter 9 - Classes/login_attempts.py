# Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called
# increment_ login_attempts() that increments the value of
# login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.

class User():
    """For users."""

    def __init__(self, first_name, last_name):
        """Initialize user's first name and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print the summary of a user's information."""
        print("\nUser's first and last name: " + self.first_name.title() +
            " " + self.last_name.title())

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print("\nWelcome " + self.first_name.title() + " " + 
            self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1
        print("\nNumber of login attempts: " + str(self.login_attempts) + ".")

    def reset_login_attempts(self):
        """Reset the valua of login_attempts to 0."""
        self.login_attempts = 0
        print("\nLogin attempt reset to: " + str(self.login_attempts))

user_01 = User('albert', 'einstein')

user_01.describe_user()

user_01.greet_user()

user_01.increment_login_attempts()

user_01.increment_login_attempts()

user_01.increment_login_attempts()

user_01.increment_login_attempts()

user_01.reset_login_attempts()

user_01.increment_login_attempts()