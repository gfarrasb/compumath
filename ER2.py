import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


total = len(sys.argv)
if total <> 3:
  print "Usage: python ER2 n-nodes p-probability. We will generate a random graph"
  sys.exit("Error")

numnodes = int(sys.argv[1])
prob = float(sys.argv[2])

print ("# nodes: " + str(numnodes))
print ("Probability by edge: " + str(prob))

#Graph generation
G=nx.Graph()
i = 0
while (i < numnodes):
    G.add_node(i)
    i = i + 1
    

for j in range(0, numnodes):
   print 'Evaluating edges on node', j
   for k in range(j+1, numnodes):
	r=np.random.choice([0,1],1,p=[1-prob,prob])[0]
	if r==1:
	  G.add_edge(j,k)
	  
	    
print("# number of plotted edges " + str( G.number_of_edges() ));    
nx.draw(G)
plt.show()
nx.write_pajek(G, "ER2.net")

   
