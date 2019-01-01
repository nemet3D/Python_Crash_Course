# Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of
# magicians by adding the phrase the Great to each magician’s name. Call
# show_magicians() to see that the list has actually been modified.

def show_magicians(magician_names):
    """Print the name of the magicians from the list"""
    for magician_name in magician_names:
        print(magician_name.title())

def make_great(magician_names):
    """Add the phrase 'The Great' before the magician's name."""
    for i in range(len(magician_names)):
        magician_names[i] += ' the Great'

magician_names = ['houdini', 'gandalf']

show_magicians(magician_names)

make_great(magician_names)

show_magicians(magician_names)