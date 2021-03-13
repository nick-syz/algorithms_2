from SimpleTree import SimpleTree, SimpleTreeNode
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

    def test_EvenTrees(self):
        self.tree.Root = None

        node_1 = SimpleTreeNode(1, None)
        node_2 = SimpleTreeNode(2, node_1)
        node_3 = SimpleTreeNode(3, node_1)
        node_6 = SimpleTreeNode(6, node_1)
        node_5 = SimpleTreeNode(5, node_2)
        
        node_14 = SimpleTreeNode(14, node_5)
        
        node_7 = SimpleTreeNode(7, node_2)
        
        node_15 = SimpleTreeNode(15, node_7)
        
        node_4 = SimpleTreeNode(4, node_3)
        node_8 = SimpleTreeNode(8, node_6)
        node_9 = SimpleTreeNode(9, node_8)
        node_10 = SimpleTreeNode(10, node_8)
        
        node_11 = SimpleTreeNode(11, node_9)
        node_12 = SimpleTreeNode(12, node_10)

        node_1.Children = [node_2, node_3, node_6] 
        node_2.Children = [node_5, node_7]
        
        node_5.Children = [node_14]
        node_7.Children = [node_15]
        
        node_3.Children = [node_4]
        node_6.Children = [node_8]
        node_8.Children = [node_9, node_10]
        
        node_9.Children = [node_11]
        node_10.Children = [node_12]

        self.tree.Root = node_1

        deleted_bonds = self.tree.EvenTrees()
        check = ([node_1, node_3], [node_1, node_6], 
                 [node_2, node_5], [node_2, node_7], 
                 [node_8, node_9], [node_8, node_10])
        i = 0
        count = 0
        for j in range(0, len(deleted_bonds)+1, 2):
            if deleted_bonds[i:j] in check:
                count += 1
            i = j

        self.assertEqual(6, count)
