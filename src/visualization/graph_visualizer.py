import matplotlib.pyplot as plt
import networkx as nx

# Function to visualize the handshake network
def visualize_network(graph):
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')
    plt.show()

