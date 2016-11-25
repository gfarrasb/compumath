import sys
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


total = len(sys.argv)
if total <> 4:
	print "Usage: python CM n-nodes (ER poisson | GM gamma |SF Pareto power-law) value. We will generate a random graph using CM"
  	sys.exit("Error")

numnodes = int(sys.argv[1])
dist = str(sys.argv[2])
param = int(sys.argv[3])

if dist=="ER":
	print "Poisson"

if dist=="SF":
	print "Pareto Power-law"

if dist=="GM":
	print "Gamma"

#Graph generation
G=nx.Graph()
i = 0
while (i < numnodes):
    G.add_node(i)
    i = i + 1
    
if dist=="ER":
	deg_dist=np.random.poisson(param, numnodes)

if dist=="GM":
	deg_dist=np.random.gamma(param, 1, numnodes)



deg_dist[deg_dist > numnodes-1] = numnodes-1
print deg_dist
numit=0

while sum(deg_dist)>0 and numit<10000:
	o = random.randint(0,numnodes-1)
	if (deg_dist[o] > 0):
		d = random.randint(0,numnodes-1)
		if (( deg_dist[d] > 0 ) and (o <> d) and (G.has_edge(o,d)==False)):
			G.add_edge(o,d)
			deg_dist[o]=deg_dist[o]-1
			deg_dist[d]=deg_dist[d]-1
	print "pendent " , deg_dist
	numit = numit+1
	print "Num iteration " , numit



print "Final num edges" , G.number_of_edges()
nx.draw_circular(G)
plt.show()
nx.write_pajek(G, "CM1.net")
   
