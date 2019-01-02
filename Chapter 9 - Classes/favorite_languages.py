# Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that
# are not.
# • Loop through the list of people who should take the poll. If they
# have already taken the poll, print a message thanking them for
# responding. If they have not yet taken the poll, print a message
# inviting them to take the poll.

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c++'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + languages.title() + ".")
