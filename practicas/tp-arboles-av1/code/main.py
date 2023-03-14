from avltree import *
from linkedlist import printL

B = AVLTree()

insertAVL(B,'A',15)
insertAVL(B,'C',22)
insertAVL(B,'B',8)
insertAVL(B,'F',17)
insertAVL(B,'D',3)
insertAVL(B,'E',12)
insertAVL(B,'I',19)
insertAVL(B,'G',32)
insertAVL(B,'J',18)
insertAVL(B,'H',7)

L = traverseBreadFirst(B)
printL(L)

h = search_h(B.root.rightnode)
print('La altura es ',h)