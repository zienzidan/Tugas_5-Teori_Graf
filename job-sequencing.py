import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create an adjacency matrix representing adjustment times between jobs
adj_matrix = np.array(
    [
        [0, 5, 3, 4, 2, 1],
        [1, 0, 1, 2, 3, 2],
        [2, 5, 0, 1, 2, 3],
        [1, 4, 4, 0, 1, 2],
        [1, 3, 4, 5, 0, 5],
        [4, 4, 2, 3, 1, 0],
    ]
)


# Create a directed graph from the adjacency matrix
G = nx.DiGraph()

# Add nodes to the graph with labels
num_jobs = len(adj_matrix)
node_labels = {i + 1: f"J{i + 1}" for i in range(num_jobs)}
G.add_nodes_from(node_labels.keys())

# Add edges with weights representing adjustment times
for i in range(num_jobs):
    for j in range(num_jobs):
        if adj_matrix[i, j] != 0:
            G.add_edge(i + 1, j + 1, weight=adj_matrix[i, j])

pos = nx.kamada_kawai_layout(G)

labels = nx.get_edge_attributes(G, "weight")

edge_colors = range(len(labels))
cmap = plt.cm.viridis

edges = nx.draw(
    G,
    pos,
    with_labels=True,
    labels=node_labels,
    node_size=700,
    font_size=10,
    font_color="black",
    font_weight="bold",
    arrowsize=20,
    edge_color=edge_colors,
    edge_cmap=cmap,
    width=2,
)

for (edge, weight), color in zip(labels.items(), cmap(edge_colors)):
    x1, y1 = pos[edge[0]]
    x2, y2 = pos[edge[1]]
    plt.text(
        0.2 * x1 + 0.8 * x2,
        0.2 * y1 + 0.8 * y2 - 0.1,
        str(weight),
        bbox=dict(facecolor=color, alpha=0.7),
        color=color,
        horizontalalignment="center",
        verticalalignment="center",
    )

# Find the shortest path
shortest_path = nx.approximation.traveling_salesman_problem(G, cycle=False)

total_cost = 0
for i in range(len(shortest_path) - 1):
    total_cost += G[shortest_path[i]][shortest_path[i + 1]]["weight"]
    print(
        f"Edge: {shortest_path[i]} -> {shortest_path[i+1]}. Adjustment time: {G[shortest_path[i]][shortest_path[i+1]]['weight']}"
    )

# Print the shortest path and the total adjustment time
print("Shortest Path:", shortest_path)
print("Total adjustment time:", total_cost)

plt.show()
