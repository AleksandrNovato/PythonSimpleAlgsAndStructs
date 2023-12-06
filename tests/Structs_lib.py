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
        """pop() method returns last item from the stack O(1),if its empty returns None"""
        if self.length >0:
            self.length-=1
            poped=self.body.pop()
            return poped
        else:
            return None
    def push(self,item):
        """push() method adds element to the end of the stack body O(1)"""
        self.body.append(item)
        self.length+=1

class MyQueue:
    """bad queue realization MyDeque has much better perfomanse due to be a double linked list not a array"""

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
    """simple double linked list implementation,contain length of itself"""

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
    def print_list(self):
        """showes content of list only if elements of list can be arg for print() method"""
        current=self.first
        if current==None:print("list is empty")
        while current!=None:
            print(current.data,end=",")
            current=current.next_node
        print(f"[{self.length}]",'\n',end="")
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
  

class NodeForLinkedList:
    """class to store in linked list"""

    def __init__(self,data=None) -> None:
        """Node contains 3 elemetns(data,next node,previous node) constructor gets data to insert inside node or sets it to None """
        self.data=data
        self.next_node=None
        self.previos_node=None
    
class NaiveHashMap:
    """simple hash map implementation"""
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
        self.size=size
        self.body=[None]*(size)
        self.items=0
    def print_hash(self):
        """prints hash map if key and value can be args for print() method"""
        print(f"{self.body}")
    def insert(self,key,value):
        """adds to hashmap pair (key,value) in O(1) adds value to key if key is already exists"""
        index=self.MyHash(key)        
        if self.body[index]==None:
            self.body[index]=[(key,value)]
        else:
            for (key_old,value_old) in self.body[index]:
                if (key_old,value_old)==(key,value):
                    return
            self.body[index].append((key,value))          
    def get(self,key):
        "returns all values assigned to key  O(1) if where is little collisions in map.if key is not in map returns KeyError"
        index=self.MyHash(key)
        if self.body[index]==None:
            raise KeyError
        else:
            list_of_values=[]
            for (k,v) in self.body[index]:
                if k==key:
                    list_of_values.append(v)
            if list_of_values==[]:
                raise KeyError
            return list_of_values
                    
    def delete(self,key,value):
        "deletes pair key value from map in 0(1) if where is little coliision in map ,if key had several values the rests will remain."
        index=self.MyHash(key)
        if self.body[index]==None:
            return
        else:
            indx=0
            for (k,v) in self.body[index]:
                if (k,v)==(key,value):
                    self.body[index].pop(indx)
                indx+=1
            return
                    


    




