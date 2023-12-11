"""
Structs_lib its primitive studyind-porpouse handmade library of data structures
"""
from typing import Any

class MyStack:
    """simple Stack realization"""

    def __init__(self) -> None:
        """stack contains its body as empty list with its length=0"""
        self.body=[]
        self.length=0
    def pop(self)->Any:
        """pop() method returns last item from the stack O(1),if its empty panics with IndexError"""
        if self.length >0:
            self.length-=1
            poped=self.body.pop()
            return poped
        else:
            raise IndexError
    def push(self,item:Any)->None:
        """push() method adds element to the end of the stack body O(1)"""
        self.body.append(item)
        self.length+=1
class MyQueue:
    """No reasons to use due to faster and more functional MyDeque.
    bad queue realization. MyDeque has much better perfomanse due to be a double linked list not a array
    and also MyDeque has all functionality of queue,so ill just leave it to be"""

    def __init__(self) -> None:
        """queue contains its body as empty list and its length=0"""
        self.body=[]
        self.length=0        
    def add(self,item):
        """add element to the end of queue in O(N)"""
        self.body.insert(0,item)
        self.length+=1
    def take(self):
        """removes and gets first inserted item from the queue in  O(1) if queue is empty return None"""
        if self.length >0:
            return self.body.pop()
        else:
            return None
class MyDeque:
    """simple double linked list implementation,contain length of itself """

    def __init__(self) -> None:
        """initialize epty deque"""
        self.last=None
        self.first=None
        self.length=0 
    def add_last(self,data:Any):
        """adds element after last element in list in O(1)"""
        added_node=self.NodeForLinkedList(data)
        if self.last==None:#empty list
            self.last=added_node
            self.first=added_node
            self.length+=1           
        else:#not empty
            self.last.next_node=added_node
            added_node.previos_node=self.last
            self.last=added_node
            self.length+=1
    def __iter__(self)->iter:
        return self.LinkedListIterator(self.first)       
    def add_first(self,data:Any)->None:
        """adds element before first element in list in O(1)"""
        added_node=self.NodeForLinkedList(data)
        if self.first==None:#empty list
            self.last=added_node
            self.first=added_node
            self.length+=1           
        else:#not empty
            self.first.previos_node=added_node
            added_node.next_node=self.first
            self.first=added_node
            self.length+=1   
    def __str__(self) -> str:
        returned='<-'
        for node in self:
            returned=''.join([returned,str(node),','])
        return returned[:-1]+'->'
    def get_last(self)->Any:
        """returns and deletes.last element from list in O(1) if list is empty returns None"""
        if self.length==0:#empty list
            extracted=None
        elif self.length==1:#one element
            extracted=self.last.data
            self.first=None
            self.last=None
            self.length-=1
        else:#general case
            extracted=self.last.data
            self.last=self.last.previos_node
            self.last.next_node=None
            self.length-=1
        return extracted
    def get_first(self)->Any:
        """returns first added element in O(1)if list is emtp returns None"""
        if self.length==0:#empty list
            extracted=None
        elif self.length==1:#one element
            extracted=self.last.data
            self.first=None
            self.last=None
            self.length-=1
        else:#general case
            extracted=self.first.data
            self.first=self.first.next_node
            self.first.previos_node=None
            self.length-=1
        return extracted
    def search(self,data:Any):
        """returns true if data is in list in O(N) else-false"""
        current=self.first
        while current!=None:
            if current.data==data:                
                return True
            current=current.next_node
        return False
    def delete(self,data:Any):
        """delete data from the list in O(N)"""
        current=self.last
        while current!=None:
            if current.data==data:
                if current.previos_node!=None and current.next_node!=None:#common case
                    current.previos_node.next_node=current.next_node
                    current.next_node.previos_node=current.previos_node
                if current.previos_node==None and current.next_node==None:#only 1 element in list
                    self.last=None
                    self.first=None
                if current.previos_node!=None and current.next_node==None:#last inserted element
                    self.last=current.previos_node
                    self.last.next_node=None
                if current.previos_node==None and current.next_node!=None:#first inserted element
                    self.first=current.next_node
                    current.next_node.previos_node=None #ALL ABOVE LOOKS HORRIBLE REFACTOR LATER
                self.length-=1
            current=current.previos_node
    def insert(self,data:Any,index:int):
        """inserts element  in index position in list in O(N) raises IndexError if index>length or index<0"""
        if index>self.length or index<0:
            raise IndexError
        if self.length==0 or index==0: #insertion in empty list or without displace
            self.add_first(data)
            return
        if self.length==index:#insertion after last element of list
            self.add_last(data)   
        else:#common case
            inserted_data=self.NodeForLinkedList(data)
            current=self.first
            for i in range(index-1):#between current and current.next_node
                current=current.next_node
            inserted_data.next_node=current.next_node
            inserted_data.previos_node=current
            current.next_node.previos_node=inserted_data
            current.next_node=inserted_data
            self.length+=1
    def rotate(self)->None:
        """displase linked list forvard 
        node1,node2...nodeN-1,nodeN--->>> nodeN,node1,node2...nodeN-1
         O(1)  """        
        if self.length==0 or self.length==1:
            return
        new_first=self.last
        self.get_last()
        self.add_first(new_first.data) 
    class LinkedListIterator:
        def __init__(self,first) -> None:
            self.current=first
        def __iter__(self):
            return self
        def __next__(self):
            if self.current==None:
                raise StopIteration
            else:
                data=self.current.data
                self.current=self.current.next_node
                return data
    class NodeForLinkedList:
        """class to store data in linked list """

        def __init__(self,data=None) -> None:
            """Node contains 3 fields(data,next node,previous node) constructor gets data to insert inside node or sets it to None """
            self.data=data
            self.next_node=None
            self.previos_node=None  
