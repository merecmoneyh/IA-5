
class Vertice:
    '''
    Clase Vertice encargada de crear los vértices de la gráfica, contiene métodos que permiten 
    insertar vecinos, obtener el identificador del vérctice en cuestión, así como 
    el peso que existe entre éste y algún otro adyacente.
    '''
    def __init__(self, nombre, heuristica):
        '''
        Constructor de la clase Verticie. Recibe el nombre del vertice y su valor de heuristica.

        :nombre: Integer
        :heuristica: Integer

        :return: None
        '''
        self.id = nombre
        self.heuristic = heuristica
        self.conexiones = {}
        self.visited = False
        self.parent = None
        self.weight = -1
        self.weightH = -1

    def insertarVecino(self,vecino,Peso=0):
        '''
        Método para insertar un vecino a la lista dde vecinos del vértice.
        Si no se da un valor para peso este se asigna por defecto como 0.

        :vecino: Vertice
        :Peso: Integer

        :return: None
        '''
        self.conexiones[vecino] = Peso

    def obtenerId(self):
        '''
        Método para obtener el identificador del vértice.

        :return: Integer
        '''
        return self.id

    def obtenerPeso(self,vecino):
        '''
        Método para obtener el peso correspondiente a la conexión con un vecino del vértice.

        :return: Vertice
        '''
        return self.conexiones[vecino]

    def setParent(self,vertex):
        '''
        Método para asignarle un padre al vértice.

        :vertex: Vertice
        :return: None
        '''
        if vertex in self.conexiones:
            self.parent = vertex

    def setVisited(self, value):
        '''
        Método para asignarle un valor a la variable que guarda el estado de visita 
        del vértice.

        :value: Boolean
        :return: None
        '''
        self.visited = value

    def setWeight(self, value):
        '''
        Método para asignarle un peso al camino que lleva al vértice desde el padre.

        :value: Float
        :return: None
        '''
        self.weight = value

    def setWeightHeuristic(self, value):
        '''
        Método para asignar un peso al camino que lleva al vértice basado en la heurística.

        :value: Float
        :return: None
        '''
        self.weightH = value

    def setHeuristic(self, value):
        '''
        Método para asignarle un valor a la heurística de este vértice.

        :value: Float
        :return: None
        '''
        self.heuristic = value

    def getParent(self):
        '''
        Método para obtener al padre del vértice.

        :return: Vertice
        '''
        return self.parent

    def getVisited(self):
        '''
        Método para obtener el estado de visita del vértice.

        :return: Boolean
        '''
        return self.visited

    def getHeuristic(self):
        '''
        Método para obtener el valor de la heurística del vértice.

        :return: Float
        '''
        return self.heuristic

    def getWeightHeuristic(self):
        '''
        Método para obtener el valor del camino hasta el vértice de acuerdo a la heurística.

        :return: Float
        '''
        return self.weightH

    def getConexiones(self):
        '''
        Método para obtener la lista con los vértices conectados al actual.

        :return: List
        '''
        return self.conexiones
