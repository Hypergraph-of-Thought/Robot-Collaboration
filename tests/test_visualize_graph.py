def test_empty_graph(self):
    G = nx.Graph()
    try:
        visualize_graph(G)
    except Exception as e:
        self.fail(f"visualize_graph raised {e} unexpectedly!")

def test_single_node_graph(self):
    G = nx.Graph()
    G.add_node(1)
    try:
        visualize_graph(G)
    except Exception as e:
        self.fail(f"visualize_graph raised {e} unexpectedly!")

def test_simple_graph(self):
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3)])
    try:
        visualize_graph(G)
    except Exception as e:
        self.fail(f"visualize_graph raised {e} unexpectedly!")