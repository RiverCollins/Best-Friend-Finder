import os
import sys
import csv
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
def make_edge(main, list):
	for index in range(len(list)):
		graph.add_edge(main, list[index])

def draw_graph():
	pos = nx.spring_layout(graph)
	nx.draw(graph, pos, node_size=200, alpha=0.5, node_color="blue", with_labels=True)
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

def get_names(name, cwd):
	if(os.getcwd() != cwd):
		os.chdir(cwd)
		os.chdir(name)
	top_friends = []
	with open(name + '.csv','r') as fh:
		reader = csv.reader(fh, delimiter = ',')
		i = 0
		for row in reader:
			if(i >= 5):
				break;
			top_friends.append(row[0])
			i = i + 1
	return top_friends

def main(argv):
	user_name = sys.argv[1]
	os.chdir(user_name)
	cwd = os.getcwd()
	top_names = get_names(user_name, cwd)
	make_graph()
	make_node(user_name)
	make_nodes_from_list(top_names)
	make_edge(user_name, top_names)
	draw_graph()


if __name__ == "__main__":
	main(sys.argv[1:])
