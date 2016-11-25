import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


total = len(sys.argv)
if total <> 3:
  print "Usage: python er1 n-nodes M-edges. We will generate a random graph"
  sys.exit("Error")

numnodes = int(sys.argv[1])
numedges = int(sys.argv[2])

if numedges > numnodes*(numnodes-1):
   print "This will not be posible"
   sys.exit()
   
print ("# nodes: " + str(numnodes))
print ("M edges: " + str(numedges))

#Graph generation
G=nx.Graph()
i = 0
while (i < numnodes):
    G.add_node(i)
    i = i + 1
    

while (G.number_of_edges() < numedges):
   nsource = np.random.choice(numnodes)
   ndst = np.random.choice(numnodes)
   if nsource <> ndst:
	  G.add_edge(nsource, ndst)
   print "We have " + str(G.number_of_edges()) + " and we want " + str(numedges)
	    
    
nx.draw(G)
plt.show()
nx.write_pajek(G, "ER1.net")
   
