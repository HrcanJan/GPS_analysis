import csv
import networkx as nx
from pyvis.network import Network

def load_csv(file_path):
	with open(file_path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		edges = [tuple(map(int, row)) for row in reader]

	return edges

def visualize_graph(edges):
	G = nx.Graph()
	G.add_edges_from(edges)

	nt = Network(directed=False, notebook=True)

	for node in G.nodes:
		nt.add_node(node, title=str(node), label=str(node))

	nt.from_nx(G)

	nt.show('./files/graphs/graph.html')

if __name__ == "__main__":
	# ADJUST FILE PATH HERE
	csv_file_path = './files/edges/geolife.csv'
	edges = load_csv(csv_file_path)
	visualize_graph(edges)
