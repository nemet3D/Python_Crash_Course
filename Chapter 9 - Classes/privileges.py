# Privileges: Write a separate Privileges class. The class should have
# one attribute, privileges, that stores a list of strings as described
# in Exercise 9-7. Move the show_privileges() method to this class. Make
# a Privileges instance as an attribute in the Admin class. Create a new
# instance of Admin and use your method to show its privileges.

"""A class for privileges."""

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
