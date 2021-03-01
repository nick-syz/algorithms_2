# https://skillsmart.ru/algo/15-121-cm/j348z1ab7c.html
import math

class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

class BalancedBST:
    def __init__(self):
    	self.Root = None

    def GenerateBST(self, node, arr):
        if len(arr):
            i = (len(arr)-1)//2
            if self.Root is None:
                self.Root = BSTNode(arr[i], None)
                self.Root.Level = 1
                node = self.Root
            else:
                if arr[i] < node.NodeKey:
                    node.LeftChild = BSTNode(arr[i], node)
                    node = node.LeftChild
                else:
                    node.RightChild = BSTNode(arr[i], node)
                    node = node.RightChild
                node.Level += node.Parent.Level + 1
            self.GenerateBST(node, arr[:i])
            self.GenerateBST(node, arr[i+1:])

    def GenerateTree(self, a):
        a = sorted(a)
        self.GenerateBST(self.Root, a)
    
    def TreeDepth(self, node):
        if node is None:
            return 0
        left_depth = self.TreeDepth(node.LeftChild)
        right_depth = self.TreeDepth(node.RightChild)
        return max(left_depth, right_depth) + 1

    def IsBalanced(self, root_node):
        if root_node is not None:
            left = self.TreeDepth(root_node.LeftChild)
            right = self.TreeDepth(root_node.RightChild)
            if abs(left-right) > 1:
                return False
            if root_node.LeftChild is not None:
                return self.IsBalanced(root_node.LeftChild)
            if root_node.RightChild is not None:
                return self.IsBalanced(root_node.RightChild)
        return True

    def WideAllNodes(self):
        nodes = [self.Root]
        if self.Root is not None:
            for i in nodes:
                if i.LeftChild is not None:
                    nodes.append(i.LeftChild)
                if i.RightChild is not None:
                    nodes.append(i.RightChild)
        return nodes