class NaiveHashMap:
    """simple hash map implementation. methods works in O(1) while map is not overfilled,else O(N)"""

    def MyHash(self,key:Any)->int:
        tmp=str(key)
        size=self.size
        sum=0
        for i in tmp:
            sum=sum+ord(i) 
        place= sum%size        
        return place    
    def __init__(self,size:int) -> None:
        """initialize hash map by given size if size is not correct raises assertion error"""
        assert(size>0)
        assert(type(size)==int)
        self.size=size
        self.body=[None]*(size)
        self.n_keys=0
    def __str__(self) -> str:
        returned='|||'
        for (k,v) in self:
            returned=''.join([returned,'{',str(k),':',(','.join(str(value) for value in v)),'}',';'])
        return returned[:-1]+'|||'
    def __iter__(self)->iter:
        for cell in self.body:
            if cell==None:
                continue
            for pair in cell:
                yield pair  
    def set(self,key:Any,value:Any) -> None:
        """set value to the key,if key is already exist replace it O(1) if where aro not many collisions in map"""
        self.delete_key(key)
        self.add(key,value)                
    def add(self,key:Any,value:Any) -> None:
        """adds to hashmap pair (key,value) in O(1) adds value to key if key is already exists"""
        index=self.MyHash(key)        
        if self.body[index]==None:
            self.body[index]=[[key,[value]]]
            self.n_keys+=1            
        else:
            for (k,v) in self.body[index]:
                if k==key:
                    v.append(value)
                    return
            self.body[index].append([key,[value]])
            self.n_keys+=1                      
    def get(self,key:Any)-> list:
        """returns all values assigned to key  O(1) if where is little collisions in map.
        if key is not in map returns KeyError"""
        index=self.MyHash(key)
        if self.body[index]==None:
            raise KeyError
        else:
            for (k,v) in self.body[index]:
                if k==key:
                    return v
            raise KeyError                    
    def delete_pair(self,key:Any,value:Any) -> None:
        """deletes pair key value from map in 0(1) if where is little coliision in map ,
        if key had several values the rests will remain."""
        index=self.MyHash(key)
        if self.body[index]==None:
            return
        else:
            for (k,v) in self.body[index]:
                if k==key and value in v:
                    v.pop(v.index(value))
                    if len(v)==0:
                        self.delete_key(key)                
                if self.body[index]==[]:self.body[index]=None
    def delete_key(self,key:Any) -> None:
        """deletes all values assigned to the key in 0(1) if where are not many collisions"""
        index=self.MyHash(key)
        if self.body[index]==None:
            return
        else:
            indx=0
            for (k,v) in self.body[index]:
                if key==k:
                    self.body[index].pop(indx)
                    self.n_keys-=1
                    if self.body[index]==[]:self.body[index]=None                    
                    return
                indx+=1
    def debug(self) -> None:
        print(self.body)
        print('n_positions=',len(self.body))
        print('n_keys=',self.n_keys)
