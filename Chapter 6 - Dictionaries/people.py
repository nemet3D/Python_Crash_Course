# People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all
#  three dictionaries in a list called people. Loop through your list of
#  people. As you loop through the list, print everything you know about
#  each person.

person_0 = {
    'first_name': 'cristiano',
    'last_name': 'ronaldo',
    'age': 30,
    'city': 'torino'
}

person_1 = {
    'first_name': 'luka',
    'last_name': 'modric',
    'age': 30,
    'city': 'madrid'
}

person_2 = {
    'first_name': 'paul',
    'last_name': 'pogba',
    'age': 30,
    'city': 'manchester'
}

persons = [person_0, person_1, person_2]

for person in persons:
    print(person)