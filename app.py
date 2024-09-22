import networkx as nx
import matplotlib.pyplot as plt

# Definir as variáveis como nós do grafo
nodes = [
    "Number of Open-Source LLM Projects",
    "Cost of Cloud-Based LLM APIs",
    "Number of LLM-based Applications",
    "User Expertise Required for LLM Deployment",
    "Public Awareness of LLMs"
]

# Definir as arestas do grafo com base nas relações causais
edges = [
    ("Number of Open-Source LLM Projects", "Number of LLM-based Applications"),
    # Adicione outras arestas conforme necessário
]

# Criar o grafo direcionado
G = nx.DiGraph()

# Adicionar nós ao grafo
G.add_nodes_from(nodes)

# Adicionar arestas ao grafo
G.add_edges_from(edges)

# Desenhar o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Directed Graph of LLM Variables")
plt.show()