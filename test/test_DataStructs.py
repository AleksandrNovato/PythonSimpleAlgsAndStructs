
import unittest 
import random
import sys 
sys.path.append("../PythonSimpleAlgsAndStructs/lib")
import Structs_lib as sl

"""Tests for Structs_lib"""

class Test_Structs_lib(unittest.TestCase):

    def test_stack(self):
        
        last_pushed=None
        random.seed()
        stack=sl.MyStack()
        number_of_items=random.randint(1,100000)
        for i in range(number_of_items):
            last_pushed=random.randint(-100000,100000)
            stack.push(last_pushed)      
        self.assertEqual(last_pushed,stack.pop())
        for i in range(2*number_of_items):
            stack.pop()
        self.assertEqual(None,stack.pop())


if __name__=='__main__':
    unittest.main()



 
        