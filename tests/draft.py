import Structs_lib as sl
m=sl.MHeap()
class pair:
        """pair key,data for heap"""

        def __init__(self,key:int,value=None) -> None:
            assert(type(key)==int)
            self.key=key
            self.value=value 
A=[]
for i in range(9,0,-1):
      A.append(pair(i))
m.buildHeap(A)
m.dbg()
print(m.get_min().value)












            
