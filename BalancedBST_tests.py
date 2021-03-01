from BalancedBST import BSTNode, BalancedBST
from unittest import TestCase
import random

class BalancedBSTTEst(TestCase):
    def setUp(self):
        self.tree = BalancedBST()
    
    def test_generate(self):
        arr = [i for i in range(1, 16)]
        random.shuffle(arr)
        
        self.tree.GenerateTree(arr)
        lst = []
        for i in self.tree.WideAllNodes():
            lst.append(i.NodeKey)
        #print(lst)

        lst = []
        for  i in self.tree.WideAllNodes():
            lst.append(i.Level)
        #print(lst)
    
    def test_balanced(self):
        self.tree.GenerateTree([4, 3, 2, 6])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
    
    def test_balanced1(self):
        self.tree.GenerateTree([1, 2, 3])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
    
    def test_unbalanced1(self):
        self.assertIsNone(self.tree.Root)
        self.tree.GenerateTree([1, 2])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
    
    def test_balanced2(self):
        tree = BalancedBST()
        tree.Root = BSTNode(3, None)
        tree.Root.Level = 1
        
        node_2 = BSTNode(2, tree.Root)
        node_2.Level = 2
        tree.Root.LeftChild = node_2
        
        node_4 = BSTNode(4, tree.Root)
        node_4.Level = 2
        tree.Root.RightChild = node_4
        
        node_6 = BSTNode(6, node_4)
        node_6.Level = 3
        node_4.RightChild = node_6
        
        node_7 = BSTNode(7, node_6)
        node_7.Level = 4
        node_6.RightChild = node_7

        self.assertFalse(tree.IsBalanced(tree.Root))

    def test_balanced3(self):
        tree = BalancedBST()
        tree.Root = BSTNode(8, None)
        tree.Root.Level = 1

        node_7 = BSTNode(7, tree.Root)
        node_7.Level = 2
        tree.Root.LeftChild = node_7

        node_5 = BSTNode(5, node_7)
        node_5.Level = 3
        node_7.LeftChild = node_5

        node_6 = BSTNode(6, node_5)
        node_6.Level = 4
        node_5.RightChild = node_6

        node_10 = BSTNode(10, tree.Root)
        node_10.Level = 2
        tree.Root.RightChild = node_10

        node_9 = BSTNode(9, node_10)
        node_9.Level = 3
        node_10.LeftChild = node_9

        node_11 = BSTNode(11, node_10)
        node_11.Level = 3
        node_10.RightChild = node_11

        node_13 = BSTNode(13, node_11)
        node_13.Level = 4
        node_11.RightChild = node_13

        node_12 = BSTNode(12, node_13)
        node_12.Level = 5
        node_13.LeftChild = node_12

        self.assertFalse(tree.IsBalanced(tree.Root))
    
    def test_height(self):
        tree = BalancedBST()
        tree.Root = BSTNode(8, None)
        tree.Root.Level = 1

        node_7 = BSTNode(7, tree.Root)
        node_7.Level = 2
        tree.Root.LeftChild = node_7

        node_5 = BSTNode(5, node_7)
        node_5.Level = 3
        node_7.LeftChild = node_5

        node_6 = BSTNode(6, node_5)
        node_6.Level = 4
        node_5.RightChild = node_6

        node_10 = BSTNode(10, tree.Root)
        node_10.Level = 2
        tree.Root.RightChild = node_10

        node_9 = BSTNode(9, node_10)
        node_9.Level = 3
        node_10.LeftChild = node_9

        node_11 = BSTNode(11, node_10)
        node_11.Level = 3
        node_10.RightChild = node_11

        node_13 = BSTNode(13, node_11)
        node_13.Level = 4
        node_11.RightChild = node_13

        node_12 = BSTNode(12, node_13)
        node_12.Level = 5
        node_13.LeftChild = node_12

        self.assertEqual(5, tree.TreeDepth(tree.Root))
        self.assertFalse(tree.IsBalanced(tree.Root))
