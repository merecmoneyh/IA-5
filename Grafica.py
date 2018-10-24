import math, json
from PriorityQueue import *
from Vertice import *

class Grafica:
    '''
    Clase Grafica es donde se crea el Grafica con todos sus vértices, tiene sus métodos 
    que permiten insertar un nuevo vértice, una nueva arista, el método __iter__ para 
    facilitar la iteración sobre todos los objetos vértice de un Grafica en particular.
    '''

    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0
        self.listaBellman = {}

    def leerArchivo(self, file_name):
        '''
        Lee un archivo json. Se leen los vértices de una lista, las aristas de una lista de listas.
        Cada lista de la lista de aristas cuenta con 3 índices:
        -origen
        -destino
        -peso

        :file_name: String
        :return: None
        '''
        file_data = open(file_name).read()
        data = json.loads(file_data)
        lista_vertices = data["vertices"]
        lista_aristas = data["aristas"]
        self.insertarVertices(lista_vertices)
        self.insertarAristas(lista_aristas)

    def insertarVertices(self, vertices):
        '''
        Este método lee los vértices de una lista y los agrega a la Gráfica.
        El proceso varía si se incluyen valores de heurística para cada vértice.

        :vertices: List
        :return: None
        '''
        for vertice in vertices:
            if isinstance(vertice, list):
                self.insertarVertice(vertice[0], vertice[1])
            else:
                self.insertarVertice(vertice)

    def insertarAristas(self, aristas):
        '''
        Este método lee las aristas de una lista y los agrega a la Gráfica.
        
        :aristas: List
        :return: None
        '''
        for arista in aristas:
            self.insertarArista(arista[0], arista[1], arista[2])

    def insertarVertice(self, nombre, heuristica = 0):
        '''
        Este método permite agregar un vértices a la gráfica.
        Si no se proporciona un valor para la heurística este se asigna por defecto como 0.

        :nombre: Integer
        :heuristica: Integer

        :return: Vertice 
        '''
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(nombre, heuristica)
        self.listaVertices[nombre] = nuevoVertice
        return nuevoVertice

    def insertarArista(self,origen,destino,costo=0):
        '''
        Este método permite agregar valores de aristas a la gráfica.
        Si no se especifica un costo este se asgina por defecto como 0.

        :origen: Integer
        :destino: Integer
        :costo: Integer

        :return: None
        '''
        if origen not in self.listaVertices:
            self.insertarVertice(origen)
        if destino not in self.listaVertices:
            self.insertarVertice(destino)
        self.listaVertices[origen].insertarVecino(self.listaVertices[destino], costo)

    def __iter__(self):
        return iter(self.listaVertices.values())


    def BellmanFord(self, origen):
        '''
        Es un algoritmo que determina la ruta más corta desde un
        nodo hacia todos los demás en una gráfica dirigida con pesos asociados a las aristas.

        :origen: Integer
        :return: None
        '''
        
        for v in self:
            '''
            Asignar a cada nodo una distancia un nodo predecesor tentativos: (0 para el nodo inicial,
            ∞ para todos los nodos restantes); (predecesor nulo para todos los nodos)
            '''
            lista=[]
            lista.append(math.inf)
            lista.append(None)
            self.listaBellman[v.obtenerId()]=lista
        self.listaBellman[origen][0]=0
        '''Repetir |V | − 1 veces'''
        for i in range(self.numVertices-1):
            '''Para cada arista (u, v) con peso w:'''
            for v in self:
                '''Si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor que
                la distancia tentativa al nodo v, sobreescribir la distancia a v con la suma mencionada
                y guardar a u como predecesor de v.'''
                for c in v.conexiones:
                    nuevaDis=self.listaBellman[v.obtenerId()][0]+v.obtenerPeso(c)
                    if(nuevaDis<self.listaBellman[c.obtenerId()][0]):
                        self.listaBellman[c.obtenerId()][0]=nuevaDis
                        self.listaBellman[c.obtenerId()][1]=v.obtenerId()
        '''Verificar que no existan ciclos de pesos negativos:'''
        '''Para cada arista (u, v) con peso w:'''
        for v in self:
                '''Si la distancia del nodo actual u sumada al peso w de la arista que llega a v es menor
                que la distancia tentativa al nodo v, devolver un mensaje de error indicando que existe
                 un ciclo de peso negativo.'''
                for c in v.conexiones:
                    nuevaDis=self.listaBellman[v.obtenerId()][0]+v.obtenerPeso(c)
                    if(nuevaDis<self.listaBellman[c.obtenerId()][0]):
                        print("Error: Ciclo Negativo")
                        return False
        #Resultado Final
        for i in self.listaBellman: print("Vertice "+str(i)+" Peso "+str(self.listaBellman[i][0])+" Predecesor "+str(self.listaBellman[i][1]))

    def initialize_single_source(self, s):
        '''
        Metodo para inicializar todos los vertices con peso
        infinito, que no hayan sido visitados aún, no tengan Padre

        :s: Vertice
        :return: None
        '''
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
        '''
        Método para checar si cambiamos el peso de un vertice si el peso
        del vertice "a" sumado con el peso de la arista(a,b) es menor al
        peso actual de "b"

        Args; a: posible padre
        b: nodo que se le podría cambiar su peso

        :a: Vertice
        :b: Vertice
        :heap: PriorityQueue
        :return: None
        '''
        w = a.obtenerPeso(b)
        if b.weight > (a.weight + w):
            b.weight = a.weight + w
            b.setParent(a)
            heap.heap_decrease_key(b)

    def dijkstra(self, a):
        '''
        Método para calcular el camino más corto para cada vértice
        dado un nodo inicial

        Args: a: nodo inicial
        
        :a: Vertice
        :return: None
        '''
        if (a in self.listaVertices):
            #inicializar vertices
            self.initialize_single_source(a)
            l = []
            #agregar todos los vertices a la lista l
            for i in self.listaVertices.values():
                l.append(i)
            heapDikstra = PriorityQueue(l)
            while (len(heapDikstra.heap) != 0):
                #extraer el vertice con peso mínimo
                current = heapDikstra.heap_extract_min()
                #recorrer las vecinos de current
                for i in current.getConexiones().keys():
                    if i.getVisited() != True:
                        #ver si cambiamos el peso del vecino o no
                        self.relax(current, i, heapDikstra)
                current.setVisited(True)
            self.ResultadoDijkstra()

    def ResultadoDijkstra(self):
        '''
        Método para imprimir el resultado del algoritmo de dijkstra.

        :return: None
        '''
        for i in self.listaVertices.values():
            print( "id " + str(i.obtenerId()) + " el peso es " + str(i.weight), end = " ")
            if i.getParent() != None:
                print(" parent " + str(i.getParent().obtenerId()))
                continue
            print(" parent " + str(None))

    def rebuildPath(self, a):
        '''
        Método para reconstruir los caminos de los algorismos de Dijkstra y Bellman-Ford,
        desde el último nodo 'a'.

        :a: Vertice 
        :return: List
        '''
        actual = a
        camino = []
        peso = str(actual.weight)
        camino.append(actual.obtenerId())
        while actual.getParent() != None:
            actual = actual.getParent()
            camino.insert(0, actual)
            actual = self.listaVertices[actual]
        print("Peso: " + peso)
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
        '''
        Este método ejecuta la búsqueda del camino más obtimo desde 'a' a 'b'
        utilizando el algoritmo A*.

        :a: Vertice
        :b: Vertice
        '''
        oSet = []
        if a in self.listaVertices:
            self.initialize_single_source(a)
            oSet.append(a)

            while len(oSet) > 0:
                aux = self.minHeuristic(oSet)
                actual = self.listaVertices[aux]
                if actual.id == b:
                    print(self.rebuildPath(actual))
                    return
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
