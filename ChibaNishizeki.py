from utils import *

def Chiba_Nishizeki(adj_lst_name):
    adj_lst = Adjacency_List(adj_lst_name)
    order = adj_lst.sort()
    marked = []
    count = 0
    for v in order[:-1]:
        current = adj_lst.dict[v].head.next
        marking = current
        while marking:                    # Marking all neighbors of v 
            marked.append(marking.data) 
            marking = marking.next
        while current:                    # For each marked neighbor 
            current_nei= adj_lst.dict[current.data].head.next
            while current_nei:
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

