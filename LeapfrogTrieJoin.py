from utils import *

class TreijoinIterator(object):
    def __init__(self,tree,root):
        self.tree = tree
        self.root = root
        self.current = self.tree.search(self.root, self.tree.min)
        self.key = self.current.key
        self.subtree = None
        self.parentroot = None

    def atEnd(self):
        if self.current == "Not found":
            return True
        else: 
            return False
    
    def next(self):
        self.current = self.tree.getNext(self.root,self.key)
        if not self.atEnd():
            self.key = self.current.key

    def seek(self,seekKey):
        self.current = self.tree.seek(self.root,seekKey)
        if not self.atEnd():
            self.key = self.current.key
    
    def open(self):
        subtree = self.current.subtree
        self.parentroot = self.root
        self.root = self.current.child_root
        node = subtree.search(self.current.child_root, subtree.min)
        self.current = node
        self.key = self.current.key
        self.subtree = subtree

    def up(self):
#         "closed!"
        node = self.subtree.parent
        self.current =node
        self.root = self.parentroot
        self.key = self.current.key
        
    def begin(self):
        self.current =self.tree.search(self.root, self.tree.min)
        self.key = self.current.key
        
        
class LeapfrogJoin():
    def __init__(self,Iter_1,Iter_2):
        self.iter_1 = Iter_1
        self.iter_2 = Iter_2
        self.key = []
        if self.iter_1.atEnd() or self.iter_2.atEnd():
            self.atEnd = True
            return 
        else:
            self.atEnd = False
            self.Iter = sorted([self.iter_1,self.iter_2], key=lambda iter: iter.key)    # was sorted!
            self.k = len(self.Iter)
            self.p = 0 
            self.leapfrogSearch()
    def leapfrogSearch(self):
        max = self.Iter[(self.p -1) % self.k].key
        while True:
            x = self.Iter[self.p].key
            if x==max:                                #All iter are at the same key 
                self.key.append(x)
                return
            else:
                self.Iter[self.p].seek(max)
                if self.Iter[self.p].atEnd():
                    self.atEnd = True 
                    return
                else:
                    max = self.Iter[self.p].key
                    self.p=(self.p + 1) % self.k
    
    def leapfrogNext(self):
        self.Iter[self.p].next()
        if self.Iter[self.p].atEnd():
            self.atEnd=True
        else:
            self.p=(self.p+1)% self.k
            self.leapfrogSearch()
    
   

class LeapfrogTrieJoin():
    # Assuming that variables are sorted such that (a, b), (b,c), (a,c)
    def __init__(self,Iter_1,Iter_2, Iter_3, Triangle = False):
        self.a = None
        self.b = None
        self.c = None
        self.count = 0
        self.Triangle = Triangle
        self.Join_A = LeapfrogJoin(Iter_1,Iter_3)     # find the first A key that matches
        while not self.Join_A.atEnd:
            self.a = self.Join_A.Iter[0].key
#             print("a b - a c  match")
#             print(self.a)
#             print("opening Iter_1")
            Iter_1.open()
            Iter_2.begin()
            self.Join_B = LeapfrogJoin(Iter_1, Iter_2)
            while not self.Join_B.atEnd:
                self.b = self.Join_B.Iter[0].key
                if Triangle and self.a==self.b:
                    self.Join_B.leapfrogNext() 
                    continue
#                 print("a b - b c  match")
#                 print(self.b)
#                 print("opening Iter_2")
                Iter_2.open()
#                 print("opening Iter_3")
                Iter_3.open()
                self.Join_C = LeapfrogJoin(Iter_2, Iter_3)
                while not self.Join_C.atEnd:
                    self.c = self.Join_C.Iter[0].key 
                    if Triangle and self.c==self.b:
                        self.Join_C.leapfrogNext() 
                        continue
                    if Triangle and self.c==self.a:
                        self.Join_C.leapfrogNext() 
                        continue
                    print([self.a,self.b,self.c])
                    self.count +=1
                    self.Join_C.leapfrogNext()
#                 print("closing Iter_2")
                Iter_2.up()
#                 print("closing Iter_3")
                Iter_3.up()
                self.Join_B.leapfrogNext() 
#             print("closing Iter_1")
            Iter_1.up()
            self.Join_A.leapfrogNext()                     



class CountTriangles():
    def __init__(self,edge_list,directed=True):
        if "txt" in edge_list:
            txt = True
            skip =4
        else:
            txt = False
            skip =0
        Tree_1, root_1 = TreeBuilder(edge_list,skip =skip,txt=txt,directed=directed)
        Tree_2, root_2 = TreeBuilder(edge_list,skip =skip,txt=txt,directed=directed)
        Tree_3, root_3 = TreeBuilder(edge_list,skip =skip,txt=txt,reverse=True,directed=directed)
        self.Iter_1 = TreijoinIterator(Tree_1, root_1)
        self.Iter_2 = TreijoinIterator(Tree_2, root_2)
        self.Iter_3 = TreijoinIterator(Tree_3, root_3)
        #return 
        self.Join = LeapfrogTrieJoin(self.Iter_1,self.Iter_2,self.Iter_3,Triangle = True)
        return 
    def getCount(self):
        if self.directed:
            return self.Join.count/3
        else:
            return self.Join.count/6
