def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)