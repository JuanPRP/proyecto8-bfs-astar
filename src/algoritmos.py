from src.estructuras import Cola   

def bfs(grafo, inicio, meta):
    previo = {inicio: None}        
    cola = Cola()
    cola.encolar(inicio)
    while not cola.vacia():
        u = cola.desencolar()
        if u == meta:
            camino = []
            while u is not None:
                camino.append(u)
                u = previo[u]
            return camino[::-1]         # devolvemos el camino en orden correcto
        for v in grafo.vecinos(u):
            if v not in previo:
                previo[v] = u
                cola.encolar(v)
    return None                    

#A* con heuristica Manhattan