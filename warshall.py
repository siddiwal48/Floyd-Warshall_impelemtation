import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_undirected_graph(n, edge_probability=0.7, max_weight=10):
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0  # Distance to itself is 0
        for j in range(i+1, n):
            if random.random() < edge_probability:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight  # Make symmetric for undirected graph
    return graph

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def print_matrix(matrix):
    for row in matrix:
        print(["INF" if x == float('inf') else x for x in row])

def visualize_graph(graph):
    G = nx.Graph()  # Use Graph() instead of DiGraph() for undirected
    n = len(graph)
    for i in range(n):
        for j in range(i+1, n):  # Only add once for undirected
            if graph[i][j] != float('inf'):
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Undirected Weighted Graph")
    plt.show()

# MAIN
n = 5  # number of nodes
graph = generate_random_undirected_graph(n)



# Print initial adjacency matrix
print("Initial Random Graph (Adjacency Matrix):")
print_matrix(graph)


# Run Floyd-Warshall
shortest_paths = floyd_warshall(graph)


# Print shortest paths matrix
print("\nAll Pairs Shortest Path Matrix after Floyd-Warshall:")
print_matrix(shortest_paths)


# Visualize initial graph
visualize_graph(graph)
