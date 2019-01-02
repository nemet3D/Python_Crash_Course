# Admin: An administrator is a special kind of user. Write a class
# called Admin that inherits from the User class you wrote in Exercise
# 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute,
# privileges, that stores a list of strings like "can add post", "can
# delete post", "can ban user", and so on. Write a method called
# show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

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


class Privileges():
    """Represent aspects of an admin user."""

    def __init__(self, first_name, last_name):
        """Then initialize attributes specific to an admin user."""
        self.first_name = first_name
        self.last_name = last_name
        self.rights = ['add posts', 'delete posts']

    def describe_user(self):
        """Print the summary of a user's information."""
        print("\nUser's first and last name: " + self.first_name.title() +
            " " + self.last_name.title())

    def display_rights(self):
        """Print the different rights of an admin user."""
        print("An admin user has the following rights: ")
        for right in self.rights:
            print("\t" + right)
