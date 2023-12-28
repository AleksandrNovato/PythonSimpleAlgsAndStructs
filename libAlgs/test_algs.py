import random 
import unittest
import algs

"""tests for algorithms"""

class test_algs(unittest.TestCase):
    def test_insert(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(-1000,1000) for i in range(random.randint(0,100))]
            compared=sorted(A)
            algs.insert_sort(A)
            self.assertEqual(compared,A)
    def test_bubble(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(-1000,1000) for i in range(random.randint(0,100))]
            compared=sorted(A)
            algs.bubble_sort(A)
            self.assertEqual(compared,A)
    def test_choice(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(-1000,1000) for i in range(random.randint(0,100))]
            compared=sorted(A)
            algs.choice_sort(A)
            self.assertEqual(compared,A)
    def test_count(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(0,10) for i in range(random.randint(0,100))]
            compared=sorted(A)
            b=algs.count_sort(A)
            self.assertEqual(compared,b)
    def test_TH(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(-1000,1000) for i in range(random.randint(0,100))]
            compared=sorted(A)
            algs.sort_TH(A)
            self.assertEqual(compared,A)
    def test_merge(self):
        for i in range(1000):
            random.seed()
            A=[random.randint(-1000,1000) for i in range(random.randint(0,100))]
            compared=sorted(A)
            algs.merge_sort(A)
            self.assertEqual(compared,A)

if __name__=='__main__':
    unittest.main()
