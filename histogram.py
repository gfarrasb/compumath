#!/usr/bin/python

import networkx as nx
import sys
import operator
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

G1=nx.read_pajek(sys.argv[1])
G=nx.Graph(G1)
d=nx.degree(G)
maxdegree=max ( d.iteritems(), key=operator.itemgetter(1))[1]
mindegree=min ( d.iteritems(), key=operator.itemgetter(1))[1]
numnodesmaxdegree = max ( d.iteritems(), key=operator.itemgetter(1))[0]
print d.values()
h=plt.hist ( d.values(), maxdegree, normed=1, cumulative=False )
plt.xlabel("Min: " + str(mindegree) + " - Degree k - " + " Max: " + str(maxdegree ))
plt.ylabel(' Fraction pk of vertices with degree k ')
plt.title(" Degree histogram " +  sys.argv[1])
plt.axis([0 , maxdegree*1.2, 0 , 1])
plt.grid(True)
plt.show()



