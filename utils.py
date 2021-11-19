import csv

class treeNode(object):
    def __init__(self, leaf, key, key_child=None):
        self.leaf = True
        self.key = key
        self.l = None
        self.r = None
        self.subtree=None
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
   
    # O(log N)
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
            return treeNode(True, key, key_child=key_child)
        elif key<root.key:
            root.l = self.insert(root.l, key, key_child=key_child)
        elif key==root.key:
            if root.subtree!=None:
                root.child_root = root.subtree.insert(root.child_root, key_child)
        else:
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

def TreeBuilder(file_name, header = True, skip = 0, txt = False,reverse=False, directed=True):
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
                if not directed:
                    root = Tree.insert(root, int(edge[1]),int(edge[0]))
                    root = Tree.insert(root, int(edge[0]),int(edge[1]))
                elif reverse:
                    root = Tree.insert(root, int(edge[1]),int(edge[0]))
                else:
                    root = Tree.insert(root, int(edge[0]),int(edge[1]))
        else:
            if "musae_git" in file_name:
                delimiter = ','
            else:
                delimiter=' '
            reader = csv.reader(file, delimiter=delimiter)
            if header:
                next(reader)
            for edge in reader:
                root = Tree.insert(root, int(edge[0]),int(edge[1]))
    return Tree, root


        
   

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
            current = self.head
            while current.next:
                if current.next.data==data:
                    # edge already in adjacency list
                    return
                current = current.next
            node.prev = current
            current.next = node
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
        txt = True
        skip = 4
        self.dict = {}
        with open(file_name, newline='') as file:
            if txt:
                lines = file.readlines()
                for line in lines:
                    if skip>0:
                        skip -=1
                        continue
                    edge = (line.strip('\n')).strip('\r').split("\t")
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
                    
            else:
                if "musae_git" in file_name:
                    delimiter = ','
                else:
                    delimiter=' '
                reader = csv.reader(file, delimiter=delimiter)
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
    
    def delete(self, u):
        if u not in self.dict.keys():
            return "Error: linked list with head "+ u+" does not exist"
        else:
            self.dict.pop(u)
            for n in self.dict.keys():
                self.dict[n].delete(u)

    # Return descending sort of the keys based on length of Adj list
    def sort(self):            
        order={}
        for v in self.dict.values():
            order[v.head.data] = v.len
        return sorted(order, key=lambda k: order[k],reverse=True)
    def print(self):
        for v in self.dict.values():
            v.print()

       
