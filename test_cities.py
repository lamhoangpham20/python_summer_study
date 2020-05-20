import unittest
from city_functions import show_city


class CitiesTestCases(unittest.TestCase):
    def test_city_country(self):
        """Tests for 'cities_function.py'."""
        formatted_city = show_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_city = show_city('santiago', 'chile','10000')
        self.assertEqual(formatted_city, 'Santiago, Chile - population 10000')

if __name__ == '__main__':
    unittest.main()
