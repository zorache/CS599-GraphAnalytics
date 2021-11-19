import random
import sys
from pprint import pprint


def DP_from_coloring(file, type, k):
    if ".txt" in file:
        G={} 
        with open(file_name, newline='') as file:
            lines = file.readlines()
            skip = 4
            for line in lines:
                if skip>0:
                    skip -=1
                    continue
                edge = (line.strip('\n')).strip('\r').split("\t")
                if not u in G:
                    G[u]=set([])
                if not v in G:
                    G[v]=set([])
                G[u].add(v)
                G[v].add(u)
    else:
        fin = open(file)
        n, m=map(int, next(fin).split())    #first row: #of nodes    #of edges
        G={}                                #adjacency list
        for i in range(m):
            u,v = map(int,next(fin).split())
            if not u in G:
                G[u]=set([])
            G[u].add(v)
        V = list(range(n))
        for u in V:
            if not u in G:
                G[u]=set([])                   #add empty set for nodes that don't have outgoing edge

    k = int(k)

    if type=="random":
        coloring = {u:random.randint(1,k) for u in V}    #random coloring
    
    # Create partition by color
    inv_map = {}
    for k, v in coloring.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    
    # If a partition has less than three nodes, cannot form a triangle
    if len(min(inv_map.values(), key=lambda k: len(k)))<3:
        return "No k disjoint triangles can be found with this coloring"
    
    
    dp_table = {}
    for u in V:
        dp_table[(u,0)]=set([(coloring[u],)])
        
    # Iterate through the color partitions 
    for n in inv_map.values():
        # For each partition, create a partial_paths dictionary
        partial_paths = {(u,(coloring[u],)):[u] for u in n}
        found = False
        i=0
        for u in n:
            dp_table[(u,0)]=set([(coloring[u],)])
            for v in G[u]:
                if coloring[v]==coloring[u]:
                    for partial_coloring in dp_table[(v,i-1)]:
                        new_partial_coloring = tuple(sorted(list(partial_coloring)+[coloring[u]]))
                        if not new_partial_coloring in dp_table[(u,i)]:
                            for j in new_partial_coloring:
                                if u in G[j]:
                                    i+=1
                                    dp_table[(u,i)].add(new_partial_coloring)
                                    partial_paths[(u, new_partial_coloring)]=[u] +partial_paths[v,partial_coloring]
                                    if i==2:
                                        print(partial_paths[(u,new_partial_coloring)])
                                        found = True
                                        break
                        if found:
                            break
                if found:
                    break
        if not found:
            return "No k disjoint triangles can be found with this coloring"
    return True
            
                        
                    
                    
#     pprint(dp_table)
#     pprint(partial_paths)
