import unittest
from unittest import mock
from format_output import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average_scores.average() == 90
        with mock.patch('builtins.input', side_effect=[60, 70, 80]):
            assert average_scores.average() == 70


if __name__ == '__main__':
    unittest.main()
