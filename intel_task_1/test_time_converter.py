import unittest

from intel_task_1.time_converter import time_to_sec


class TestTimeConverter(unittest.TestCase):
    def test_type_error(self):
        values = ['1seconds', '-1', 1, '1m30s', '1y']
        for i in values:
            with self.assertRaises(TypeError):
                time_to_sec(i)

    def test_value_error(self):
        values = ['.', '.s', '.m', '.h', '.d']
        for i in values:
            with self.assertRaises(ValueError):
                time_to_sec(i)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            time_to_sec('')

    def test_no_args(self):
        self.assertEqual(time_to_sec(), 1)

    def test_specifier_only(self):
        time_units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        for i in time_units.keys():
            self.assertEqual(time_to_sec(i), time_units.get(i))

    def test_different_input_styles(self):
        values = {'01', '1s', '1.s', '1.1s', '1.1', '.017m'}
        for i in values:
            self.assertEqual(time_to_sec(i), 1)

    def test_int_data(self):
        values = {'2s': 2, '2m': 120, '2h': 7200, '2d': 172800, '0': 0, '0s': 0}
        for i in values.keys():
            self.assertEqual(time_to_sec(i), values.get(i))

    def test_float_data(self):
        values = {'60.5m': 3630, '1.0004h': 3601, '.0001d': 8}
        for i in values.keys():
            self.assertEqual(time_to_sec(i), values.get(i))


if __name__ == "__main__":
    unittest.main()
