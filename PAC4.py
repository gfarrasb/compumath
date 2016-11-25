import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

total = len(sys.argv)
if total < 3:
	  print "Usage: python PAC4\n\tnetwork (Pajek file)\n\tu (spontaneus recovery probability - in %)\n\tB (infection probability - in %)\n\tnrep (number of repetitions simulation)\n\tpinit (initial fraction of infected nodes - in %)\n\ttmax (maximum time steps of each simulation)\n\tttrans (number of steps of the transitory)"
	  sys.exit("Error")

#network - Pajek file
net = sys.argv[1]

#spontaneus recovery probability
u = int(sys.argv[2])

#infection probability
b = int(sys.argv[3])

#number of simulation repetitions
nrep = int(sys.argv[4])
actrep = 0

#initial fraction of infected nodes
pinit = int(sys.argv[5])

#maximum time steps of each simulation
tmax = int(sys.argv[6])

#number of steps of the transitory
ttrans = int(sys.argv[7])

#print "Preparing the graph..."
G=nx.read_pajek(net)
#G=nx.complete_graph(10)

#Variable to save the final p value
prob = 0
nfstep = 0
probinters = 0


while actrep < nrep:
      #print "Simulation " , actrep

      eti={}
      i=0
      for node in G:
	      v = random.randint(0,100)
	      if v <= pinit:
		      G.node[node]['State']="I"
		      eti[i]='I'
	      else:
		      G.node[node]['State']="S"
		      eti[i]='S'
	      i=i+1

      #print "The graph is ready ... epidemic spreading begins..."
      #print "Values: " , eti
      pos=nx.circular_layout(G)
      #nx.draw_networkx_labels(G, pos, eti)
      #nx.draw_circular(G)
      #plt.show()


      step=0
      while step < tmax:

	      i=0
	      for node in G:
		      if G.node[node]['State']=="I":
			      v = random.randint(0,100)
			      if v <= u:
				      G.node[node]['State']="S"
				      eti[i]='S'
		      i=i+1


	      i=0
	      for node in G:
		      if G.node[node]['State']=="S":
			      for vei in G.neighbors(node):
				      if (G.node[vei]['State']=="I") and (G.node[node]['State']=="S"):
					      v = random.randint(0,100)
					      if v<=b:
						      G.node[node]['State']="I"
						      eti[i]='I'
		      i=i+1

	      #nx.draw_networkx_labels(G, pos, eti)
	      #nx.draw_circular(G)
	      #plt.show()

	      sus=0
	      inf=0
	      for node in G:
		      if G.node[node]['State']=="S":
			      sus=sus+1
		      if G.node[node]['State']=="I":
			      inf=inf+1

	      #print "Values: " , eti
	      if step > ttrans:
		      #print " -- STABLE STATE --"
		      #print "Step : " , step , ". Infected: " , (inf/float(G.number_of_nodes()))*100 , "% . Susceptible: " , (sus/float(G.number_of_nodes()))*100 , "%"
	     	      prob = prob + (inf/float(G.number_of_nodes()))*100
		      nfstep = nfstep + 1

              if step+1 == tmax:
		      probinters = probinters + prob / nfstep 

	      step = step + 1

      actrep=actrep+1	     

print b , " " , probinters / actrep  
