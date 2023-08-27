
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

