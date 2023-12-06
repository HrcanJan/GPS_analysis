import csv
import networkx as nx
import plotly.graph_objects as go

def load_csv(file_path):
	with open(file_path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		edges = [tuple(map(int, row)) for row in reader]

	return edges

def draw_graph(edges):
	G = nx.Graph()
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
		edge_x.append(x0)
		edge_x.append(x1)
		edge_x.append(None)
		edge_y.append(y0)
		edge_y.append(y1)
		edge_y.append(None)

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
	csv_file_path = '../files/edges/geolife.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)
	
	csv_file_path = '../files/edges/geolife_time_1min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/geolife_time_30min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/geolife_time_1h.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/tdrive.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/tdrive_time_1min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/tdrive_time_30min.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)

	csv_file_path = '../files/edges/tdrive_time_1h.csv'
	edges = load_csv(csv_file_path)
	draw_graph(edges)