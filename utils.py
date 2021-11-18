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
    def seek(self,root,key):
        if root ==None:
            return "Not found"
        elif key > root.key:     
            return self.seek(root.r,key)
        elif key < root.key:
            current= root
            while current.l and current.l.key>=key:
                current = current.l
            return current
        else:
            return root

    # O(logN)
    def getNext(self, root, key):
        return self.seek(root,key+1)

    
    def insert(self,root,key,key_child=None):
        print("inserting: key is "+ str(key))
        print("prev max and min ")
        print(str(self.max))
        print(str(self.min))
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
        print("after max and min ")
        print(str(self.max))
        print(str(self.min))
        if root!=None:
            print("current")
            print(str(root.key))
        if root==None: 
            print("current is None")
            return treeNode(True, key, key_child=key_child)
        elif key<root.key:
            print("go left")
            root.l = self.insert(root.l, key, key_child=key_child)
        elif key==root.key:
            print("found")
            root.child_root = root.subtree.insert(root.child_root, key_child)
        else:
            print("go right")
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
