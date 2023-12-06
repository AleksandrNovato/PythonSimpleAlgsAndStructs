
import unittest 
import random
import sys 
#sys.path.append("../PythonSimpleAlgsAndStructs/lib")
import Structs_lib as sl

"""Tests for Structs_lib"""

class Test_Structs_lib(unittest.TestCase):

    def test_Stack(self):
        for i in range(10):
            last_pushed=None
            random.seed()
            stack=sl.MyStack()
            number_of_items=random.randint(1,1000)
            for i in range(number_of_items):
                last_pushed=random.randint(-100000,100000)
                stack.push(last_pushed)      
            self.assertEqual(last_pushed,stack.pop())#stack returns correct element
            for i in range(2*number_of_items):
                stack.pop()
            self.assertEqual(None,stack.pop())#stack returns None if its empty

    def test_Queue(self):
        for i in range(10):
            random.seed()
            queue=sl.MyQueue()
            self.assertEqual(None,queue.take())#queue returns None if its empty
            number_of_items=random.randint(1,1000)

            first=random.randint(-120120,212123)
            queue.add(first)
            for i in range(number_of_items):
                queue.add(random.randint)
            self.assertEqual(first,queue.take())#queue returns correct element

    def test_Deque(self):
    
        for i in range(100):
            l=sl.MyDeque()
            
            random.seed()
            number_of_items=random.randint(0,1000)
            for i in range(number_of_items):
                added_first=random.randint(-10000,1000)
                l.add_first(added_first)
                added_last=random.randint(-10000,1000)
                l.add_last(added_last)
                self.assertEqual(added_first,l.get_first())
                self.assertEqual(added_last,l.get_last())
            assert(l.get_first()==None)
            assert(l.get_last()==None)

            number_of_items=random.randint(0,1000)
            place_of_insertion=random.randint(0,number_of_items)
            for i in range(number_of_items):
                l.add_last(random.randint(-10000,10000))
            l.insert('!',random.randint(0,number_of_items))
            self.assertEqual(True,l.search('!'))
            l.delete('!')
            self.assertEqual(False,l.search('!'))             

    def test_Hash(self):
        pass
if __name__=='__main__':
    unittest.main()



 
        