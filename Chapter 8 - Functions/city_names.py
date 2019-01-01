# City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string
# formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print
# the value that’s returned.

def city_country(city, country):
    """Format the city and country of input."""
    formated = city.title() + ', ' + country.title()
    print(formated)

city_country('santiago', 'chile')

city_country('berlin', 'germany')

city_country(country = 'france', city = 'paris')

