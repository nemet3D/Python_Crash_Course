# OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the
# program using the OrderedDict class and make sure the order of the
# output matches the order in which key-value pairs were added to the
# dictionary.

from collections import OrderedDict


glossary = OrderedDict()

glossary['list'] = 'a list of words'
glossary['loop'] = 'for looping'
glossary['dictionary'] = 'dictionary'
glossary['tuple'] = 'a fixed list'
glossary['blog'] = 'weblog'
glossary['variables'] = 'variables'
glossary['monty'] = 'python'

for key, value in glossary.items():
    print(key.title() + " means: " + value + ".")