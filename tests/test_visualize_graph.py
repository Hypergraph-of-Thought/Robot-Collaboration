# tests/test_visualize_graph.py
import networkx as nx
from ollama_app import visualize_graph  # Import the function

def test_visualize_graph_empty():
    G = nx.Graph()
    visualize_graph(G)  # Call the function

def test_visualize_graph_single_node():
    G = nx.Graph()
    G.add_node(1)
    visualize_graph(G)

def test_visualize_graph_two_nodes():
    G = nx.Graph()
    G.add_edge(1, 2)
    visualize_graph(G)