import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


total = len(sys.argv)
if total <> 4:
  print "Usage: python BA nodes-initial nodes-final degree-new-nodes."
  print "We will generate a random graph using Barabasi-Albert Algorithm"
  sys.exit("Error")

nnodinit = int(sys.argv[1])
nnodfi   = int(sys.argv[2])
m = int(sys.argv[3])

if nnodfi < nnodinit:
	print "The final # of nodes can't be smaller than the initial one"
	sys.exit()

#Graph generation. I will generate the initial graph
G=nx.Graph()
labels={}
i = 0
while (i < nnodinit):
    G.add_node(i)
    labels[i]=i
    i = i + 1

for j in range(0,nnodinit):
	for k in range(j+1,nnodinit):
		G.add_edge(j,k)
    
print "Actual " , G.number_of_nodes() , " and we want " , nnodfi
#Time to add new nodes with preferential attachment
while ( G.number_of_nodes() < nnodfi ):
	G.add_node(i)
	labels[i]=i
	while (G.degree(i) < m):
		s=float( sum(nx.degree(G).values()))
		prob_sequence=[float(x / s) for x in nx.degree(G).values()]
		print prob_sequence
		print range(0,i)
		r=np.random.choice(range(0,i+1),1,p=prob_sequence)[0]
		print "Escollim " + str(r)
		if r<>i:
			print r
			G.add_edge(i, r)

	i = i + 1
	print " Adding new node..."

pos=nx.circular_layout(G)
#nx.draw_networkx_nodes(G, pos, nodelist=[0,1,2], node_color='B', node_size=500)
nx.draw_networkx_labels(G,pos,labels,font_size=10)
nx.draw_circular(G)
plt.show()
nx.write_pajek(G, "BA1.net")


   
