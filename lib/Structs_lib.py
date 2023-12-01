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
    def remove(self):
        """removes and gets first inserted item from the queue in  O(1) if queue is empty raise IndexError"""
        if self.length >0:
            return self.body.pop()
        else:
            raise IndexError

class MyLinkedList:
    """linked list implementation"""

    def __init__(self) -> None:
        """ linked list initializes head and tail with nones and end with ist length=0 """
        self.head=None
        self.tail=None
        self.length=0
    def dbg(self):
        current=self.tail
        while current!=None:
            print(current.data)
            current=current.next_node

    def add(self,data):
        """appens data to the end of linked list in O(1)"""
        packed_data=NodeForLinkedList(data)
        if self.head==None: 
            self.head=packed_data
            self.tail=packed_data
            self.length+=1
        else:        
            packed_data.set_previos(self.head)
            packed_data.set_next(None)
            self.head=packed_data
            self.length+=1

    def insert(self,element,data):
        """insert data before sertain element"""
        pass          
            
    def find(self,data):
        """returns true if data is in linked list O(N)"""
        current=self.tail
        flag=False
        while current!=None and flag==False:
            if current.data==data:
                flag = True
                return flag
            current=current.get_next()
        return flag                
    def delete(self,data):
        """deletes all elements with data from linked list,if it is not there does nothing O(N)"""
        current=self.tail
        while current!=None:
            if current.data==data:
                current.next_node.set_previos(current.previos_node.next_node)
                current.previos_node.set_next(current.next_node.previos_node)




class NodeForLinkedList:
    """class to store in linked list"""

    def __init__(self,data=None) -> None:
        """Node contains 3 elemetns(data,next node,previous node) constructor gets data to insert inside node or sets it to None """
        self.data=data
        self.next_node=None
        self.previos_node=None
    def get_data(self):
        """extract data from node"""
        return self.data
    def set_next(self,next):
        """link node to next node"""
        self.next_node=next
    def set_previos(self,previos):
        """link node to previos node"""
        self.previos_node=previos


