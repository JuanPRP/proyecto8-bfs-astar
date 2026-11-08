class Grafo:
    """Grafo no dirigido con pesos, en lista de adyacencia."""

    def __init__(self):
        self._ady = {}          # {(f, c): [((f2, c2), w), ...]}
        self._num_aristas = 0

    def _validar(self, u):
        if u not in self._ady:
            raise ValueError(f"{u} no es un vértice del grafo")

    def agregar_vertice(self, u):
        if u not in self._ady:
            self._ady[u] = []

    def agregar_arista(self, u, v, w=1):
        self._validar(u)
        self._validar(v)
        if u == v:
            raise ValueError("u y v deben ser distintos")
        if self.existe_arista(u, v):
            raise ValueError("la arista ya existe")
        self._ady[u].append((v, w))
        self._ady[v].append((u, w))
        self._num_aristas += 1

    def existe_arista(self, u, v):
        self._validar(u)
        self._validar(v)
        for vecino, _ in self._ady[u]:
            if vecino == v:
                return True
        return False

    def vecinos(self, u):
        self._validar(u)
        return [v for v, _ in self._ady[u]]

    def peso(self, u, v):
        self._validar(u)
        for vecino, w in self._ady[u]:
            if vecino == v:
                return w
        raise ValueError("la arista no existe")

    def vertices(self):
        return list(self._ady)

    def num_vertices(self):
        return len(self._ady)

    def num_aristas(self):
        return self._num_aristas

    @classmethod
    def desde_mapa(cls, mapa):
        """Construye el grafo desde una matriz de 0 (libre) y 1 (obstáculo)."""
        grafo = cls()
        filas, cols = len(mapa), len(mapa[0])
        for f in range(filas):
            for c in range(cols):
                if mapa[f][c] == 0:
                    grafo.agregar_vertice((f, c))
        for f in range(filas):
            for c in range(cols):
                if mapa[f][c] != 0:
                    continue
                for df, dc in ((1, 0), (0, 1)):   # abajo y derecha
                    nf, nc = f + df, c + dc
                    if nf < filas and nc < cols and mapa[nf][nc] == 0:
                        grafo.agregar_arista((f, c), (nf, nc), 1)
        return grafo
