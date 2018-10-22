import math

class PriorityQueue:

    def __init__(self, heap):
        self.heap = heap
        self.positions = {}
        self.build_minHeapify()

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*i + 1

    def rightChild(self, i):
        return 2*i + 2

    def changePosition(self, position):
        tmp = self.heap[position]
        parent = self.heap[self.parent(position)]
        self.positions[tmp.obtenerId()] = self.parent(position)
        self.positions[parent.obtenerId()] = position

    def minHeapify(self, i):
        length = len(self.heap)
        left = self.leftChild(i)
        right = self.rightChild(i)
        parent = i
        if (left < length) and (self.heap[left].weight < self.heap[i].weight):
            parent = left
        if (right < length) and (self.heap[right].weight < self.heap[parent].weight):
            parent = right
        if parent != i:
            self.changePosition(parent)
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[i]
            self.heap[i] = tmp
            return self.minHeapify(parent)

    def build_minHeapify(self):
        length = len(self.heap)
        numberOfParents=(length//2) - 1
        for i in range(numberOfParents, -1, -1):
            self.minHeapify(i)
        index = 0
        #add postions for every node
        for i in self.heap:
            self.positions[i.obtenerId()] = index
            index = index + 1

    def heap_extract_min(self):
        if len(self.heap) == 0:
            print("error")
            return -1
        length = len(self.heap) - 1
        min = self.heap[0]
        self.heap[0] = self.heap[length]
        self.heap = self.heap[:length]
        if len(self.heap) != 0:
            self.positions[self.heap[0].obtenerId()] = 0
        self.minHeapify(0)
        del self.positions[min.obtenerId()]
        return min

    def heap_decrease_key(self, value):
        position = self.positions[value.obtenerId()]
        while (position > 0) and (self.heap[self.parent(position)].weight > self.heap[position].weight):
            self.changePosition(position)
            tmp = self.heap[position]
            self.heap[position] = self.heap[self.parent(position)]
            self.heap[self.parent(position)] = tmp
            position = self.parent(position)

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

'''Clase Grafica es donde se crea el Grafica con todos sus vértices, tiene sus métodos que permiten insertar un nuevo vértice,
una nueva arista, el método __iter__ para facilitar la iteración sobre todos los objetos vértice de un Grafica en particular.'''
class Grafica:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
        self.listaBellman = {}

    def insertarVertice(self, nombre, heuristica = 0):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(nombre, heuristica)
        self.listaVertices[nombre] = nuevoVertice
        return nuevoVertice

    def insertarArista(self,origen,destino,costo=0):
        if origen not in self.listaVertices:
            nv = self.insertarVertice(origen)
        if destino not in self.listaVertices:
            nv = self.insertarVertice(destino)
        self.listaVertices[origen].insertarVecino(self.listaVertices[destino], costo)

    def __iter__(self):
        return iter(self.listaVertices.values())


    '''Es un algoritmo que determina la ruta más corta desde un
        nodo hacia todos los demás en una gráfica dirigida con pesos asociados a las aristas.'''
    def BellmanFord(self, origen):
        '''Asignar a cada nodo una distancia un nodo predecesor tentativos: (0 para el nodo inicial,
        ∞ para todos los nodos restantes); (predecesor nulo para todos los nodos)'''
        for v in self:
            lista=[]
            lista.append(math.inf)
            lista.append(None)
            self.listaBellman[v.obtenerId()]=lista
            self.listaBellman[origen][0]=0
        '''Si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor que
        la distancia tentativa al nodo v, sobreescribir la distancia a v con la suma mencionada
        y guardar a u como predecesor de v.'''
        for i in range(self.numVertices-1):
            for v in self:
                for c in v.conexiones:
                    nuevaDis=self.listaBellman[v.obtenerId()][0]+v.obtenerPeso(c)
                    if(nuevaDis<self.listaBellman[c.obtenerId()][0]):
                        self.listaBellman[c.obtenerId()][0]=nuevaDis
                        self.listaBellman[c.obtenerId()][1]=v.obtenerId()
        '''Si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor
        que la distancia tentativa al nodo v, devolver un mensaje de error indicando que existe
        un ciclo de peso negativo.'''
        for v in self:
                for c in v.conexiones:
                    nuevaDis=self.listaBellman[v.obtenerId()][0]+v.obtenerPeso(c)
                    if(nuevaDis<self.listaBellman[c.obtenerId()][0]):
                        print("Error: Ciclo Negativo")
                        return False

    def ResultadoBellman(self):
        for i in self.listaBellman: print("Vertice "+str(i)+" Peso "+str(self.listaBellman[i][0])+" Predecesor "+str(self.listaBellman[i][1]))

    def initialize_single_source(self, s):
        if s in self.listaVertices:
            vertex = self.listaVertices[s]
            for i in self.listaVertices.values():
                i.setWeight(math.inf)
                i.setWeightHeuristic(math.inf)
                i.setVisited(False)
                i.setParent(None)
            vertex.setWeight(0)
            vertex.setWeightHeuristic(0)
            vertex.setHeuristic(0)

    def relax(self, a, b, heap):
        w = a.obtenerPeso(b)
        if b.weight > (a.weight + w):
            b.weight = a.weight + w
            b.setParent(a)
            heap.heap_decrease_key(b)


    def dijkstra(self, a):
        if (a in self.listaVertices):
            self.initialize_single_source(a)
            l = []
            for i in self.listaVertices.values():
                l.append(i)
            heapDikstra = PriorityQueue(l)
            while (len(heapDikstra.heap) != 0):
                current = heapDikstra.heap_extract_min()
                for i in current.getConexiones().keys():
                    if i.getVisited() != True:
                        self.relax(current, i, heapDikstra)
                current.setVisited(True)
            self.ResultadoDijkstra()

    def ResultadoDijkstra(self):
        for i in self.listaVertices.values():
            print( "id " + str(i.obtenerId()) + " el peso es " + str(i.weight), end = " ")
            if i.getParent() != None:
                print(" parent " + str(i.getParent().obtenerId()))
                continue
            print(" parent " + str(None))

    def rebuildPath(self, a):
        actual = a
        camino = []
        camino.append(actual.id)
        while actual.getParent() != None:
            actual = actual.getParent()
            camino.append(actual)
            actual = self.listaVertices[actual]
        return camino

    def minHeuristic(self, oSet):
        a = []
        b = []
        for i in oSet:
            if i in self.listaVertices:
                aux = self.listaVertices[i]
                a.append(aux.id)
                b.append(aux.weightH)
        c = min(b)
        c = b.index(c)
        return a[c]

    def aStar(self, a, b):
        oSet = []
        if a in self.listaVertices:
            self.initialize_single_source(a)
            oSet.append(a)

            while len(oSet) > 0:
                aux = self.minHeuristic(oSet)
                actual = self.listaVertices[aux]
                if actual.id == b:
                    return self.rebuildPath(actual)
                oSet.remove(aux)
                actual.setVisited(True)
                for i in actual.conexiones.keys():
                    vecino = self.listaVertices[i.id]
                    if vecino.getVisited() == False:
                        if i.id not in oSet:
                            oSet.append(i.id)
                        if (actual.weight + actual.conexiones[i]) < vecino.weight:
                            vecino.parent = actual.id
                            vecino.weight = actual.weight + actual.conexiones[i]
                            vecino.weightH = vecino.weight + vecino.heuristic
        return False
