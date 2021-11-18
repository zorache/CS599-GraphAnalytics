import pandas as pd
import csv


### Problem 1 ###

### Problem 2 ###




### Problem 3 ###
# 3.1 O(ma) time of Triangle Counting Algorithm 
# Chiba-Nishizeki Algorithm

# Suppose the graph is stored in undirected edge list format, and that no edges are listed repeated

# Adjacency list builder using doubly linked list
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data 
        #self.marked = False
        self.prev = prev 
        self.next = next

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        # self.end = None       #For graph purposes, keeping track of last node
        self.len = 0
    def append(self, data):
        node = Node(data)
        if self.head ==None:
            self.head = node
            # self.end = node
            return
        else:
            if self.head.data==data:
                return "Error: adding self loop"
            # prev = self.end    #Previous last node
            current = self.head
            while current.next:
                if current.next.data==data:
                    # edge already in adjacency list
                    return
                current = current.next
            node.prev = current
            current.next = node
            # prev = current   
            # prev.next = node
            # self.end = node
            # node.prev = prev
        self.len +=1
    def delete(self, data):
        deleted = False
        if self.head.data==data:
            return "Error: deleting head of adjacency list"
        else:
            current = self.head.next
            while current:
                if data ==current.data:
                    prev = current.prev
                    next = current.next
                    prev.next = next
                    if next!=None:
                        next.prev = prev
                    deleted=True
                current = current.next
            if deleted:
                self.len -=1
            #return "Error: node is not a neighbor, cannot be deleted"
            #self.len -=1
    def print(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.data)
            current = current.next
        print(lst)

class Adjacency_List:
    def __init__(self, file_name):
        self.dict = {}
        with open(file_name, newline='') as file:
            reader = csv.reader(file, delimiter=' ')
            for edge in reader:
                if edge[0] not in self.dict:
                    lst = Doubly_Linked_List()
                    lst.append(edge[0])
                    self.dict[edge[0]] = lst
                if edge[1] not in self.dict:
                    lst = Doubly_Linked_List()
                    lst.append(edge[1])
                    self.dict[edge[1]] = lst
                self.dict[edge[0]].append(edge[1])
                self.dict[edge[1]].append(edge[0])
    #Not used
    # def delete(self, u, v):
    #     if str(u) not in self.dict.keys() or str(v) not in self.dict.keys():
    #         print(self.dict.keys())
    #         return "Error: deleting an edge that does not exist"
    #     self.dict[str(u)].delete(str(v))
    #     self.dict[str(v)].delete(str(u))
    def delete(self, u):
        if u not in self.dict.keys():
            return "Error: linked list with head "+ u+" does not exist"
        else:
            self.dict.pop(u)
            for n in self.dict.keys():
                self.dict[n].delete(u)

    #Return descending sort of the keys based on length of Adj list
    def sort(self):            
        order={}
        for v in self.dict.values():
            order[v.head.data] = v.len
        return sorted(order, key=lambda k: order[k],reverse=True)
    def print(self):
        for v in self.dict.values():
            v.print()

def Chiba_Nishizeki(adj_lst):
    order = adj_lst.sort()
    marked = []
    for v in order[:-1]:
        current = adj_lst.dict[v].head.next
        marking = current
        print("marking!")
        while marking:                    # Marking all neighbors of v 
            print(marking.data)
            marked.append(marking.data) 
            marking = marking.next
        while current:                    # For each marked neighbor 
            print("current "+ current.data)
            current_nei= adj_lst.dict[current.data].head.next
            while current_nei:
                print("neighbor's neighbor "+current_nei.data)
                #if current_nei.marked:
                if current_nei.data in marked:
                    print(v,current.data,current_nei.data)
                current_nei = current_nei.next
            #current.marked=False
            marked.remove(current.data)
            current = current.next
        adj_lst.delete(v)

# 3.3 


