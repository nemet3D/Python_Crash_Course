# Magicians: Make a list of magician’s names. Pass the list to a
# function called show_magicians(), which prints the name of each
# magician in the list.

def show_magicians(magician_names):
    """Print the name of the magicians from the list"""
    for magician_name in magician_names:
        print(magician_name.title())

magician_names = ['houdini', 'gandalf']

show_magicians(magician_names)