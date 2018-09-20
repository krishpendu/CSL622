import networkx as nx

data = {}

def is_com_sub(m, n): #checking if common subject exists
	for i in range(len(m)):
		if m[i] == n[i] == '1':
			return True
	return False

def bpath(G, d, src, dest): #finding best path b/w given src and dest
	path = [src]
	while True:
		neighbors = list(G.neighbors(src))
		if dest in neighbors:
			path.append(dest)
			break
		for p in path:
			if p in neighbors:
				neighbors.remove(p)
		w = []
		for i in neighbors:
			c = 0
			for p, q in zip(d[src], d[i]):
				if p == '1' and q is '1':
					c+=1
			w.append(c)    	
		best = neighbors[ w.index(max(w)) ]
		path.append(best)
		src = best
	return path

file = open("subj.txt","r") # importing the file
for l in file.readlines():
	tmp = l.strip() #loading each row
	data[int(tmp.split()[0])] = tmp.split()[1:] # splitting the row data

nodes = data.keys() #drawing graph
G = nx.Graph()
G.add_nodes_from(nodes) # adding nodes

for i in range(1, len(data)):
	for j in range(i+1, len(data)+1):
		if is_com_sub(data[i], data[j]): # calling funcn to check whether common subject are there or not
			G.add_edge(i, j) # add edge if common subject exists

print("%-15s %s" % ("Start    End", "Best Path"))

for i in G.nodes():
	for j in G.nodes():
		if(i!=j):
			print("%-15s %s" % (str(i)+"        "+str(j), str(bpath(G, data, i, j) )))
