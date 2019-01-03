# Common Words: Visit Project Gutenberg (http://gutenberg.org/) and find
# a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the
# number of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg
# and determines how many times the word 'the' appears in each text.

def common_word(filename, word):
    """Count the approximate number of times a words appears."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of times the word appears in the file.
        times = contents.lower().count(word)
        print("The word " + word + " appears " + str(times) + " times in " + filename + ".")

filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt']
word = 'row'
for filename in filenames:
    common_word(filename, word)