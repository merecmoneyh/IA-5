"""Versión de Python utilizada 3.7.0 (Recomendado utilizar la consola de Linux o cmd en Windows)

	Integrantes:
	- Aco Guerrero Iván Rogelio
	- Ricardo Hernández Gómez
	- Hernández Arrieta Carlos Alberto
	- Hernández García Luis Angel

	Éste es un programa desmuestra el funcionamiento de los algoritmos de búsqueda de rutas:
    -Dijkstra
    -Bellman-Ford
    -A*
"""
from Grafica import Grafica

def main():
    """Función principal main	"""
    # Variables:
    opcion = 0
    grafica = None

    print("**** Algoritmos de busqueda ****")
    print("Escoja una opcion:\
    \n\t1. Cargar grafica desde archivo .json\
    \n\t2. Dijkstra\
    \n\t3. Bellman-Ford\
    \n\t4. A*\
    \n\t5. Salir")
    
    while opcion != "5":
        opcion = input("\n\tOpcion: ")
        
        if opcion == "1":
            try:
                file_name = input("\t\tNombre del archivo json: ")
                grafica = Grafica()
                grafica.leerArchivo(file_name)
                print("\n\tArchivo cargado exitosamente\n")
            except:
                grafica = None
                print("\t\tEl archivo no existe")
        if grafica:
            if opcion == "2":
                origen = int(input("\t\tOrigen: "))
                try:
                    grafica.dijkstra(origen)
                except:
                    print("\t\tEl origen no existe")
            elif opcion == "3":
                origen = int(input("\t\tOrigen: "))
                try:
                    grafica.BellmanFord(origen)
                except:
                    print("\t\tEl origen no existe")
            elif opcion == "4":
                origen = int(input("\t\tOrigen: "))
                destino = int(input("\t\tDestino: "))
                try:
                    grafica.aStar(origen, destino)
                except:
                    print("\t\tDatos incorrectos")
        else:
            print("\n\tElija una opción válida\n")

if __name__ == '__main__':
    main()