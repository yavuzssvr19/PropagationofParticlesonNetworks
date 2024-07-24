import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

# Just make a chain like 1->2->3->4
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])
pos = nx.spring_layout(G)
fig, ax = plt.subplots()
# Drawing the Graph
nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray', node_size=500, font_size=16, ax=ax)
plt.show()
# Call the adjacency matrix A
A = nx.adjacency_matrix(G)
A = csr_matrix(A)  # transform scipy.sparse format
print(A.toarray())

# Calculate and visualize matrix power
def plot_heatmap(matrix, title):
    plt.figure(figsize=(6, 6))
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

# simulate t=0
A0 = np.linalg.matrix_power(A.toarray(), 0)
plot_heatmap(A0, 't=0 (A^0)')
# Simulate t=1
A1 = np.linalg.matrix_power(A.toarray(), 1)
plot_heatmap(A1, 't=1 (A^1)')
# Simulate t=2
A2 = np.linalg.matrix_power(A.toarray(), 2)
plot_heatmap(A2, 't=2 (A^2)')
# Simulate t=3
A3 = np.linalg.matrix_power(A.toarray(), 3)
plot_heatmap(A3, 't=3 (A^3)')
# Simulate t=4
A4 = np.linalg.matrix_power(A.toarray(), 4)
plot_heatmap(A4, 't=4 (A^4)')
# Simulate t=100
A100 = np.linalg.matrix_power(A.toarray(), 100)
plot_heatmap(A100, 't=100 (A^100)')

# Making the weird looking graphs
G_weird = nx.erdos_renyi_graph(10, 0.3)
A_weird = nx.adjacency_matrix(G_weird)
A_weird = csr_matrix(A_weird)  # scipy.sparse formatına dönüştürme

# Simulate t=1
A_weird_1 = np.linalg.matrix_power(A_weird.toarray(), 1)
plot_heatmap(A_weird_1, 'Weird Graph t=1 (A^1)')

# Simulate t=2
A_weird_2 = np.linalg.matrix_power(A_weird.toarray(), 2)
plot_heatmap(A_weird_2, 'Weird Graph t=2 (A^2)')

# Simulate t=3
A_weird_3 = np.linalg.matrix_power(A_weird.toarray(), 3)
plot_heatmap(A_weird_3, 'Weird Graph t=3 (A^3)')

