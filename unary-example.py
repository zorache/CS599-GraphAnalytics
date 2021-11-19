from utils import *


# Joining Two Tries for first column
Tree = AVLTree()
root = None
root = Tree.insert(root, 1,1)
root = Tree.insert(root, 2,1)
root = Tree.insert(root, 3,3)
root = Tree.insert(root, 7, 1)

Tree2 = AVLTree()
root2 = None
root2 = Tree2.insert(root2, 0,1)
root2 = Tree2.insert(root2, 2,1)
root2 = Tree2.insert(root2, 4,3)
root2 = Tree2.insert(root2, 7, 1)

Iter = TreijoinIterator(Tree, root)
Iter_2 = TreijoinIterator(Tree2, root2)

frog = LeapfrogJoin(Iter,Iter_2)

frog.atEnd
print(frog.Iter[0].key)
print(frog.Iter[1].key)
while not frog.atEnd:
    frog.leapfrogNext()
frog.key
# Expected answer: [2,7]
