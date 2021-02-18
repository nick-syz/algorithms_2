from BinarySearchTree import BSTNode, BSTFind, BST
from unittest import TestCase

class BinarySearchTreeTest(TestCase):
    def setUp(self):
        self.node_9 = BSTNode(9, 9, None)
        self.node_4 = BSTNode(4, 4, self.node_9)
        self.node_3 = BSTNode(3, 3, self.node_4)
        self.node_6 = BSTNode(6, 6, self.node_4)
        self.node_5 = BSTNode(5, 5, self.node_6)
        self.node_7 = BSTNode(7, 7, self.node_6)
        self.node_17 = BSTNode(17, 17, self.node_9)
        self.node_22 = BSTNode(22, 22, self.node_17)
        self.node_20 = BSTNode(20, 20, self.node_22)

        self.bst = BST(self.node_9)
        
        self.bst.AddKeyValue(4, 4)
        self.bst.AddKeyValue(3, 3)
        self.bst.AddKeyValue(6, 6)
        self.bst.AddKeyValue(5, 5)
        self.bst.AddKeyValue(7, 7)
        self.bst.AddKeyValue(17, 17)
        self.bst.AddKeyValue(22, 22)
        self.bst.AddKeyValue(20, 20)

    def test_add(self):
        self.assertTrue(self.bst.AddKeyValue(30, 30))
        self.assertFalse(self.bst.AddKeyValue(4, 4))
        self.assertFalse(self.bst.AddKeyValue(3, 3))
        self.assertFalse(self.bst.AddKeyValue(6, 6))
        self.assertFalse(self.bst.AddKeyValue(5, 5))
        self.assertFalse(self.bst.AddKeyValue(7, 7))
        self.assertFalse(self.bst.AddKeyValue(17, 17))
        self.assertFalse(self.bst.AddKeyValue(22, 22))
        self.assertFalse(self.bst.AddKeyValue(20, 20))
    
    def test_find(self):
        # check field "Node"
        self.assertIsNone(self.bst.FindNodeByKey(1).Node)
        self.assertIsNone(self.bst.FindNodeByKey(2).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(9).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(4).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(3).Node)  
        self.assertIsNotNone(self.bst.FindNodeByKey(6).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(5).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(7).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(17).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(22).Node)
        self.assertIsNotNone(self.bst.FindNodeByKey(20).Node)

        # check field "NodeHasKey"
        self.assertTrue(self.bst.FindNodeByKey(9).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(4).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(3).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(6).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(5).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(7).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(17).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(22).NodeHasKey)
        self.assertTrue(self.bst.FindNodeByKey(20).NodeHasKey)
        
        self.assertFalse(self.bst.FindNodeByKey(1).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(2).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(25).NodeHasKey)
        self.assertFalse(self.bst.FindNodeByKey(8).NodeHasKey)
        
        # check field "ToLeft"
        self.assertFalse(self.bst.FindNodeByKey(9).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(4).ToLeft)  
        self.assertTrue(self.bst.FindNodeByKey(3).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(6).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(5).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(7).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(17).ToLeft)
        self.assertFalse(self.bst.FindNodeByKey(22).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(20).ToLeft)
        self.assertTrue(self.bst.FindNodeByKey(1).ToLeft)
    def test_minmax(self):
        # Max from Root
        self.assertEqual(22, self.bst.FinMinMax(self.bst.Root, True).Node.NodeValue)
        # Min from Root
        self.assertEqual(3, self.bst.FinMinMax(self.bst.Root, False).Node.NodeValue)
        
        # Max from subtree (NodeKey = 17)
        self.assertEqual(22, self.bst.FinMinMax(self.bst.FindNodeByKey(17).Node, True).Node.NodeValue)
        # Min from subtree (NodeKey = 4)
        self.assertEqual(3, self.bst.FinMinMax(self.bst.FindNodeByKey(4).Node, False).Node.NodeValue)
    
    def test_delete(self):
        self.assertEqual(9, self.bst.Count())
        self.assertIsNotNone(self.bst.FindNodeByKey(7).Node)
        self.assertTrue(self.bst.DeleteNodeByKey(7))
        self.assertEqual(8, self.bst.Count())

        self.assertFalse(self.bst.DeleteNodeByKey(7))
        self.assertEqual(8, self.bst.Count())

        self.assertTrue(self.bst.AddKeyValue(7, 7))
        self.assertEqual(9, self.bst.Count())

        self.assertFalse(self.bst.DeleteNodeByKey(23))
        
        self.assertTrue(self.bst.DeleteNodeByKey(9))
        self.assertEqual(0, self.bst.Count())

    def test_count(self):
        self.assertEqual(9, self.bst.Count())

    def test_zero_tree(self):
        self.assertTrue(self.bst.DeleteNodeByKey(9))
        self.assertEqual(0, self.bst.Count())
        self.assertIsNone(self.bst.FindNodeByKey(9).Node)
        self.assertIsNone(self.bst.FinMinMax(self.bst.Root, True).Node)
        self.assertIsNone(self.bst.FinMinMax(self.bst.Root, False).Node)

        self.assertTrue(self.bst.AddKeyValue(9, 9))
        self.assertEqual(1, self.bst.Count())
        self.assertIsNotNone(self.bst.FindNodeByKey(9).Node)
        
        self.assertEqual(9, self.bst.FinMinMax(self.bst.Root, True).Node.NodeValue)
        self.assertEqual(9, self.bst.FinMinMax(self.bst.Root, False).Node.NodeValue)
