import networkx as nx
import matplotlib.pyplot as plt
import gradio as gr

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

# Função para criar e desenhar o grafo
def draw_graph():
    # Criar o grafo direcionado
    G = nx.DiGraph()
    
    # Adicionar nós ao grafo
    G.add_nodes_from(nodes)
    
    # Adicionar arestas ao grafo
    G.add_edges_from(edges)
    
    # Desenhar o grafo
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.title("Directed Graph of LLM Variables")
    plt.show()

# Interface Gradio
iface = gr.Interface(fn=draw_graph, inputs=[], outputs="plot")

# Executar a interface
if __name__ == "__main__":
    iface.launch()