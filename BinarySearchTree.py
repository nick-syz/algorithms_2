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

    def FindNodeByKey(self, key):
        result = BSTFind()
        result.Node = self.Root
        if self.Root is None:
            return result
        if key < self.Root.NodeKey and self.Root.LeftChild is None:
            result.ToLeft = True
            return result
        elif key > self.Root.NodeKey and self.Root.RightChild is None:
            return result
        elif self.Root.NodeKey == key:
            result.NodeHasKey = True
            return result
        if key < self.Root.NodeKey:
            return BST(self.Root.LeftChild).FindNodeByKey(key)
        else:
            return BST(self.Root.RightChild).FindNodeByKey(key)
    
    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        if self.Root.NodeValue == val:
            return False
        if val < self.Root.NodeValue:
            if self.Root.LeftChild is None:
                self.Root.LeftChild = BSTNode(key, val, self.Root.Parent)
                return True
            return BST(self.Root.LeftChild).AddKeyValue(key, val)
        else:
            if self.Root.RightChild is None:
                self.Root.RightChild = BSTNode(key, val, self.Root.Parent)
                return True
            return BST(self.Root.RightChild).AddKeyValue(key, val)

    def FinMinMax(self, FromNode, FindMax):
        if self.Root is not None:
            if FindMax:
                while FromNode.RightChild is not None:
                    FromNode = FromNode.RightChild
            else:
                while FromNode.LeftChild is not None:
                    FromNode = FromNode.LeftChild
            return FromNode

    def DeleteNodeByKey(self, key):
        if self.Root.Parent is None and self.Root.NodeKey == key:
            self.Root = None
            return True
        if self.Root is None:
            return False
        if key < self.Root.NodeKey:
            if self.Root.LeftChild is not None:
                if self.Root.LeftChild.NodeKey == key:
                    self.Root.LeftChild = None
                    return True
                return BST(self.Root.LeftChild).DeleteNodeByKey(key)
        else:
            if self.Root.RightChild is not None:
                if self.Root.RightChild.NodeKey == key:
                    self.Root.RightChild = None
                    return True
                return BST(self.Root.RightChild).DeleteNodeByKey(key)

    def Count(self):
        count = 0
        if self.Root is not None:
            count += 1
            count += BST(self.Root.LeftChild).Count()
            count += BST(self.Root.RightChild).Count()
        return count
