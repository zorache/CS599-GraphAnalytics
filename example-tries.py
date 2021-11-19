from utils import *




### Joining Two Tries ###
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

# Answer is [2,7]


### Joining Three Tries ###

file_name_R = "data/Q3_3_R.csv"
file_name_S = "data/Q3_3_S.csv"
file_name_T = "data/Q3_3_T.csv"

Tree_R, root_R = TreeBuilder(file_name_R)
Tree_S, root_S = TreeBuilder(file_name_S)
Tree_T, root_T = TreeBuilder(file_name_T)

Iter_R = TreijoinIterator(Tree_R, root_R)
Iter_S = TreijoinIterator(Tree_S, root_S)
Iter_T = TreijoinIterator(Tree_T, root_T)

Join = LeapfrogTrieJoin(Iter_R,Iter_S, Iter_T)

# Answer is [7,4,5]

file_name_R = "data/Q3_3_R_1.csv"
file_name_S = "data/Q3_3_S_1.csv"
file_name_T = "data/Q3_3_T_1.csv"

Tree_R, root_R = TreeBuilder(file_name_R)

Tree_S, root_S = TreeBuilder(file_name_S)

Tree_T, root_T = TreeBuilder(file_name_T)

Iter_R = TreijoinIterator(Tree_R, root_R)
Iter_S = TreijoinIterator(Tree_S, root_S)
Iter_T = TreijoinIterator(Tree_T, root_T)

Join = LeapfrogTrieJoin(Iter_R,Iter_S, Iter_T)

# Answers are
# [7, 4, 0]
# [7, 4, 1]
# [7, 4, 2]


### Small TrieJoin Triangle counting example ###
Count = CountTriangles("data/test.txt",directed = True)
Count = CountTriangles("data/test.txt",directed = True)

# directed: 9    (3 unique)
# undirected: 24 (4 unique)


