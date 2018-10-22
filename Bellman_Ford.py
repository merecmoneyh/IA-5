import math

'''Clase Vertice encargada de crear los vértices del Grafica, contiene métodos que permiten insertar
vecinos, obetner el Identificador del vérctice y el peso que existe entre éste y alguno adyacente'''
class Vertice:
    def __init__(self,nombre):
        self.id = nombre
        self.conexiones = {}

    def insertarVecino(self,vecino,Peso=0):
        self.conexiones[vecino] = Peso

    def obtenerId(self):
        return self.id

    def obtenerPeso(self,vecino):
        return self.conexiones[vecino]
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
        #Resutado final
        for i in self.listaBellman: print("Vertice "+str(i)+" Peso "+str(self.listaBellman[i][0])+" Predecesor "+str(self.listaBellman[i][1]))



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
#Llama al algoritmo Bellman Ford
g.BellmanFord(1)
