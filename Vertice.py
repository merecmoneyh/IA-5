'''Clase Vertice encargada de crear los vértices del Grafica, contiene métodos que permiten insertar
vecinos, obetner el Identificador del vérctice y el peso que existe entre éste y alguno adyacente'''
class Vertice:
    def __init__(self, nombre, heuristica):
        self.id = nombre
        self.heuristic = heuristica
        self.conexiones = {}
        self.visited = False
        self.parent = None
        self.weight = -1
        self.weightH = -1

    def insertarVecino(self,vecino,Peso=0):
        self.conexiones[vecino] = Peso

    def obtenerId(self):
        return self.id

    def obtenerPeso(self,vecino):
        return self.conexiones[vecino]

    def setParent(self,vertex):
        if vertex in self.conexiones:
            self.parent = vertex

    def setVisited(self, value):
        self.visited = value

    def setWeight(self, value):
        self.weight = value

    def setWeightHeuristic(self, value):
        self.weightH = value

    def setHeuristic(self, value):
        self.heuristic = value

    def getParent(self):
        return self.parent

    def getVisited(self):
        return self.visited

    def getHeuristic(self):
        return self.heuristic

    def getWeightHeuristic(self):
        return self.weightH

    def getConexiones(self):
        return self.conexiones