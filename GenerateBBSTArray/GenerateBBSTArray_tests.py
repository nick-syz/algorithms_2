from GenerateBBSTArray import GenerateBBSTArray
from unittest import TestCase
import random

class GenerateBBSTArrayTest(TestCase):
    def setUp(self):
        self.arr = [i for i in range(1, 16)]
        random.shuffle(self.arr)
        
        self.arr1 = [i for i in range(1, 2)]
        random.shuffle(self.arr1)

        self.arr2 = [i for i in range(1, 4)]
        random.shuffle(self.arr2)

        self.arr3 = [i for i in range(1, 8)]
        random.shuffle(self.arr3)

        self.arr4 = [i for i in range(1, 32)]
        random.shuffle(self.arr4)

    def test_generator(self):
        print(GenerateBBSTArray([]))
        self.assertEqual([None], GenerateBBSTArray([]))
        
        print(GenerateBBSTArray(self.arr1))
        self.assertEqual([1], GenerateBBSTArray(self.arr1))
        
        print(GenerateBBSTArray(self.arr2))
        self.assertEqual([2, 1, 3], GenerateBBSTArray(self.arr2))
        
        print(GenerateBBSTArray(self.arr3))
        self.assertEqual([4, 2, 6, 1, 3, 5, 7], GenerateBBSTArray(self.arr3))
        
        print(GenerateBBSTArray(self.arr))
        self.assertEqual([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], GenerateBBSTArray(self.arr))
        
        print(GenerateBBSTArray(self.arr4))
        self.assertEqual([16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31], GenerateBBSTArray(self.arr4))
