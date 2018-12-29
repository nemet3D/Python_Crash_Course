# Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters . Use these words as the keys in your glossary, and store
# their meanings as values.
# • Print each word and its meaning as neatly formatted output . You
# might print the word followed by a colon and then its meaning, or
# print the word on one line and then print its meaning indented on a
# second line. Use the newline character ( \n ) to insert a blank line
# between each word-meaning pair in your output.

glossary = {
    'list': 'a list of words',
    'loop': 'for looping',
    'dictionary': 'dictionary',
    'tuple': 'a fixed list',
    'blog': 'weblog'
}

print("\nA list is: " + glossary['list'] + ".")
print("\nA loop is: " + glossary['loop'] + ".")
print("\nA dictionary is: " + glossary['dictionary'] + ".")
print("\nA tuple is: " + glossary['tuple'] + ".")
print("\nA blog is: " + glossary['blog'] + ".")