# ollama/ollama_app.py
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G):
    """
    Visualize a graph using matplotlib.

    Args:
        G: A NetworkX graph object.
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues)
    plt.show()

# Rest of your code in ollama_app.py