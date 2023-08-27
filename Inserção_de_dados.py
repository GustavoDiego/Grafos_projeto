import pandas as pd
class Vertice:
    def __init__(self, nome, continente=None):
        self.nome = nome
        self.continente = continente

class Grafo:
    def __init__(self):
        self.grafo = {}
        self.indices = {}  # Mapeia nomes de vértices para índices numéricos
        self.vertices_dista = []

    def vertices_di(self,vertice):
        self.vertices_dista.append(vertice)

    def adicionar_vertice(self, vertice):

        if vertice not in self.grafo:

            self.grafo[vertice] = []
            index = len(self.indices)
            self.indices[vertice] = index

    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.grafo[destino].append((origem,peso))
        self.grafo[origem].append((destino, peso))

    def listar_arestas(self):
        arestas = []
        for origem, destinos in self.grafo.items():
            for destino, peso in destinos:
                arestas.append((origem, destino, peso))
        return arestas

    def encontrar_peso_aresta(self, origem, destino):
        if origem in self.grafo:
            for v, w in self.grafo[origem]:
                if v == destino:
                    return w
        return None

# Carregar os dados da planilha atual
planilha = pd.read_excel("Database/Continental.xlsx")

# Carregar os dados da planilha intercontinental
planilha_intercontinental = pd.read_excel("Database/Intercontinental.xlsx")
# Criar um grafo
grafo = Grafo()

unique_vertex_names = set()

# Adicionar vértices com continente da planilha atual
for index, linha in planilha.iterrows():
    vertice1 = Vertice(linha["Inicio"], linha["Continente"])
    vertice2 = Vertice(linha["Fim"], linha["Continente"])

    if vertice1.nome not in unique_vertex_names:
        grafo.vertices_di(vertice1)

        unique_vertex_names.add(vertice1.nome)

    if vertice2.nome not in unique_vertex_names:
        grafo.vertices_di(vertice2)

        unique_vertex_names.add(vertice2.nome)


    grafo.adicionar_aresta(linha["Inicio"], linha["Fim"], linha["Distancia"])

# Adicionar arestas da planilha intercontinental
for index, linha in planilha_intercontinental.iterrows():
    vertice1_nome = linha["Inicio"]
    vertice2_nome = linha["Fim"]

    if vertice1_nome in grafo.grafo and vertice2_nome in grafo.grafo:
        vertice1 = vertice1_nome
        vertice2 = vertice2_nome
        grafo.adicionar_aresta(vertice1, vertice2, linha["Distancia"])