# https://skillsmart.ru/algo/15-121-cm/s9b9313o8b.html

class aBST:

    def __init__(self, depth):
        tree_size = self.depth_calc(depth)
        self.Tree = [None] * tree_size 
    
    def depth_calc(self, depth):
        n = 0
        for i in range(depth+1):
            n += 2**i
        return n

    def FindKeyIndex(self, key, i=0):
        if i >= len(self.Tree):
            return None
        elif self.Tree[i] is None:
            return -i
        if key < self.Tree[i]:
            return self.FindKeyIndex(key, 2*i+1)
        elif self.Tree[i] == key:
            return i
        else:
            return self.FindKeyIndex(key, 2*i+2)

    def AddKey(self, key):
        i = self.FindKeyIndex(key)
        if i is not None:
            if i <= 0 and self.Tree[i] != key:
                i = -i
                self.Tree[i] = key
        else:
            i = -1
        return i
