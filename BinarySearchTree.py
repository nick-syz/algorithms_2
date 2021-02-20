# https://skillsmart.ru/algo/15-121-cm/bcd63523a1.html

class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

class BSTFind:
    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False

class BST:
    def __init__(self, node):
        self.Root = node
        self.count = 1

    def FindNodeByKey(self, key):
        result = BSTFind()
        node = self.Root
        while node is not None:
            if node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                return result
            elif key < node.NodeKey:
                if node.LeftChild is None:
                    result.Node = node
                    result.ToLeft = True
                    return result
                else:
                    node = node.LeftChild
            elif key > node.NodeKey:
                if node.RightChild is None:
                    result.Node = node
                    return result
                else:
                    node = node.RightChild
        return result

    def AddKeyValue(self, key, val):
        node = self.Root
        while node is not None:
            if node.NodeKey == key:
                return False
            elif key < node.NodeKey:
                if node.LeftChild is None:
                    node.LeftChild = BSTNode(key, val, node)
                    self.count += 1
                    return True
                node = node.LeftChild
            elif key > node.NodeKey:
                if node.RightChild is None:
                    node.RightChild = BSTNode(key, val, node)
                    self.count += 1
                    return True
                node = node.RightChild
        self.Root = BSTNode(key, val, None)
        self.count += 1
        return True
    
    def FinMinMax(self, FromNode, FindMax):
        if self.Root is not None:
            if FindMax:
                while FromNode.RightChild is not None:
                    FromNode = FromNode.RightChild
            else:
                while FromNode.LeftChild is not None:
                    FromNode = FromNode.LeftChild
            return FromNode

    def FindPrePostNode(self, node):
        if node.RightChild is not None:
            return self.FinMinMax(node.RightChild, False)
        parent = node.Parent
        while parent is not None and node == parent.RightChild:
            node = parent
            parent = parent.Parent
        return parent
    
    def FindNewNode(self, node):
        new_node = None
        if node.LeftChild == None or node.RightChild == None:
            new_node = node
        else:
            new_node = self.FindPrePostNode(node)
        return new_node
    
    def FindNewChild(self, node):
        new_child = None
        if node.LeftChild != None:
            new_child = node.LeftChild
        else:
            new_child = node.RightChild
        return new_child
    
    def ConnectParentAndChild(self, new_node, new_child):
        if new_child != None:
            new_child.Parent = new_node.Parent
        if new_node.Parent == None:
            self.Root = new_child
        elif new_node == new_node.Parent.LeftChild:
            new_node.Parent.LeftChild = new_child
        else:
            new_node.Parent.RightChild = new_child
    
    def DeleteNodeByKey(self, key):
        # Find the removed node
        node = self.FindNodeByKey(key).Node
        if node.NodeKey != key:
            return False
    
        # Find new_node instead of the removed node
        new_node = self.FindNewNode(node)
        
        # Find a child of the new_node
        new_child = self.FindNewChild(new_node)
        
        # Connect a new_node.Children 
        # with new_node.Parent
        self.ConnectParentAndChild(new_node, new_child)

        # Change key and value of the removed 
        # node with new_node
        if new_node != node:
            node.NodeKey = new_node.NodeKey
            node.NodeValue = new_node.NodeValue
        self.count -= 1
        return True
    
    def Count(self):
        if self.count and self.Root is None:
            self.count -= 1
        return self.count
