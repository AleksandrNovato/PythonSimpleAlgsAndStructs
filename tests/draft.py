import Structs_lib as sl

l=sl.MyDoubleLinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)

l.print_list()

l.insert('o',4)
print(l.search('o'))
l.delete('0')
print(l.search('0'))


