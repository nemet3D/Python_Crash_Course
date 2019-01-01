# Large Shirts: Modify the make_shirt() function so that shirts are
# large by default with a message that reads I love Python. Make a large
# shirt and a medium shirt with the default message, and a shirt of any
# size with a different message.

def make_shirt(size = 'l', text = 'I love Python'):
    """Display information about the size and text on the t-shirt."""
    print("\nI want a size " + size.upper() + " t-shirt.")
    print("The text should read: " + text + ".")

make_shirt()

make_shirt('xxl', 'Man Utd')

make_shirt(text = 'Forza Juve', size = 'm')