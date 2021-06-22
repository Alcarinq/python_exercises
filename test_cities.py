import unittest
from city_functions import print_name


class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = print_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = print_name('santiago', 'chile', 1000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - Populacja 1000000')
