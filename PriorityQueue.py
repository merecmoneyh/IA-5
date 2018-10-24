class PriorityQueue:
    '''
    Esta clase define a la estructura heap utilizada para la realización del algoritmo
    de Dijkstra.     
    '''
    def __init__(self, heap):
        self.heap = heap
        self.positions = {}
        self.build_minHeapify()

    def parent(self, i):
        '''
        Este método permite obtener el valor del índice del padre del vértice indicado.

        :return: Integer
        '''
        return (i-1)//2

    def leftChild(self, i):
        '''
        Este método permite obtener el valor del índice del hijo izquierdo del vértice indicado.

        :return: Integer
        '''
        return 2*i + 1

    def rightChild(self, i):
        '''
        Este método permite obtener el valor del índice del hijo derecho del vértice indicado.

        :return: Integer
        '''
        return 2*i + 2

    def changePosition(self, position):
        '''
        Cambiar la posición de una nodo con su padre dentro del Heap

        :return: None
        '''
        tmp = self.heap[position]
        parent = self.heap[self.parent(position)]
        self.positions[tmp.obtenerId()] = self.parent(position)
        self.positions[parent.obtenerId()] = position

    def minHeapify(self, i):
        '''
        Método para intercambiar los hijos con su padre si su peso es menor

        :i: Integer
        :return: None
        '''
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
        '''
        Extraer el  vertice con menor peso y reconstruir el heap para que seguir
        teniendo el vertice con menor peso en la posición 0

        :return: el vertice con el menor peso si le heap tiene elementos
        si no manda un menos uno
        '''
        # si el heap no tiene elementos, entonces no se puede extraer ningun
        #elemento
        if len(self.heap) == 0:
            print("error")
            return -1
        #nueva longitud del heap
        length = len(self.heap) - 1
        #extraer el vertice con menor peso
        min = self.heap[0]
        self.heap[0] = self.heap[length]
        #obtener nuevo heap sin el elemento extraido
        self.heap = self.heap[:length]
        #si el nuevo heap tiene una longitud mayor a cero cambiar
        #la posición del primer elemento
        if len(self.heap) != 0:
            self.positions[self.heap[0].obtenerId()] = 0
        #reconstruir el heap
        self.minHeapify(0)
        #eliminar el elemento extraido del diccionario de posiciones
        del self.positions[min.obtenerId()]
        return min

    def heap_decrease_key(self, value):
        '''
        Este método es para mantener el vertice con el menor peso en la posición cero
        cuando cambiamos el peso del vertice en el método relax de la gráfica

        Args: value: vertice que le fue cambiado su peso
        '''
        #obtenemos la posición del vertice que le fue cambiado su peso en relax
        position = self.positions[value.obtenerId()]
        #si el vertice no esta en la posición cero y su peso es menor al  de su padre
        #cambiar las posiciones
        #lo de posición cero es debido a que esa posición signfica en el heap que
        #es más mínimo en valor por ello ya no se checa
        while (position > 0) and (self.heap[self.parent(position)].weight > self.heap[position].weight):
            self.changePosition(position)
            tmp = self.heap[position]
            self.heap[position] = self.heap[self.parent(position)]
            self.heap[self.parent(position)] = tmp
            position = self.parent(position)
