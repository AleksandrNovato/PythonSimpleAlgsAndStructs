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
    """queue realization"""

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

class MyDoubleLinkedList:
    """simple double linked list implementation,contain length of itself"""

    def __init__(self) -> None:
        self.head=None
        self.length=0
    def add(self,data):
        "adds element after head element in list in O(1)"
        added_node=NodeForLinkedList(data)
        if self.head==None:
            self.head=added_node
            self.length+=1           
        else:
            self.head.next_node=added_node
            added_node.previos_node=self.head
            self.head=added_node
            self.length+=1
    def print_list(self):
        "showes content of list in order how whey will be extracted by func get() if its possible to print elements"
        current=self.head
        if current==None:print("list is empty")
        while current!=None:
            print(current.data,end=",")
            current=current.previos_node
        print('[',self.length,']','\n',end="")
    def get(self):
        "returns and deletes head element from list in O(1) if list is empty returns None"
        if self.length==0:
            extracted=None
        elif self.length==1:
            extracted=self.head.data
            self.head=None
            self.length-=1
        else:
            extracted=self.head.data
            self.head=self.head.previos_node
            self.head.next_node==None
            self.length-=1
        return extracted
    def search(self,data):
        "returns true if data is in list in O(N)"
        current=self.head
        while current!=None:
            if current.data==data:                
                return True
            current=current.previos_node
        return False
    def delete(self,data):
        "delete data from list in O(N)"
        current=self.head
        while current!=None:
            if current.data==data:
                if current.previos_node!=None and current.next_node!=None:#common case
                    current.previos_node.next_node=current.next_node
                    current.next_node.previos_node=current.previos_node
                if current.previos_node==None and current.next_node==None:#only 1 element in list
                    self.head=None
                if current.previos_node!=None and current.next_node==None:#last inserted element
                    self.head=current.previos_node
                    self.head.next_node=None
                if current.previos_node==None and current.next_node!=None:#first inserted element
                    current.next_node.previos_node=None #ALL ABOVE LOOKS HORRIBLE REFACTOR LATER
                self.length-=1
            current=current.previos_node
    def insert(self,data,index):
        "inserts element  after index elements of list in O(N) raises IndexError if index>length or index<0"
        if index>self.length or index<0:
            raise IndexError
        if self.length==0 or index==0: #insertion in empty list or without displace
            self.add(data)
            return
        inserted_data=NodeForLinkedList(data)
        if self.length==index:#insertion at tail of list
            current=self.head
            for i in range(index-1):#stop 1 earlier to not step into None
                current=current.previos_node
            inserted_data.next_node=current
            current.previos_node=inserted_data          
            self.length+=1   
        else:#common case
            current=self.head
            for i in range(index):
                current=current.previos_node
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
    



