import networkx as nx
import matplotlib.pyplot as plt

# Function to create a new handshake network graph
def create_network():
    return nx.Graph()

# Function to add a handshake (edge) between two people
def add_handshake(graph, person1, person2):
    graph.add_edge(person1, person2)

# Function to get the nodes (people) involved in the network
def get_network(graph):
    return graph.nodes()

# Function to visualize the graph in a tree-like layout
def visualize_network(graph):
    # Generate a tree-like layout (using spring_layout for now)
    pos = nx.spring_layout(graph, seed=42)  # seed for reproducibility

    # Draw the graph with more aesthetics
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray", width=2)

    # Add title and display the plot
    plt.title("Handshake Network Graph", fontsize=16)
    plt.show()

