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

	nt.show('./files/graph2.html')

if __name__ == "__main__":
	csv_file_path = './files/geolife_time_1day.csv'
	edges = load_csv(csv_file_path)
	visualize_graph(edges)
