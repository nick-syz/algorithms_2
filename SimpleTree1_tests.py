from SimpleTree1 import SimpleTree, SimpleTreeNode
from unittest import TestCase

class SimpleTreeTest(TestCase):
    def setUp(self):
        self.node_9 = SimpleTreeNode(9, None)
        self.node_4 = SimpleTreeNode(4, self.node_9)
        self.node_3 = SimpleTreeNode(3, self.node_4)
        self.node_6 = SimpleTreeNode(6, self.node_4)
        self.node_5 = SimpleTreeNode(5, self.node_6)
        self.node_7 = SimpleTreeNode(7, self.node_6)
        self.node_17 = SimpleTreeNode(17, self.node_9)
        self.node_22 = SimpleTreeNode(22, self.node_17)
        self.node_20 = SimpleTreeNode(20, self.node_22)
        self.node_7_1 = SimpleTreeNode(7, self.node_6)

        self.tree = SimpleTree(self.node_9)
        
        self.tree.AddChild(self.node_9, self.node_4)
        self.tree.AddChild(self.node_4, self.node_3)
        self.tree.AddChild(self.node_4, self.node_6)
        self.tree.AddChild(self.node_6, self.node_5)
        self.tree.AddChild(self.node_6, self.node_7)
        self.tree.AddChild(self.node_6, self.node_7_1)
        self.tree.AddChild(self.node_9, self.node_17)
        self.tree.AddChild(self.node_17, self.node_22)
        self.tree.AddChild(self.node_22, self.node_20)

    def test_AddChild(self):
        self.assertEqual(10, self.tree.Count())
        self.assertEqual(5, self.tree.LeafCount())
        
        self.assertTrue(len(self.tree.FindNodesByValue(9)))
        self.assertTrue(len(self.tree.FindNodesByValue(4)))
        self.assertTrue(len(self.tree.FindNodesByValue(3)))
        self.assertTrue(len(self.tree.FindNodesByValue(6)))
        self.assertTrue(len(self.tree.FindNodesByValue(5)))
        self.assertTrue(len(self.tree.FindNodesByValue(7)))
        self.assertTrue(len(self.tree.FindNodesByValue(17)))
        self.assertTrue(len(self.tree.FindNodesByValue(22)))
        self.assertTrue(len(self.tree.FindNodesByValue(20)))
        
        self.assertEqual(2, len(self.tree.FindNodesByValue(7)))
    
    def test_Delete(self):  
        self.tree.DeleteNode(self.node_6)
        self.assertFalse(len(self.tree.FindNodesByValue(6)))
        self.assertFalse(len(self.tree.FindNodesByValue(5)))
        self.assertFalse(len(self.tree.FindNodesByValue(7)))
        
        self.assertTrue(len(self.tree.FindNodesByValue(9)))
        self.assertTrue(len(self.tree.FindNodesByValue(4)))
        self.assertTrue(len(self.tree.FindNodesByValue(3)))

        self.assertTrue(len(self.tree.FindNodesByValue(17)))
        self.assertTrue(len(self.tree.FindNodesByValue(22)))
        self.assertTrue(len(self.tree.FindNodesByValue(20)))

    def test_Move(self):
        self.tree.MoveNode(self.node_6, self.node_20)
        
        self.assertEqual(1, len(self.node_4.Children))
        self.assertEqual(1, len(self.node_20.Children))

        self.tree.MoveNode(self.node_9, self.node_20)

        self.tree.MoveNode(self.node_4, self.node_17)

        self.assertEqual(9, len(SimpleTree(self.node_17).GetAllNodes()))

        self.assertEqual(1, len(self.node_9.Children))
        self.assertEqual(17, self.node_9.Children[0].NodeValue)

        self.assertEqual(10, self.tree.Count())
        self.assertEqual(4, self.tree.LeafCount())
