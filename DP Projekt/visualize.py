import networkx as nx
import plotly.graph_objects as go
import json

# Load meeting data from JSON file
with open("./files/meeting_data.json", "r") as json_file:
    meeting_data = [json.loads(line) for line in json_file]

# Create a NetworkX graph
G = nx.Graph()

# Add nodes and edges based on meeting data
for meeting in meeting_data:
    taxi1 = meeting["Taxi1"]
    taxi2 = meeting["Taxi2"]
    
    G.add_node(taxi1)
    G.add_node(taxi2)
    G.add_edge(taxi1, taxi2)

# Create a Plotly figure for the interactive graph
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
