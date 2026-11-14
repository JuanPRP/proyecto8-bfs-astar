class Nodo:
    """Nodo de lista enlazada: guarda un dato y apunta al siguiente."""

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class Cola:
    def __init__(self):
        self._frente = None    
        self._final = None     
        self._n = 0            # cantidad de elementos

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self._final is None:
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._n += 1

    def desencolar(self):
        if self._frente is None:
            raise IndexError("Cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._n -= 1
        return dato

    def vacia(self):
         if self._frente is None:
            return True
         else:
            return False

    def __len__(self):
        return self._n


c = Cola()
c.encolar("A")
c.encolar("B")
c.encolar("C")
print(len(c))
print(c.desencolar())
print(c.desencolar())
print(c.desencolar())
print(c.vacia())
c.encolar("D")
print(c.desencolar())
print(c.vacia())
#MonticuloMin Faltan par mas adelante