from experta import *

class Ruta(Fact):
    """Representa una ruta entre dos estaciones."""
    pass

class Exploracion(Fact):
    """Representa una estación en exploración con el tiempo acumulado y el camino recorrido."""
    pass

class DestinoUsuario(Fact):
    """Representa el destino objetivo del usuario."""
    pass

class MejorRuta(Fact):
    """Guarda la mejor ruta encontrada."""
    pass

class SistemaRutas(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.mejor_tiempo = float('inf')
        self.mejor_precio = float('inf')
        self.mejor_camino = []
        self.costo_beneficio = bool

    @Rule(Exploracion(estacion=MATCH.actual, tiempo=MATCH.tiempo_acumulado, camino=MATCH.camino, precio=MATCH.precio))
    def expandir_rutas(self, actual, tiempo_acumulado, camino, precio):
        """Expande las rutas disponibles desde la estación actual."""
        hechos = list(self.facts.values())  
        for hecho in hechos:
            if isinstance(hecho, Ruta) and hecho['origen'] == actual:
                nueva_estacion = hecho['destino']
                nuevo_tiempo = tiempo_acumulado + hecho['tiempo']
                nuevo_camino = list(camino) + [nueva_estacion]
                nuevo_precio = precio + hecho['precio']
                
                self.declare(Exploracion(estacion=nueva_estacion, tiempo=nuevo_tiempo, camino=nuevo_camino, precio=nuevo_precio))

    @Rule(Exploracion(estacion=MATCH.est, tiempo=MATCH.tiempo, camino=MATCH.camino, precio=MATCH.precio), DestinoUsuario(destino=MATCH.dest))
    def verificar_destino(self, est, tiempo, dest, camino, precio):
        """Si se alcanza el destino, se compara si es la mejor ruta encontrada."""
        if est == dest and tiempo < self.mejor_tiempo and self.costo_beneficio == False: 
            self.mejor_tiempo = tiempo
            self.mejor_precio = precio
            self.mejor_camino = list(camino)
            self.declare(MejorRuta(ruta=self.mejor_camino, tiempo=self.mejor_tiempo, precio=self.mejor_precio))
        elif est == dest and tiempo < self.mejor_tiempo and precio < self.mejor_precio:
            self.mejor_tiempo = tiempo
            self.mejor_precio = precio
            self.mejor_camino = list(camino)
            self.declare(MejorRuta(ruta=self.mejor_camino, tiempo=self.mejor_tiempo, precio=self.mejor_precio))

    def iniciar_busqueda(self, origen, destino, costo_beneficio_input):
        """Inicializa la búsqueda desde la estación de origen."""
        
        if costo_beneficio_input == "Y":
            self.costo_beneficio = True
        else:
            self.costo_beneficio = False
        
        self.reset()
        self.declare(DestinoUsuario(destino=destino))
        self.declare(Exploracion(estacion=origen, tiempo=0, camino=[origen], precio=0))
        for ruta in rutas:
            self.declare(Ruta(origen=ruta[0], destino=ruta[1], tiempo=ruta[2], precio=ruta[3]))
        self.run()
        if self.mejor_camino:
            print(f"\n Mejor ruta encontrada: {' → '.join(self.mejor_camino)} con tiempo {self.mejor_tiempo} min. y precio {self.mejor_precio} COP.")
        else:
            print("\n No hay ruta disponible entre los puntos ingresados.")

rutas = [
    ("A", "B", 5, 5000),
    ("A", "C", 10, 2000),
    ("B", "D", 7, 3000),
    ("B", "E", 3, 7000),
    ("C", "F", 12, 2000),
    ("E", "F", 4, 5000),
    ("D", "F", 6, 7000),
]

origen = input("Ingrese la estación de origen: ").strip().upper()
destino = input("Ingrese la estación de destino: ").strip().upper()
costo_beneficio_input = input("Desea considerar el costo de transporte (y/n): ").strip().upper()

engine = SistemaRutas()
engine.iniciar_busqueda(origen, destino, costo_beneficio_input)
