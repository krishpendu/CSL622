""" Krishnendu Sahu
	2016MED1004
	Assignment_3 """
import networkx as nx # importing networkx function
import random # importing random function
import matplotlib.pyplot as plt # importing plot function

G = nx.read_edgelist("Wiki-Vote.txt",create_using=nx.DiGraph(), nodetype = int) # Creating directed graph for "Wiki-Vote.txt"
# Data set obtained from https://snap.stanford.edu/data/wiki-Vote.txt.gz
n = G.number_of_nodes() # Count no. of nodes
itr = 10000 # Defining no. of iteration
l=[] # initialising list
for i in list(G.nodes()):
	l[i]=0;

random_node = random.choice(list(G.nodes())) # choose a random starting node for random walk
for j in range(1,itr+1): # loop to perform random walk
	curr_node = random_node
	l[curr_node] = l[curr_node] + 1
	x=random.random()
	if (x >= 0.8): # go to neighbour node for probability >0.2
		N = list(G.neighbors(curr_node))
		ln = len(N)
		if ln != 0:
			random_node = random.choice(N)
		elif ln==0:
			random_node = random.choice(list(G.nodes()))
	elif(x <= 0.2) : # Teleporting for probability < 0.2
		random_node = random.choice(list(G.nodes()))		

ndlst = list(l.keys())
vstslst = [l[x] for x in ndlst]
pageRank = nx.pagerank(G) # using inbuilt function to find rank
rankval = [500*pageRank[x] for x in ndlst] 
plt.plot(ndlst,vstslst,'b--', ndlst, rankval , 'r--')
plt.show() # displaying graph
