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


    def test_match_returns_index_of_pattern_matched_in_test(self):
        text = 'AAAAAAAAAAAAAAAAAB'
        pattern = 'AAAB'

        self.assertEqual(text.find(pattern), kmp.match(text, pattern))

        text = 'AAAAABAAABA'
        pattern = 'AAAA'

        self.assertEqual(text.find(pattern), kmp.match(text, pattern))

        text = 'ABABABCABABABCABABABC'
        pattern = 'ABABAC'

        self.assertEqual(text.find(pattern), kmp.match(text, pattern))


    def test_match_returns_negative_1_if_pattern_not_in_text(self):
        text = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        pattern = 'AAAB'

        self.assertEqual(-1, kmp.match(text, pattern))




if __name__ == '__main__':
    unittest.main()
