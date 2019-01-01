def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'rex', animal_type = 'cat')

describe_pet('willie')

describe_pet('harry', 'hamster')

describe_pet(animal_type = 'bear', pet_name = 'fram')

describe_pet(pet_name = 'frodo')