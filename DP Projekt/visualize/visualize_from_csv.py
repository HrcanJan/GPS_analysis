import csv
import networkx as nx
import plotly.graph_objects as go

def load_csv(file_path):
	with open(file_path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		edges = [tuple(map(int, row)) for row in reader]

	return edges

def draw_graph(edges, nodes):
	G = nx.Graph()

	G.add_nodes_from(nodes)
	G.add_edges_from(edges)

	pos = nx.spring_layout(G)

	node_trace = go.Scatter(
		x=[pos[x][0] for x in G.nodes()],
		y=[pos[x][1] for x in G.nodes()],
		mode="markers",
		marker=dict(size=10, color="blue"),
		text=[str(node) for node in G.nodes()],
		hoverinfo="text"
	)

	edge_x = []
	edge_y = []
	for edge in G.edges():
		x0, y0 = pos[edge[0]]
		x1, y1 = pos[edge[1]]
		edge_x.extend([x0, x1, None])
		edge_y.extend([y0, y1, None])

	edge_trace = go.Scatter(
		x=edge_x,
		y=edge_y,
		line=dict(width=1, color="#888"),
		hoverinfo="none",
		mode="lines"
	)

	fig = go.Figure(data=[edge_trace, node_trace])
	fig.update_layout(
		showlegend=False,
		hovermode="closest",
		title="Interactive Taxi Meeting Visualization",
		xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
		yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
	)

	fig.show()

if __name__ == "__main__":
	node_path = './files/nodes/geolife.csv'
	nodes = load_csv(node_path)

	csv_file_path = './files/edges/geolife.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)
	
	csv_file_path = './files/edges/geolife_time_1min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	csv_file_path = './files/edges/geolife_time_30min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	csv_file_path = './files/edges/geolife_time_1day.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	node_path = './files/nodes/tdrive.csv'
	nodes = load_csv(node_path)

	csv_file_path = './files/edges/tdrive.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	csv_file_path = './files/edges/tdrive_time_1min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	csv_file_path = './files/edges/tdrive_time_30min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges, nodes)

	csv_file_path = './files/edges/tdrive_time_1day.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)