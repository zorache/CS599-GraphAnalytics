import csv

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
    count = 0
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
                    count+=1
                current_nei = current_nei.next
            #current.marked=False
            marked.remove(current.data)
            current = current.next
        adj_lst.delete(v)
    return count


Adj = Adjacency_List("data/ca-GrQc.txt")
Count = Chiba_Nishizeki(Adj)
