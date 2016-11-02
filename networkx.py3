import os
import sys
import csv
import community
import networkx as nx
import matplotlib.pyplot as plot
'''
node_list = [('riv'), ('chaz'), ('Tiley'), ('Ryan')]

graph = nx.Graph()

#add nodes to graph from node listcls
for index in range(len(node_list)):
	graph.add_node(node_list[index])

graph.add_edge('riv', 'chaz', weight=3)
graph.add_edge('riv', 'Tiley', weight=5)

pos = nx.spring_layout(graph)

nx.draw(graph, pos, node_size=200, alpha=0.5, node_color="blue", with_labels=True)

edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in graph.edges(data=True)])
nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)

plot.axis('off')
plot.show()
'''
def make_edge(main, list, num):
	for index in range(len(list)):
		graph.add_edge(main, list[index], weight=num[index], node_color='red')

def draw_graph():
	pos = nx.spring_layout(graph, k = 0.1, iterations=20, scale=5)
	nx.draw(graph, pos, node_size=200, alpha=0.5, node_color="blue", with_labels=True)
	
	edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in graph.edges(data=True)])
	nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)
	
	plot.axis('off')
	plot.show()

def make_node(node):
	graph.add_node(node)

def make_nodes_from_list(list):
	for index in range(len(list)):
		graph.add_node(list[index])

def make_graph():
	global graph
	graph = nx.Graph()

	
def get_weight(name, cwd):
	if(cwd == 1):
		asdf = 1
	else:
		os.chdir(cwd)
		os.chdir(name)
	weight = []
	with open(name + 'Sorted.csv','r') as fh:
		reader = csv.reader(fh, delimiter = ',')
		i = 0
		for row in reader:
			if(i >= 10):#number of friends here
				break;
			weight.append(row[1])
			i = i + 1
	return weight

def get_names(name, cwd):
	if(cwd == 1):
		asdf = 1
	else:
		os.chdir(cwd)
		os.chdir(name)
	top_friends = []
	with open(name + 'Sorted.csv','r') as fh:
		reader = csv.reader(fh, delimiter = ',')
		i = 0
		for row in reader:
			if(i >= 10):#number of friends here
				break;
			top_friends.append(row[0])
			i = i + 1
	return top_friends

def main(argv):
	user_name = sys.argv[1]
	os.chdir(user_name)
	cwd = 1
	top_names = get_names(user_name, cwd)
	weight = get_weight(user_name, cwd)
	main_list = top_names
	cwd = os.getcwd()
	make_graph()
	make_node(user_name)
	make_nodes_from_list(top_names)
	make_edge(user_name, top_names, weight)
	
	#print("test")

	for index in range(len(main_list)):
		#print(main_list[index])
		top_names = get_names(main_list[index], cwd)
		weight = get_weight(main_list[index], cwd)
		make_nodes_from_list(top_names)
		make_edge(main_list[index], top_names, weight)
		
	draw_graph()


if __name__ == "__main__":
	main(sys.argv[1:])