class Matrix_as_list_of_lists:
    """simple matrix [[e00 e01...e0(j-1)], [e10 e11...e1(j-1)]...[e(i-1)0 e(i-1)1...e(i-1)(j-1)]]
    each line is array inside main array i-index in main array(represents row) 
    j-index in array inside(represents column)"""

    def __init__(self,rows:int=1,columns:int=1) -> None:
        """initialize be number of rows and columns raises assertion error if numbers are incorrect"""
        assert(rows>0 and columns>0)
        assert(type(rows)==int and type(columns==int))
        self.rows=rows
        self.columns=columns
        self.body=[]
        for i in range(rows):
            row=[]
            for j in range(columns):
                row.append(None)
            self.body.append(row)
    def add_column(self)->None:
        for row in self.body:
            row.append(None)
        self.columns+=1
    def add_row(self)->None:
        self.body.append([None]*self.columns)
        self.rows+=1
    def __str__(self) -> str:
        returned=''
        for row in self.body:
            for column in row:
                returned=returned+'|'+str(column)+' |'
            returned=returned+'\n'
        return returned[:-1]
    def __iter__(self)->iter:
        for row in self.body:
            for column in row:
                yield column
    def place_data(self,data,row:int,column:int)->None:
        """places data in sertain position in matrix if index out of bound raises assertion error
        first element in matrix has index[0][0] last-index[rows-1][columns-1]
          O(1)"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        self.body[row][column]=data
    def get_data(self,row:int,column:int)->Any:
        """gets data from matrix if indexes are nor correct raises assertion error
          O(1)"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        extracted=self.body[row][column]
        return extracted
class Matrix_linearized:
    def __init__(self,rows:int=1,columns=1) -> None:
        """initialize matrix as dynamic array raises assertionError if rows or columns are incorrect
        matrix will have this representstion:
        [e00, e01...e0(j-1), e10, e11...e1(j-1)...e(i-1)0, e(i-1)1...e(i-1)(j-1)"""

        assert(rows>0 and columns>0)
        assert(type(rows)==int and type(columns==int))
        self.rows=rows
        self.columns=columns
        self.body=[None]*rows*columns
    def __str__(self) ->str:
        returned=''
        for (index,item) in enumerate(self.body):
            if ((index+1)%(self.columns))==0:
                returned=returned+f'|{item}|\n'
            else:
                returned=returned+f'|{item}|'
        return returned
    def __iter__(self)->iter:
        "iterates row-wise"
        for elem in self.body:
            yield elem
    def add_row(self)->None:
        """adds row into matrix in 0(N) where N-number of columns in matrix"""
        for i in range(self.columns):
            self.body.append(None)
        self.rows+=1
    def add_column(self)->None:
        """adds column into matrix in 0(M*N)~O(N*2) where N-number of columns M-number of rows"""
        displace=0
        for row in range(self.rows):
            self.body.insert((self.columns-1+displace),None)
            displace+=1
        self.columns+=1
    def place_data(self,data:Any,row:int,column:int)->None:
        """places data in sertain position in matrix if index out of bound raises assertion error
        first element in matrix has index[0][0] last-index[rows-1][columns-1]
          O(1)"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        index=self.columns*row+column
        self.body[index]=data
    def get_data(self,row:int,column:int)->Any:
        """gets data by index in O(1) if cell is empty returns None. If index are incorrect returns assertion error"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        index=self.columns*row+column
        data=self.body[index]
        return data
class MHeap:
    """simple Heap implementation only for keys represented by int,else raises assertion error
    smallest key on top of heap"""

    class pair:
        """pair key,data for heap"""

        def __init__(self,key:int,value:Any) -> None:
            assert(type(key)==int)
            self.key=key
            self.value=value           
    def __init__(self) -> None:
        """initialize as emty dyn array and number of elements=0"""
        self.body=[]
        self.number_of_items=0
    def add_pair(self,key:int,data:Any='')->None:#temporaly stores default data for debugging
        """add pair to the heap works only for int keys else assertonError. O(logN)"""
        assert(type(key)==int)
        appended=self.pair(key,data)
        self.body.append(appended)
        self.number_of_items+=1
        self.place_correct(self.number_of_items)#giving as arg position(index+1) of element
    def place_correct(self,position:int)->None:#NOT INDEX
        if self.number_of_items==0 or self.number_of_items==1:
            return
        while position>1:
            if self.body[position-1].key<self.body[position//2-1].key:
                (self.body[position-1],self.body[position//2-1])=(self.body[position//2-1],self.body[position-1])
                 #comparing element with its parent and replasing if parent bigger than element
            position=position//2
    def dbg(self)->None:
        i=0
        for (index,pair) in enumerate(self.body):
            print(pair.key,end=' ')
            if index==i:
                print('\n',end='')
                i=i*2+2
        print('')
    def get_min(self)->pair:#temporaly returns only pair.key for debugging
        """delete and return min value from heap if heap is empty raises value error"""
        pass

            
        





    



    
        

        

                    


    




