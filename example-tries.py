from utils import *

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
