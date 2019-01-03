# Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the
# second file. Write a program that tries to read these files and print
# the contents of the file to the screen. Wrap your code in a try-except
# block to catch the FileNotFound error, and print a friendly message if
# a file is missing. Move one of the files to a different location on
# your system, and make sure the code in the except block executes
# properly.

def print_file_content(filename):
    """Print the content of a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        print(contents)

filenames = ['cats.txt', 'dogs.txt', 'cows.txt']
for filename in filenames:
    print_file_content(filename)