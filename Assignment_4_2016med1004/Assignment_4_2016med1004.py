import networkx as nx
import matplotlib.pyplot as plt
import random as rand


G = nx.karate_club_graph()

n = G.number_of_nodes() # calculating no. of nodes

V = list(G.nodes()) # listing all the nodes

E =  G.edges() # Finding the edges

Count = {}# Counting shortest paths b/w 2 nodes

while(nx.is_connected(G)):
	# Calculating betweeness centrality of a node
	for i in E:
		Count[i] = 0

	for i in range(len(V)):
		for j in range(i+1,len(V)):
			X = nx.shortest_path(G,source=V[i],target=V[j]) # finding shortest paths b/w 2 nodes
			for k in range(len(X)-1):
				p,q = min(X[k],X[k+1]),max(X[k],X[k+1])
				Count[(p,q)] += 1
	c = n*(n-1)/2 # Dividing by total number of shotest paths
	for i in E:
		Count[i] = (Count[i]*1.0)/c

	# TO sort all the edges according to betweenes centrality of the node
	P = []
	for i,j in Count.items():
		P.append((j,i))

	P = sorted(P)

	x = P.pop() # to pop out
	print(x)
	G.remove_edge(x[1][0],x[1][1]) # removing edges bw nodes with high betweness centrality

nx.draw(G, with_labels = True) # drawing graph with labels
plt.show() # display the graph
