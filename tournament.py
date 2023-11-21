import networkx as nx

# Matriks adjacency untuk merepresentasikan hasil pertandingan
# tim 1 mengalahkan tim 2
# tim 3 mengalahkan tim 4
edges = [
    (1, 2),
    (1, 3),
    (1, 5),
    (1, 6),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 2),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 1),
    (5, 6),
    (6, 2),
    (6, 4),
]

# Membuat directed graph menggunakan NetworkX
G = nx.DiGraph()

for match in edges:
    G.add_edge(match[0], match[1])

# Menghitung PageRank
pagerank_scores = nx.pagerank(G)

# Menampilkan ranking
# PageRank score yang lebih kecil menandakan tim yang lebih baik
print(pagerank_scores.items())
sorted_teams = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=False)

print("Ranking:")
for i, (team, score) in enumerate(sorted_teams):
    print(f"{i+1}. Team {team} - PageRank Score: {score:.4f}")
