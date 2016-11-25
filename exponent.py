import sys
import numpy as np
import operator
import networkx as nx
import matplotlib.pyplot as plt
from math import log,pow

G=nx.read_pajek("BA1.net")
d=nx.degree(G)

maxdegree=max ( d.iteritems(), key=operator.itemgetter(1))[1]
mindegree=min ( d.iteritems(), key=operator.itemgetter(1))[1]
sum=0
i=0
for key, val in d.items():
	sum = sum + log ( val / (mindegree - 0.5) )
	i=i+1

al = 1 + i * pow(sum,-1)
print al

   
