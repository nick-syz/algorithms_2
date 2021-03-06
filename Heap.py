# https://skillsmart.ru/algo/15-121-cm/dfb9a4b3bf.html

class Heap:

    def __init__(self):
        self.HeapArray = []
    
    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2**(depth+1)-1)
        for i in a:
            self.Add(i)
    
    def GetMax(self):
        if len(self.HeapArray) and self.HeapArray[0] is not None:
            max_key = self.HeapArray[0]
            i = len(self.HeapArray)-1
            while i > 0:
                if self.HeapArray[i] is not None:
                    break
                i -= 1
            if i != 0:
                self.HeapArray[0], self.HeapArray[i] = \
                    self.HeapArray[i], None
                self.SiftDown(0, self.HeapArray)
            else:
                self.HeapArray[0] = None
            return max_key
        return -1
    
    def Swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = \
            self.HeapArray[j], self.HeapArray[i]

    def SiftDown(self, i, array):
        left = 2*i+1
        right = 2*i+2
        largest = i
        size = len(array)
        if left < size:
            if array[left] is not None and array[left] > array[largest]:
                largest = left
        if right < size:
            if array[right] is not None and array[right] > array[largest]:
                largest = right
        if largest != i:
            self.Swap(largest, i)
            return self.SiftDown(largest, array)
    
    def SiftUp(self, i):
        while self.HeapArray[(i-1)//2] is None or \
                self.HeapArray[i] > self.HeapArray[(i-1)//2]:
            self.Swap((i-1)//2, i)
            i = (i-1)//2
            if (i-1)//2 < 0:
                break

    def Add(self, key):
        i = len(self.HeapArray)-1
        if self.HeapArray[i] is None:
            self.HeapArray[i] = key
        else:
            while i > 0:
                i -= 1
                if self.HeapArray[i] is None:
                    break
            if i == 0:
                return False
            self.HeapArray[i] = key
        self.SiftUp(i)
        return True
