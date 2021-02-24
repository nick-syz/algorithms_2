from aBST import aBST
from unittest import TestCase

class aBSTTest(TestCase):
    def setUp(self):
        self.tree = aBST(15)
        self.tree.Tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]

    def test_find(self):
        self.assertEqual(0, self.tree.FindKeyIndex(50))
        self.assertEqual(9, self.tree.FindKeyIndex(31))
        self.assertEqual(-12, self.tree.FindKeyIndex(63))
        self.assertEqual(-3, self.tree.FindKeyIndex(20))
        self.tree.AddKey(20)
        self.assertEqual(-8, self.tree.FindKeyIndex(22))
        self.tree.AddKey(22)
        self.assertEqual(-7, self.tree.FindKeyIndex(15))
        self.assertEqual(None, self.tree.FindKeyIndex(53))
        self.assertEqual(None, self.tree.FindKeyIndex(30))

    def test_add(self):
        self.assertEqual(3, self.tree.AddKey(20))
        self.assertEqual(7, self.tree.AddKey(18))
        self.assertEqual(8, self.tree.AddKey(22))
        self.assertEqual(-1, self.tree.AddKey(30))
        self.assertEqual(12, self.tree.AddKey(65))
        self.assertEqual(13, self.tree.AddKey(80))
        self.assertEqual(14, self.tree.AddKey(92))

        self.assertEqual(None, self.tree.FindKeyIndex(130))

    def test_empty(self):
        tree = aBST(4)

        self.assertEqual(0, tree.FindKeyIndex(10))
        self.assertEqual(0, tree.AddKey(10))
        self.assertEqual(0, tree.AddKey(10))
