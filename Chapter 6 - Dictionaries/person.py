# Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they
# live. You should have keys such as first_name  last_name, age, and
# city. Print each piece of information stored in your dictionary.

person = {
    'first_name': 'cristiano',
    'last_name': 'ronaldo',
    'age': 30,
    'city': 'torino'
}

print(person['first_name'].title() + " " + person['last_name'].title() +
             ", " + str(person['age']) + ", " + person['city'].title() +
             ".")