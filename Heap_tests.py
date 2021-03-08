from Heap import Heap
from unittest import TestCase

class HeapTest(TestCase):
    def setUp(self):
        self.heap = Heap()
    
    def test_add(self):
        self.heap.MakeHeap([9, 8, 4, 6, 7, 3, 1, 2, 5], 3)
        self.assertTrue(self.heap.Add(11))
        
        self.assertTrue(self.heap.Add(12))

        for i in range(13, 17):
            self.assertTrue(self.heap.Add(i))
        
        self.assertFalse(self.heap.Add(100))
    
    def test_make(self):
        heap = Heap()
        self.assertEqual(0, heap.count)
        a = [9, 8, 4, 6, 7, 3, 1, 2, 5]
        heap.MakeHeap(a, 3)
        self.assertEqual(9, heap.count)

        for i in range(10, 16):
            self.assertTrue(heap.Add(i))
        self.assertEqual(15, heap.count)
        for i in range(15, 0, -1):
            self.assertEqual(i, heap.GetMax())
    
    def test_make1(self):
        heap = Heap()
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11]
        heap.MakeHeap(a, 3)

    def test_zero(self):
        self.assertEqual(-1, self.heap.GetMax())
    
    def test_make2(self):
        a = []
        for i in range(1, 15):
            a.append(i)
        self.heap.MakeHeap(a, 3)
        self.assertTrue(self.heap.Add(20))
        self.assertFalse(self.heap.Add(19))

        self.assertTrue(self.heap.CheckHeap())
        
        b = []
        for i in range(1, 15):
            b.append(i)
        self.heap.HeapArray = b[:]
        
        self.assertFalse(self.heap.CheckHeap())

    def test_add1(self):
        self.heap.HeapArray = [11, 9, 7, None, 8, 6, 3, None, None, None, None, 5, 4, 3, 2, 1]
        self.heap.count = 11
        j = 11
        for i in [21, 10, 45, 12, 19]:
            j += 1
            self.assertTrue(self.heap.Add(i))
            self.assertEqual(j, self.heap.count)

        self.assertFalse(self.heap.Add(24))
