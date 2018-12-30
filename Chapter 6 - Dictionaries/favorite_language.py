# Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that
# are not.
# • Loop through the list of people who should take the poll. If they
# have already taken the poll, print a message thanking them for
# responding. If they have not yet taken the poll, print a message
# inviting them to take the poll.

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c++', 'python'],
    'edward': ['javascript'],
    'phil': ['c#', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) <= 1:
        print("\n" + name.title() + "'s favorite language is:")
        print("\t" + languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())