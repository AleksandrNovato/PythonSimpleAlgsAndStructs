"""
Structs_lib its primitive studyind-porpouse handmade library of data structures
"""

class MyStack:
    """Stack realization"""

    def __init__(self) -> None:
        """stack contains its body as empty list with its length=0"""
        self.body=[]
        self.length=0
    def pop(self):
        """pop() method returns last item from the stack O(1),if its empty panics with IndexError"""
        if self.length >0:
            self.length-=1
            poped=self.body.pop()
            return poped
        else:
            raise IndexError
    def push(self,item):
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
        self.last=None
        self.first=None
        self.length=0 
    def add_last(self,data):
        """adds element after last element in list in O(1)"""
        added_node=NodeForLinkedList(data)
        if self.last==None:#empty list
            self.last=added_node
            self.first=added_node
            self.length+=1           
        else:#not empty
            self.last.next_node=added_node
            added_node.previos_node=self.last
            self.last=added_node
            self.length+=1
    def __iter__(self):
        return LinkedListIterator(self.first)       
    def add_first(self,data):
        """adds element before first element in list in O(1)"""
        added_node=NodeForLinkedList(data)
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
    def get_last(self):
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
    def get_first(self):
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
    def search(self,data):
        """returns true if data is in list in O(N)"""
        current=self.first
        while current!=None:
            if current.data==data:                
                return True
            current=current.next_node
        return False
    def delete(self,data):
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
    def insert(self,data,index:int):
        """inserts element  in index position in list in O(N) raises IndexError if index>length or index<0"""
        if index>self.length or index<0:
            raise IndexError
        if self.length==0 or index==0: #insertion in empty list or without displace
            self.add_first(data)
            return
        if self.length==index:#insertion after last element of list
            self.add_last(data)   
        else:#common case
            inserted_data=NodeForLinkedList(data)
            current=self.first
            for i in range(index-1):#between current and current.next_node
                current=current.next_node
            inserted_data.next_node=current.next_node
            inserted_data.previos_node=current
            current.next_node.previos_node=inserted_data
            current.next_node=inserted_data
            self.length+=1
    def rotate(self):
        """displase linked list forvard in n positions 
        node1,node2...nodeN-1,nodeN--->>> nodeN,node1,node2...nodeN-1
         O(1)  """        
        if self.length==0 or self.length==1:
            return
        new_first=self.last
        self.get_last()
        self.add_first(new_first.data)        
class NodeForLinkedList:
    """class to store in linked list"""

    def __init__(self,data=None) -> None:
        """Node contains 3 elemetns(data,next node,previous node) constructor gets data to insert inside node or sets it to None """
        self.data=data
        self.next_node=None
        self.previos_node=None
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
class NaiveHashMap:
    """simple hash map implementation. methods works in O(1) while map is not overfilled,else O(N)"""

    def MyHash(self,key):
        tmp=str(key)
        size=self.size
        sum=0
        for i in tmp:
            sum=sum+ord(i) 
        place= sum%size        
        return place    
    def __init__(self,size:int) -> None:
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
    def __iter__(self):
        for cell in self.body:
            if cell==None:
                continue
            for pair in cell:
                yield pair  
    def set(self,key,value) -> None:
        """set value to the key,if key is already exist replace it O(1) if where aro not many collisions in map"""
        self.delete_key(key)
        self.add(key,value)                
    def add(self,key,value) -> None:
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
    def get(self,key)-> list:
        """returns all values assigned to key  O(1) if where is little collisions in map.if key is not in map returns KeyError"""
        index=self.MyHash(key)
        if self.body[index]==None:
            raise KeyError
        else:
            for (k,v) in self.body[index]:
                if k==key:
                    return v
            raise KeyError                    
    def delete_pair(self,key,value) -> None:
        """deletes pair key value from map in 0(1) if where is little coliision in map ,if key had several values the rests will remain."""
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
    def delete_key(self,key) -> None:
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
    """simple matrix [[e11 e12...e1j], [e21 e22...e2j]...[ei1 ei2...eij]]
    each line is array inside main array i-index in main array(represents row) 
    j-index in array inside(represents column)"""

    def __init__(self,rows:int=1,columns:int=1) -> None:
        """initialize be number of rows and columns"""
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
    def add_column(self):
        for row in self.body:
            row.append(None)
        self.columns+=1
    def add_row(self):
        self.body.append([None]*self.columns)
        self.rows+=1
    def __str__(self) -> str:
        returned=''
        for row in self.body:
            for column in row:
                returned=returned+'|'+str(column)+' |'
            returned=returned+'\n'
        return returned[:-1]
    def __iter__(self):
        for row in self.body:
            for column in row:
                yield column
    def place_data(self,data,row:int,column:int):
        """places data in sertain position in matrix if index out of bound raises assertion error
        first element in matrix has index[0][0] last-index[rows-1][columns-1]
          O(1)"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        self.body[row][column]=data
    def get_data(self,row:int,column:int):
        """gets data from matrix if indexes are nor correct raises assertion error
          O(1)"""
        assert(row>=0 and row<=self.rows-1 and column>=0 and column<=self.columns-1)
        assert(type(row)==int and type(column==int))
        extracted=self.body[row][column]
        return extracted
class Matrix_linearized:
    def __init__(self) -> None:
        pass
        

                    


    




