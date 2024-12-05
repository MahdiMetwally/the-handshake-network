import networkx as nx

# Function to create a new handshake network graph
def create_network():
    return nx.Graph()

# Function to add a handshake (edge) between two people
def add_handshake(graph, person1, person2):
    graph.add_edge(person1, person2)

# Function to get the nodes (people) involved in the network
def get_network(graph):
    return graph.nodes()

