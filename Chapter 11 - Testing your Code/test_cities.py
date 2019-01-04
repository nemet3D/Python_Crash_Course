import unittest
from format_city_country import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'format_city_country.py'."""

    def test_city_country(self):
        """Do names like 'Santiago, Chile' work?"""
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do names like 'Santiag, Chile - Population 5000000' work?"""
        formatted_name = get_formatted_name('santiago', 'chile', '5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000000')

unittest.main()