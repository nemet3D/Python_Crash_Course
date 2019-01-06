from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'

    # If country was not found, return None.
    return None