import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


total = len(sys.argv)
if total <> 4:
  print "Usage: python watts-strogatz n-nodes k-edges p-probability. We will generate a random graph"
  sys.exit("Error")

if float(sys.argv[3]) > 1:
  print "Probability can't be greater than 1"
  sys.exit("Error")

numnodes = int(sys.argv[1])
edges = int(sys.argv[2])
prob = float(sys.argv[3])
indeg = edges*2 / numnodes

if edges > numnodes*(numnodes-1)/2:
	print "Is not posible to generate a graph with more than " , numnodes*(numnodes-1)/2 , " edges"
	sys.exit("Error")

print ("# nodes: " + str(numnodes))
print ("# edges: " + str(edges))
print ("# initial edges per node: " + str(indeg))
print ("Probability by edge: " + str(prob))

#Graph generation
G=nx.Graph()
i = 0
while (i < numnodes):
    G.add_node(i)
    i = i + 1
    

for j in range(0, numnodes):
	for k in range(0, numnodes):
		l = abs(j-k) % (numnodes -1 - indeg/2 )
		#print "j,k -->" , j , k , " --> l value " , l
		if l > 0 and l<=indeg/2:
			G.add_edge(j, k)

for j in range(0, numnodes):
	for k in range(j+1, numnodes):
		r=np.random.choice([0,1],1,p=[1-prob,prob])[0]
		if r==1:
	  		G.add_edge(j,k)
	  
	    
print "Final num edges" , G.number_of_edges()
nx.draw_circular(G)
plt.show()

nx.write_pajek(G, "WS.net")
