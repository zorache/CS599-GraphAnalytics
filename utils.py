import csv

class treeNode(object):
    def __init__(self, leaf, key, key_child=None):
        self.leaf = True
        self.key = key
        self.l = None
        self.r = None
        if key_child!=None:
            self.subtree = AVLTree(parent=self)
            child_root = None
            self.child_root = self.subtree.insert(child_root,key_child)
        self.h = 1
        
class AVLTree():
    def __init__(self,parent=None):
        self.min = None
        self.max = None
        self.parent = parent

    def end(self,node):
        return node.key==self.max         
    
    def search(self, root, key):
        if root ==None:
            return "Not found"
        elif key==root.key:
            return root
        elif key> root.key:
            return self.search(root.r,key)
        else:
             return self.search(root.l,key)
        
    # O(logN)
#     def seek(self,root,key):
#         if root ==None:
#             return "Not found"
#         elif key > root.key:     
#             return self.seek(root.r,key)
#         elif key < root.key:
#             current= root
#             while current.l and current.l.key>=key:
#                 current = current.l
#             return current
#         else:
#             return root
        # O(logN)
    def seek(self,root,key):
        if root ==None:
            return "Not found"
        elif key > root.key:     
            return self.seek(root.r,key)
        elif key < root.key:
            current= root
            temp = current.l
            while temp:
                if temp.key>key:
                    current = temp
                    temp = temp.l
                elif temp.key<key:
                    temp = temp.r
                else:
                    return temp
            return current
        else:
            return root

    # O(logN)
    def getNext(self, root, key):
        return self.seek(root,key+1)

    
    def insert(self,root,key,key_child=None):
#         print("inserting: key is "+ str(key))
#         print("prev max and min ")
#         print(str(self.max))
#         print(str(self.min))
        if self.max==None:
            self.max = key
        else:
            if self.max<key:
                self.max = key
        if self.min==None:
            self.min = key
        else:
            if self.min>key:
                self.min = key
#         print("after max and min ")
#         print(str(self.max))
#         print(str(self.min))
#         if root!=None:
#             print("current")
#             print(str(root.key))
        if root==None: 
#             print("current is None")
            return treeNode(True, key, key_child=key_child)
        elif key<root.key:
#             print("go left")
            root.l = self.insert(root.l, key, key_child=key_child)
        elif key==root.key:
#             print("found")
            root.child_root = root.subtree.insert(root.child_root, key_child)
        else:
#             print("go right")
            root.r = self.insert(root.r, key, key_child=key_child)
            
        
        root.h = 1 + max(self.getHeight(root.l),
                        self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.key:
            return self.rRotate(root)

        if b < -1 and key > root.r.key:
            return self.lRotate(root)

        if b > 1 and key > root.l.key:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.key:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.key), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)

def TreeBuilder(file_name, header = True, skip = 0, txt = False,reverse=False):
    Tree = AVLTree()
    root = None
    with open(file_name, newline='') as file:
        if txt:
            lines = file.readlines()
            for line in lines:
                if skip>0:
                    skip -=1
                    continue
                edge = (line.strip('\n')).strip('\r').split("\t")
#                 print(edge)
                if reverse:
                    root = Tree.insert(root, int(edge[1]),int(edge[0]))
                else:
                    root = Tree.insert(root, int(edge[0]),int(edge[1]))
        else:
            reader = csv.reader(file, delimiter=' ')
            if header:
                next(reader)
                skip =skip -1
            for edge in reader:
                root = Tree.insert(root, int(edge[0]),int(edge[1]))
    return Tree, root

# def TreeBuilder(file_name, header = True, skip = 0, txt = False):
#     Tree = AVLTree()
#     root = None
#     with open(file_name, newline='') as file:
#         if txt:
#             lines = file.readlines()
#             for line in lines:
#                 if skip>0:
#                     skip -=1
#                     continue
#                 edge = (line.strip('\n')).strip('\r').split("\t")
#                 print(edge)
#                 root = Tree.insert(root, int(edge[0]),int(edge[1]))
#         else:
#             reader = csv.reader(file, delimiter=' ')
#             if header:
#                 next(reader)
#                 skip =skip -1
#             for edge in reader:
#                 root = Tree.insert(root, int(edge[0]),int(edge[1]))
#     return Tree, root
        
        
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
            print("a b - a c  match")
            print(self.a)
            print("opening Iter_1")
            Iter_1.open()
            self.Join_B = LeapfrogJoin(Iter_1, Iter_2)
            while not self.Join_B.atEnd:
                self.b = self.Join_B.Iter[0].key
                print("a b - b c  match")
                print(self.b)
                print("opening Iter_2")
                Iter_2.open()
                print("opening Iter_3")
                Iter_3.open()
                self.Join_C = LeapfrogJoin(Iter_2, Iter_3)
                while not self.Join_C.atEnd:
                    self.c = self.Join_C.Iter[0].key 
                    print([self.a,self.b,self.c])
                    self.count +=1
                    self.Join_C.leapfrogNext()
                print("closing Iter_2")
                Iter_2.up()
                print("closing Iter_3")
                Iter_3.up()
                self.Join_B.leapfrogNext() 
            print("closing Iter_1")
            Iter_1.up()
            self.Join_A.leapfrogNext()                     



class CountTriangles():
    def __init__(self,edge_list):
        if "txt" in edge_list:
            txt = True
            skip =4
        else:
            txt = False
            skip =0
        Tree_1, root_1 = TreeBuilder(edge_list,skip =skip,txt=txt)
        Tree_2, root_2 = TreeBuilder(edge_list,skip =skip,txt=txt)
        Tree_3, root_3 = TreeBuilder(edge_list,skip =skip,txt=txt,reverse=True)
        self.Iter_1 = TreijoinIterator(Tree_1, root_1)
        self.Iter_2 = TreijoinIterator(Tree_2, root_2)
        self.Iter_3 = TreijoinIterator(Tree_3, root_3)
        #return 
        self.Join = LeapfrogTrieJoin(self.Iter_1,self.Iter_2,self.Iter_3,Triangle = True)
        return 
