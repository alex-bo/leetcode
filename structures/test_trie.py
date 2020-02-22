import unittest

from structures.trie import TernarySearchTrie


class TernarySearchTrieTest(unittest.TestCase):

    def test(self):
        tst = TernarySearchTrie()

        self.assertEqual(0, len(tst))
        self.assertFalse(tst)
        self.assertNotIn('first_key', tst)

        tst['first_key'] = 'first_value'
        tst['second_key'] = 'second_value'

        self.assertEqual(2, len(tst))
        self.assertTrue(tst)
        self.assertIn('first_key', tst)
        self.assertIn('second_key', tst)
        self.assertNotIn('third_key', tst)
        self.assertEqual('first_value', tst['first_key'])
        self.assertEqual('second_value', tst['second_key'])

        del tst['first_key']

        self.assertEqual(1, len(tst))
        self.assertTrue(tst)
        self.assertNotIn('first_key', tst)
        self.assertIn('second_key', tst)
        self.assertIsNone(tst.get('first_key'))
        self.assertEqual('second_value', tst.get('second_key'))



