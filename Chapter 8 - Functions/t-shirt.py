# T-Shirt: Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt . The
# function should print a sentence summarizing the size of the shirt and
# the message printed on it. Call the function once using positional
# arguments to make a shirt. Call the function a second time using
# keyword arguments.

def make_shirt(size, text):
    """Display information about the size and text on the t-shirt."""
    print("\nI want a size " + size.upper() + " t-shirt.")
    print("The text should read: " + text + ".")

make_shirt('xxl', 'Man Utd')

make_shirt(text = 'Forza Juve', size = 'm')