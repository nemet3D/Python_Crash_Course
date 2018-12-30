# Pets: Make several dictionaries, where the name of each dictionary is
# the name of a pet. In each dictionary, include the kind of animal and
# the owner’s name. Store these dictionaries in a list called pets.
# Next, loop through your list and as you do print everything you know
# about each pet.

pet_0 = {
    'name': 'cleopatra',
    'animal': 'cat',
    'owner': 'sandra',
}

pet_1 = {
    'name': 'rex',
    'animal': 'dog',
    'owner': 'george',
}

pet_2 = {
    'name': 'khabib',
    'animal': 'bear',
    'owner': 'ali',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet)