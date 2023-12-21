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
tree.delete_key(-100)
tree.print_bfs()






            
