# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:17:11 2020

@author: Felix
"""
"""this implementation utilizes https://github.com/taynaud/python-louvain/tree/master/community"""

import time
import numpy as np
import networkx as nx
import community as cl

G=nx.read_gpickle("LFR1000")
n=len(G.nodes())
st=time.time()

partition = cl.best_partition(G)

et=time.time()

ex_time=(et-st)*1000 #time in milliseconds

print(ex_time, partition)

communities=[]
for i in range(n):
    comm=[]
    for j in partition:
        if partition[j]==i:
            comm.append(j)
    communities.append(set(comm))

#print(communities)
modularity=nx.algorithms.community.quality.modularity (G, communities)
print(modularity)