class TreeNode:
    def __init__(self,leaf,key=None,left = None,right=None,tree_child=None,var=None):
        self.leaf = leaf
        self.key = key
        self.left = left
        self.right = right
        if tree_child!=None:
            subtree = AVLTree(parent=self)
            root = None
            self.subtree= subtree
            self.tree_child = subtree.insert(root,tree_child)
        self.var=var
        
        self.height = 1


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
            return self.search(root.right,key)
        else:
             return self.search(root.left,key)
        
    # O(logN)
    def seek(self,root,key):
        if root ==None:
            return "Not found"
        elif key > root.key:
            if root.right==None:
                return "Not found"       
            return self.seek(root.right,key)
        elif key < root.key:
            current= root
            while current.left and current.left.key>=key:
                current = current.left
            return current
        else:
            return root

    # O(logN)
    def getNext(self, root, key):
        return self.seek(root,key+1)


    def insert(self,root,key,key_child=None,child = False):
        if not child:
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
        if root==None: 
            return TreeNode(True, key=key, tree_child=key_child)
        elif key<root.key:
            root.left = self.insert(root.left,key, key_child=key_child,child = True)
        
        
        elif key==root.key:
            root.tree_child = self.insert(root.tree_child, key_child,child = True)   
            return root
        else:
            root.right = self.insert(root.right,key,key_child=key_child,child = True)
        root.height = 1+ max(self.getHeight(root.left),self.getHeight(root.right))
        balanced = self.getBal(root)
        if balanced > 1 and key < root.left.key:
            return self.rRotate(root)

        if balanced < -1 and key > root.right.key:
                return self.lRotate(root)

        if balanced > 1 and key > root.left.key:
            root.left= self.lRotate(root.left)
            return self.rRotate(root)

        if balanced < -1 and key < root.right.key:
            root.r = self.rRotate(root.right)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.right
        T2 = y.left

        y.left= z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        return y

    def rRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left= T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y
    def getHeight(self, root):
        if root==None:
            return 0
        return root.height


    def getBal(self, root):
        if root==None:
            return 0      
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
	    if root==None:
		    return
	    print("{0} ".format(root.key), end="")
	    self.preOrder(root.left)
	    self.preOrder(root.right)

def TreeBuilder(file_name, header = True):
    Tree = AVLTree()
    root = None
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        if header:
            next(reader)
        for edge in reader:
            root = Tree.insert(root, int(edge[0]),int(edge[1]))
    return Tree, root
   
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
        self.root = self.current.tree_child
        node = subtree.search(self.current.tree_child, subtree.min)
        self.current = node
        self.parentroot = self.root
        self.key = self.current.key
        self.subtree = subtree

    def up(self):
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
    def __init__(self,Iter_1,Iter_2, Iter_3):
        self.a = None
        self.b = None
        self.c = None
        self.count = 0
        self.Join_A = LeapfrogJoin(Iter_1,Iter_3)     # find the first A key that matches
        while not self.Join_A.atEnd:
            self.a = self.Join_A.Iter[0].key
            Iter_1.open()
            self.Join_B = LeapfrogJoin(Iter_1, Iter_2)
            while not self.Join_B.atEnd:
                self.b = self.Join_B.Iter[0].key
                Iter_2.open()
                Iter_3.open()
                self.Join_C = LeapfrogJoin(Iter_2, Iter_3)
                while not self.Join_C.atEnd:
                    self.c = self.Join_C.Iter[0].key
                    print([self.a,self.b,self.c])
                    self.count +=1
                    self.Join_C.leapfrogNext()      
                Iter_2.up()
                Iter_3.up()
                self.Join_B.leapfrogNext()          
            Iter_1.up()
            self.Join_A.leapfrogNext()                      



class CountTriangles():
    def __init__(self,edge_list):
        Tree_1, root_1 = TreeBuilder(edge_list)
        Tree_2, root_2 = TreeBuilder(edge_list)
        Tree_3, root_3 = TreeBuilder(edge_list)
        Iter_1 = TreijoinIterator(Tree_1, root_1)
        Iter_2 = TreijoinIterator(Tree_2, root_2)
        Iter_3 = TreijoinIterator(Tree_3, root_3)
        Join = LeapfrogTrieJoin(Iter_1,Iter_2,Iter_3)
        return Join.count



# 3.4
# http://snap.stanford.edu/data/ca-GrQc.html

