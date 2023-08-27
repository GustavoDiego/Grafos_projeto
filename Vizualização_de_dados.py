from Inserção_de_dados import *

import networkx as nx
import matplotlib.pyplot as plt


# Criar um grafo da NetworkX
grafo_networkx = nx.Graph()

# Adicionar vértices ao grafo da NetworkX
for vertice in grafo.vertices_dista:
    grafo_networkx.add_node(vertice.nome)

# Adicionar arestas ao grafo da NetworkX
for inicio in grafo.grafo:
    for fim,peso in grafo.grafo[inicio]:
        grafo_networkx.add_edge(inicio, fim, weight=peso)


# Cores por continente
cores_continente = {"América": "blue", "Europa": "green", "Ásia": "red", "África": "purple", "Oceania": "orange"}

# Criar um dicionário para mapear continentes para cores
cores_por_continente = {continente: cor for continente, cor in cores_continente.items()}

# Criar um dicionário para mapear países para cores
cores_por_pais = {vertice.nome: cores_por_continente.get(vertice.continente, "gray") for vertice in grafo.vertices_dista}

# Layout de mola (spring layout) com distância proporcional ao peso
pos = nx.spring_layout(grafo_networkx, weight="weight", seed=42)

# Definir intervalos de peso para as cores
intervalos_cores = [(0, 999), (1000, 2500), (2501, 5000), (5001, float("inf"))]
cores = ["darkgreen", "limegreen", "yellow", "red"]

color_map = []
edge_labels = {}
for u, v, data in grafo_networkx.edges(data=True):
    peso = data['weight']
    for (min_peso, max_peso), cor in zip(intervalos_cores, cores):
        if min_peso <= peso <= max_peso:
            color_map.append(cor)
            break
    edge_labels[(u, v)] = peso
    edge_labels[(v, u)] = peso

# Plotar o grafo com vértices representados como bolas coloridas por continente e arestas coloridas pelo peso
plt.figure( figsize=(12, 8), clear=True, num="Grafo")
plt.title("Gráfico de Rede de Países")
# Desenhar nós
for node, color in cores_por_pais.items():
    nx.draw_networkx_nodes(grafo_networkx, pos, nodelist=[node], node_size=1000, node_color=color)

# Desenhar arestas
nx.draw_networkx_edges(grafo_networkx, pos, width=1.0, alpha=0.5, edge_color=color_map)

# Adicionar rótulos dos vértices
labels = {node: node for node in grafo_networkx.nodes()}
nx.draw_networkx_labels(grafo_networkx, pos, labels=labels, font_size=8)

# Adicionar rótulos das arestas (pesos)
nx.draw_networkx_edge_labels(grafo_networkx, pos, edge_labels=edge_labels, font_size=6)

# Mostrar o gráfico
plt.axis('off')
plt.show()
