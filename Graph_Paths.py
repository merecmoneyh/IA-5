import math

class PriorityQueue:

    def __init__(self, heap):
        self.heap = heap
        self.build_minHeapify()

    def parent(self, i):
        return (i-1)//2;

    def leftChild(self, i):
        return 2*i + 1

    def rightChild(self, i):
        return 2*i + 2

    def minHeapify(self, l, i):
        length = len(l)
        left = self.leftChild(i)
        right = self.rightChild(i)
        parent = i
        #list is like this [vertex0, vertex1]
        if (left < length) and (l[left].weight < l[i].weight):
            parent = left
        if (right < length) and (l[right].weight < l[parent].weight):
            parent = right
        if parent != i:
            tmp = l[parent]
            l[parent] = l[i]
            l[i] = tmp
            return self.minHeapify(l, parent)

    def build_minHeapify(self):
        length = len(self.heap)
        numberOfParents=(length//2) - 1
        for i in range(numberOfParents, -1, -1):
            self.minHeapify(self.heap, i)

    def heap_extract_min(self):
        if len(self.heap) == 0:
            print("error")
            return -1
        length = len(self.heap) - 1
        min = self.heap[0]
        self.heap[0] = self.heap[length]
        self.heap = self.heap[:length]
        self.minHeapify(self.heap, 0)
        print("hola")
        print("min " + str(min.obtenerId()))
        for i in self.heap:
            print(str(i.obtenerId()) + " weight " +str(i.weight) )
        return min

    def max_heap_insert(self, value):
        self.heap.append(value)
        length = len(self.heap) - 1
        while (length > 0) and (self.heap[self.parent(length)].weight > self.heap[length].weight):
            tmp = self.heap[length]
            self.heap[length] = self.heap[self.parent(length)]
            self.heap[self.parent(length)] = tmp
            length = self.parent(length)
'''Clase Vertice encargada de crear los vértices del Grafica, contiene métodos que permiten insertar
vecinos, obetner el Identificador del vérctice y el peso que existe entre éste y alguno adyacente'''
class Vertice:
    def __init__(self,nombre):
        self.id = nombre
        self.conexiones = {}
        self.visited = False
        self.distance = -1
        self.parent = None
        self.weight = -1

    def insertarVecino(self,vecino,Peso=0):
        self.conexiones[vecino] = Peso

    def obtenerId(self):
        return self.id

    def obtenerPeso(self,vecino):
        return self.conexiones[vecino]

    def setParent(self,vertex):
        if vertex in self.conexiones:
            self.parent = vertex

    def setDistance(self, value):
        self.distance = value

    def setVisited(self, value):
        self.visited = value

    def setWeight(self, value):
        self.weight = value

    def getParent(self):
        return self.parent

    def getDistance(self):
        return self.distance

    def getVisited(self):
        return self.visited

'''Clase Grafica es donde se crea el Grafica con todos sus vértices, tiene sus métodos que permiten insertar un nuevo vértice,
una nueva arista, el método __iter__ para facilitar la iteración sobre todos los objetos vértice de un Grafica en particular.'''
class Grafica:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
        self.listaBellman = {}

    def insertarVertice(self,nombre):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(nombre)
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
                i.setVisited(False)
                i.setParent(None)
            vertex.setWeight(0)

    def relax(self, a, b, heap):
        w = a.obtenerPeso(b)
        if b.weight > (a.weight + w):
            b.weight = a.weight + w
            b.setParent(a)
            heap.max_heap_insert(b)


    def dijkstra(self, a):
        if (a in self.listaVertices):
            self.initialize_single_source(a)
            l = []
            #for i in self.listaVertices.values():
            #    l.append(i)
            l.append(self.listaVertices[a])
            heapDikstra = PriorityQueue(l)
            while (len(heapDikstra.heap) != 0):
                current = heapDikstra.heap_extract_min()
                for i in current.conexiones.keys():
                    self.relax(current, i, heapDikstra)

    def ResultadoDijkstra(self):
        for i in self.listaVertices.values():
            print( "id " + str(i.obtenerId()) + " el peso es " + str(i.weight), end = " ")
            if i.getParent() != None:
                print(" parent " + str(i.getParent().obtenerId()))
                continue
            print(" parent " + str(None))

#Crea el Grafica
g = Grafica()
#Inserta Vertices
for i in range(1,6):
    g.insertarVertice(i)
#Inserta Aristas
g.insertarArista(1,2,7)
g.insertarArista(1,3,9)
g.insertarArista(1,6,14)
g.insertarArista(2,1,7)
g.insertarArista(2,3,10)
g.insertarArista(2,4,15)
g.insertarArista(3,1,9)
g.insertarArista(3,2,10)
g.insertarArista(3,4,11)
g.insertarArista(3,6,2)
g.insertarArista(4,2,15)
g.insertarArista(4,3,11)
g.insertarArista(4,5,6)
g.insertarArista(5,4,6)
g.insertarArista(5,6,9)
g.insertarArista(6,1,14)
g.insertarArista(6,3,2)
g.insertarArista(6,5,9)


print("Graph")
g.dijkstra(1)
g.ResultadoDijkstra()

print("Grafo z")

z = Grafica()
l = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
[4, 0, 8, 0, 0, 0, 0, 11, 0],
[0, 8, 0, 7, 0, 4, 0, 0, 2],
[0, 0, 7, 0, 9, 14, 0, 0, 0],
[0, 0, 0, 9, 0, 10, 0, 0, 0],
[0, 0, 4, 14, 10, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 2, 0, 1, 6],
[8, 11, 0, 0, 0, 0, 1, 0, 7],
[0, 0, 2, 0, 0, 0, 6, 7, ],
]

for i in range(9):
    z.insertarVertice(i)
row = 0
for i in l:
    column = 0
    for j in i:
        if j != 0:
            z.insertarArista(row,column,j)
        column = column + 1
    row = row + 1

z.dijkstra(0)
z.ResultadoDijkstra()
