
import unittest 
import random
import sys 
import string
#sys.path.append("../PythonSimpleAlgsAndStructs/lib")
import Structs_lib as sl

"""Tests for Structs_lib"""

class Test_Structs_lib(unittest.TestCase):

    def test_Stack(self):
        for i in range(100):
            stack=sl.MyStack()
            random.seed()
            number_of_items=random.randint(1,1000)
            for i in range(number_of_items):
                last_pushed=random.randint(-100000,100000)
                stack.push(last_pushed)
            #filling our stack      
            self.assertEqual(last_pushed,stack.pop())#stack returns correct element
            for i in range(number_of_items-1):
                stack.pop()
            with self.assertRaises(IndexError):
                stack.pop()#stack panics
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
                #filling our deque
                self.assertEqual(added_first,l.get_first())
                self.assertEqual(added_last,l.get_last())
                #get_first(),add_first(),get_last(),add_last() works corecctly
            self.assertEqual(l.get_first(),None)
            self.assertEqual(l.get_last(),None)
            #make sure we extracted all items,there is nothin unexpected in deque

            number_of_items=random.randint(0,1000)
            place_of_insertion=random.randint(0,number_of_items)
            #picking place of insertion
            for i in range(number_of_items):
                l.add_last(random.randint(-10000,10000))
            #filling our deque again
            l.insert('!',random.randint(0,number_of_items))
            self.assertEqual(True,l.search('!'))
            l.delete('!')
            self.assertEqual(False,l.search('!'))
            #insert() and delete() inserts and deletes
            l2=sl.MyDeque()
            check_list=[]
            for i in range(number_of_items):
                l2.add_last(i)
                check_list.append(i)
            #filling queue with sequential numbers from 1 to randint
            from_gen=[number for number in l2]
            self.assertEqual(check_list,from_gen)
            #__Iter__() works correctly
            l2.rotate()
            from_gen=[number for number in l2]
            check_list.insert(0,check_list.pop())
            self.assertEqual(check_list,from_gen)
            #rotate works correctly
    def test_Hash(self):
        for i in range(100):
            random.seed()
            h=sl.NaiveHashMap(random.randint(1,100))
            #creating testing hash map
            random_pairs=[]
            for i in range(random.randint(1,100)):
                random_pairs.append((''.join(random.choices(string.ascii_letters,k=random.randint(0,10))),
                                    ''.join(random.choices(string.ascii_letters,k=random.randint(0,100)))))
                #creating a list of random pairs [(key0,value0)....(keyN,valueN)]
            for (k,v) in random_pairs:
                h.add(k,v)
                #filling our hashmap with random values to test pretty filled map
            added_pair=(''.join(random.choices(string.ascii_letters,k=random.randint(0,10))),
                                    [''.join(random.choices(string.ascii_letters,k=random.randint(0,100)))])
                #creating testing pair (key,[value])
            h.add(added_pair[0],added_pair[1])
            self.assertTrue(added_pair[1] in h.get(added_pair[0]))
            #checking if h.get() will find our value by key
            h.add(added_pair[0],'another value')
            self.assertTrue(added_pair[1] and 'another value' in h.get(added_pair[0]))
            #checking if h.get() will find another added walue too
            h.delete_pair(added_pair[0],'another value')
            self.assertFalse('another value' in h.get(added_pair[0]))
            self.assertTrue(added_pair[1] in h.get(added_pair[0]))
            #checking if h.delete_pair() will delete only 1 value not all of them
            h.delete_key(added_pair[0])
            with self.assertRaises(KeyError):
                h.get(added_pair[0])
            #checking if h.delete_key() actually deleted key and all values. Also thar h.get() will cause KeyError
            for i in range(10):
                h.add(added_pair[0],i*i%(i+3))
            h.set(added_pair[0],'the only value')
            self.assertTrue(len(h.get(added_pair[0]))==1 and 'the only value' in h.get(added_pair[0]) )
            #check if h.set() will delete all values and insert only one we need
            h_iter=sl.NaiveHashMap(random.randint(1,10))
            pairs_added=[]
            for i in range(random.randint(1,10)):
                h_iter.add(i,'value'+str(i))
                pairs_added.append([i,[f'value{str(i)}']])
            for pair in h_iter:
                if pair in pairs_added:
                    pairs_added.pop(pairs_added.index(pair))
                    continue
                else:
                    raise KeyError
            if pairs_added!=[]:
                raise ValueError
            #checing if __iter__() method returns all added pairs correct
    def test_Matrix_L_of_L(self):
        for i in range(100):
            random.seed()
            rows=random.randint(1,100)
            columns=random.randint(1,100)
            m=sl.Matrix_as_list_of_lists(rows,columns)
            self.assertEqual(m.body,[[None]*columns]*rows)
            with self.assertRaises(AssertionError):
                m2=sl.Matrix_as_list_of_lists(random.randint(-100,0),random.randint(-100,0))
            #initialize and check correct initialization
            m.add_column()
            m.add_row()
            self.assertEqual(m.body,[[None]*(columns+1)]*(rows+1))
            #add row and column works correctly
            row=random.randint(0,rows-1)
            column=random.randint(0,columns-1)
            m.place_data('data',row,column)
            self.assertEqual('data',m.body[row][column])
            self.assertEqual(m.get_data(row,column),'data')
            #palce_data() and get_data() works correctly

                        
                
    
            
            
            
                   

if __name__=='__main__':
    unittest.main()



 
        