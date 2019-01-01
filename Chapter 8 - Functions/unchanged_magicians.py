# Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names.
# Because the original list will be unchanged, return the new list and
# store it in a separate list. Call show_magicians() with each list to
# show that you have one list of the original names and one list with
# the Great added to each magician’s name.

def show_magicians(magician_names):
    """Print the name of the magicians from the list"""
    for magician_name in magician_names:
        print(magician_name.title())

def make_great(copy_magician_names):
    """Add the phrase 'The Great' before the magician's name in a copied list."""
    for i in range(len(copy_magician_names)):
        copy_magician_names[i] += ' the Great'
    return copy_magician_names

magician_names = ['houdini', 'gandalf']
show_magicians(magician_names)

new_list = make_great(magician_names[:])
show_magicians(new_list)

show_magicians(magician_names)