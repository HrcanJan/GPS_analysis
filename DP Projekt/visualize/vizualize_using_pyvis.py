import csv
import networkx as nx
from pyvis.network import Network

def load_csv(file_path):
	with open(file_path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		edges = [tuple(map(int, row)) for row in reader]

	return edges

def visualize_graph(edges, nodes):
	G = nx.Graph()
	G.add_nodes_from(map(str, nodes))
	G.add_edges_from(edges)

	nt = Network(directed=False, notebook=True)

	for node in G.nodes:
		nt.add_node(str(node), title=str(node), label=str(node))

	nt.from_nx(G)

	nt.show('./files/graphs/graph3.html')

if __name__ == "__main__":
	# ADJUST FILE PATH HERE
	node_path = './files/nodes/geolife.csv'
	edges_path = './files/edges/geolife_time_1min.csv'
	edges = load_csv(edges_path)
	nodes = load_csv(node_path)
	visualize_graph(edges, nodes)
