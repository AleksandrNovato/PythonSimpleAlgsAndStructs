import Structs_lib as sl
tree=sl.BinaryTreeOfSearch()
tree.add_pair(0,'zero')
tree.add_pair(-2,'minus two')
tree.add_pair(2,'two')
tree.add_pair(-4,'minus four')
tree.add_pair(-3,'minus three')
tree.add_pair(1,'one')
tree.add_pair(3,'three')
tree.print_bfs()
#tree.delete_key(0)
tree.delete_key(10)
#tree.delete_key(2)
#tree.delete_key(-4)
#tree.delete_key(-3)
#tree.delete_key(1)
#tree.delete_key(3)
tree.print_bfs()






            
