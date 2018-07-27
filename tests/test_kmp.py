import sys
from os import path
sys.path.append(path.dirname(path.dirname(__file__)))


import kmp
import unittest

class KmpTest(unittest.TestCase):


    def test_prefixtable_returns_prefixtable_for_given_string(self):
        text = 'ABCABABCABC'
        expected_table = [0, 0, 0, 1, 2, 1, 2, 3, 4, 5, 3]

        self.assertEqual(expected_table, kmp.prefixtable(text))


        text = 'AAACAAAA'
        expected_table = [0, 1, 2, 0, 1, 2, 3, 3]

        self.assertEqual(expected_table, kmp.prefixtable(text))


if __name__ == '__main__':
    unittest.main()
