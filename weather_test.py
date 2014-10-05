import unittest
from weather import clean_data, tokenize, is_valid, min_range_day, get_min_diurnal

class WeatherTests(unittest.TestCase):

    def test_data_clean_works_correctly(self):
        test_data = "   9  86    32*   59       6  61.5       0.00         240  7.6 220  12  6.0  78 46 1018.6"
        self.assertTrue("*" not in clean_data(test_data))

    def test_tokenize_works_correctly(self):
        test_data = "a  b    c    d e"
        expected_tokens = ["a", "b", "c", "d", "e"]
        self.assertEqual(expected_tokens, tokenize(test_data))

    def test_is_valid(self):
        valid_data = ["12", "56",   "89"]
        invalid_data = ["mo",  "34",  "222"]
        invalid_data2 = ["34",  "34.1", "56"]
        self.assertTrue(is_valid(valid_data))
        self.assertFalse(is_valid(invalid_data))
        self.assertFalse(is_valid(invalid_data2))

    def test_min_range_day(self):
        day_one = ["1", "88", "59"]
        day_two = ["2", "79", "63"]
        days = [day_one, day_two]
        self.assertEqual(min_range_day(days), 2)

    def test_main(self):
        file_name = "weather.dat"
        self.assertEqual(get_min_diurnal(file_name), 14)


if __name__ == "__main__":
    unittest.main()