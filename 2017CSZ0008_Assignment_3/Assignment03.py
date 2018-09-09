#========================================================

'''
Name : Amit Kumar Chauhan (2017csz0008) 

Usage:
>> python ssAssignment03.py

-----------------------------------------------------

The data-set "Web-Google.txt" has been taken from the SNAP-dataset database. 

'''
#========================================================

#Importing essentials libraries

import networkx as nx
import matplotlib.pyplot as plt
import random

#========================================================

G = nx.read_edgelist("web-Google.txt",nodetype=int)	

#========================================================
# Storing the ranks (in sorted order) produced by PageRank.  

Counter = dict((el, 0.0) for el in G.nodes())			

sorted_pagerank = []

for key, value in sorted(nx.pagerank(G).iteritems(), key=lambda (k,v): (v,k), reverse=True): 
	pair = [key, value]
	sorted_pagerank.append(pair)   					

#========================================================
# The teleport_randomWalk function either teleports with probability 0.2 or walks randomly with probability 0.8. 
    
def teleport_randomWalk(G,Counter): 
	u = random.choice(list(G.nodes()))			
	Counter[u] += 1	
	i=0
	while(i<1000000):					
		neighbour = [m for m in G[u]]	                
		if(len(neighbour) == 0):		   # Random Walk 		
			u=random.choice(list(G.nodes()))
			Counter[u] += 1
		else:						
			coin=random.random()
			if(coin <= 0.2):		   # Teleportation 		
 				u=random.choice(list(G.nodes()))
				Counter[u] += 1
			else:
				u=random.choice(neighbour)
				Counter[u] += 1
	
		i=i+1

	for each in Counter:					
		Counter[each] = Counter[each]/1000000

	sorted_counter = []
	for key, value in sorted(Counter.iteritems(), key = lambda (k,v): (v,k), reverse = True):	
		pair = [key,value]
		sorted_counter.append(pair)
	return sorted_counter

#========================================================
# The compare_results function plots the values on a graph and then compare the results. 
    
def compare_results(result1,result2): 
	Y1 = []
	Y2 = []
	for i in result1:
		Y1.append(i[1])
	for i in result2:
		Y2.append(i[1])
	plt.title("Comparision of Pagerank and Teleport-RandomWalk Algorithms")	 	
	plt.xlabel("Pagerank")
	plt.ylabel("Teleportation")
	plt.plot(Y1,Y2,'b',linewidth=7.0)						
	plt.show()


#========================================================


sorted_teleport=teleport_randomWalk(G,Counter)					

compare_results(sorted_pagerank, sorted_teleport)			


#========================================================