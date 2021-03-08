# https://skillsmart.ru/algo/15-121-cm/dfb9a4b3bf.html

class Heap:

    def __init__(self):
        self.HeapArray = []
        self.count = 0
        self.free_pos = None
    
    def Swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = \
            self.HeapArray[j], self.HeapArray[i]

    def SiftDown(self, i, array):
        left = 2*i+1
        right = 2*i+2
        largest = i
        size = len(array)
        if left < size and array[left] != None and array[left] > array[largest]:
            largest = left
        if right < size and array[right] != None and array[right] > array[largest]:
            largest = right
        if largest != i:
            self.Swap(largest, i)
            return self.SiftDown(largest, array)

    def SiftUp(self, i):
        while i > 0 and (self.HeapArray[(i-1)//2] is None or \
                self.HeapArray[i] > self.HeapArray[(i-1)//2]):
            self.Swap((i-1)//2, i)
            i = (i-1)//2

    def MakeHeap(self, array, depth):
        if len(array) <= (2**(depth+1)-1):
            self.HeapArray = array[:]
            self.count = len(array)
            length = 2**(depth+1)-1
            for i in range(length-len(array)):
                self.HeapArray.append(None)
            for key in range(self.count-1,-1,-1):
                self.SiftUp(key)
            if len(array) < len(self.HeapArray):
                self.free_pos = len(array)

    def GetMax(self):
        if self.count:
            max_key = self.HeapArray[0]
            i = self.count-1
            self.HeapArray[0], self.HeapArray[i] = \
                self.HeapArray[i], None
            self.SiftDown(0, self.HeapArray)
            self.count -= 1
            return max_key
        return -1
    
    def Add(self, key):
        if self.count == len(self.HeapArray):
            return False
        i = self.free_pos
        if i < len(self.HeapArray)-1:
            self.free_pos += 1
        else:
            self.free_pos = None
        self.count += 1
        self.HeapArray[i] = key
        self.SiftUp(i)
        return True
    
    def CheckHeap(self, i=0):
        left = 2*i+1
        right = 2*i+2
        array = self.HeapArray
        size = len(array)
        if left < size and array[left] != None and array[left] > array[i]:
            return False
        if right < size and array[right] != None and array[right] > array[i]:
            return False
        if 2*i+1 < size:
            return self.CheckHeap(2*i+1)
        if 2*i+2 < size:
            return self.CheckHeap(2*i+2)
        return True
