import unittest

from structures.red_black_bst import RedBlackBST


class RedBlackBSTTest(unittest.TestCase):

    def test(self):
        bst = RedBlackBST()

        self.assertFalse(bst)
        self.assertEqual(0, len(bst))
        self.assertIsNone(bst.get(1))
        self.assertFalse(1 in bst)

        for i in range(100):
            bst[i] = str(i)

        self.assertTrue(bst)
        self.assertEqual(100, len(bst))
        self.assertEquals('10', bst.get(10))
        self.assertEquals('56', bst[56])
        self.assertTrue(43 in bst)
        self.assertEqual(list(range(100)), list(bst))
        self.assertEqual(list(range(100)), bst.keys(0, 99))
        self.assertEqual(50, bst.size(0, 49))

        for _ in range(10):
            bst.delete_min()
            bst.delete_max()

        self.assertEqual(80, len(bst))
        self.assertEquals(None, bst.get(9))
        self.assertEquals('56', bst[56])
        self.assertFalse(90 in bst)
        self.assertEqual(list(range(10, 90)), list(bst))
        self.assertEqual(list(range(10, 90)), bst.keys(0, 99))
        self.assertEqual(1, bst.size(0, 10))
        self.assertEqual(10, bst.min())
        self.assertEqual(89, bst.max())
        self.assertEqual(11, bst.select(1))
        self.assertEqual(1, bst.rank(11))

        for i in list(range(10, 90)):
            del bst[i]

        self.assertFalse(bst)
        self.assertEqual(0, len(bst))
        self.assertIsNone(bst.get(1))
        self.assertFalse(1 in bst)

        for i in list(range(0, 100, 10)):
            bst[i] = str(i)

        self.assertEqual(50, bst.floor(59))
        self.assertEqual(60, bst.ceiling(59))

    def test__put_zero_value__return_zero_value(self):
        bst = RedBlackBST()
        bst[123] = 0
        self.assertEqual(0, bst[123])



