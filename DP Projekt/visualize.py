import networkx as nx
import plotly.graph_objects as go
import json
from datetime import datetime

meeting_data = []

# Open the JSON file for reading
with open("./files/geolife.json", "r") as json_file:
	meeting_data = json.load(json_file)

# Create a NetworkX graph
G = nx.Graph()

include_time = False
time_threshold = 60 # 60 seconds
distance_threshold = 0.005 # 100 meters

for meeting in meeting_data:
	if(meeting["Distance (meters)"] < distance_threshold):
		taxi1 = meeting["Taxi1"]
		taxi2 = meeting["Taxi2"]
		timestamp1 = datetime.strptime(meeting["Timestamp1"], "%Y-%m-%d %H:%M:%S")
		timestamp2 = datetime.strptime(meeting["Timestamp2"], "%Y-%m-%d %H:%M:%S")
		
		if include_time == True:
			if abs((timestamp1 - timestamp2).total_seconds()) <= time_threshold:
				G.add_node(taxi1)
				G.add_node(taxi2)
				G.add_edge(taxi1, taxi2)
		else:
			G.add_node(taxi1)
			G.add_node(taxi2)
			G.add_edge(taxi1, taxi2)

pos = nx.spring_layout(G)

# Convert node labels to strings
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
