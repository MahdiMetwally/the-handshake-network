import matplotlib.pyplot as plt
import networkx as nx

# Function to visualize the graph with rectangular boxes for nodes
def visualize_network(graph):
    # Generate a more spread out layout (using kamada_kawai_layout)
    pos = nx.kamada_kawai_layout(graph)  # This helps in spacing the nodes more evenly
    
    # Create the plot
    plt.figure(figsize=(12, 10))  # Increase figure size for more space

    # Customizing the node shapes and sizes:
    node_labels = nx.get_node_attributes(graph, 'label')
    
    # Draw the graph with node attributes
    nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color="skyblue", node_shape='s')  # square nodes
    nx.draw_networkx_edges(graph, pos, width=2, edge_color="gray")  # Thinner edges
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")

    # Set axis off and title
    plt.axis('off')
    plt.title("Handshake Network Graph", fontsize=16)

    # Display the plot
    plt.show()
