from trie import *  
from linkedlist import printL
from linkedlist import delete as deleteLL

MyTrie = Trie()
insert(MyTrie,'Hola')
insert(MyTrie,'Holas')
insert(MyTrie,'Gabi')
insert(MyTrie,'Holadee')
insert(MyTrie,'Holasaa')
insert(MyTrie,'Holasein')


#printL(MyTrie.root.children)
printTrie(MyTrie.root,'')


L = findPattern(MyTrie,'Hola',7)
printL(L)