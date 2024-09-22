import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from ollama import Ollama

# Inicializar o modelo LLaMA
MODEL_PATH = "path/to/llama-3.1.GGUF"
ollama = Ollama(model_path=MODEL_PATH)

def generate_text(prompt):
    try:
        response = ollama.generate(prompt, max_tokens=50)
        return response['text']
    except Exception as e:
        st.error(f"Erro ao gerar texto: {e}")
        return ""

def create_directional_graph(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def visualize_graph(G):