def get_formatted_name(city, country, population=''):
    """Generate e neatly formatted name."""
    if population:
        full_name = city + ", " + country + " - Population " + population
    else:
        full_name = city + ", " + country
    return full_name.title()