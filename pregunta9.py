
"""
Generar un grafo no dirigido con planetas del MCU y diseñar los algoritmos necesarios para resolver las siguientes actividades:

 

los siguientes planetas deben estar en el grafo: Tierra,Knowhere,Zen-Whoberi,Vomir,Titán,Nidavellir, agregue 7 más;
 

genere al menos 4 aristas para cada uno de los planetas del grafo, no puede haber nodos con arcos a sí mismo;
 

encuentre el árbol de expansión mínima en cuanto a costos para recorrer todos los planetas

"""



class nodoArista(object):
    def __init__(self,info,destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    def __init__(self,info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    def __init__(self,dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido
    def insertar_vertice(grafo,dato):
        nodo = nodoVertice(dato)
        if grafo.inicio is None or dato < grafo.inicio.info:
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while act is not None and act.info < nodo.info:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamanio += 1

    def insertar_arista(grafo,dato,origen, destino):
        Grafo.agregar_arista(origen.adyacentes,dato,destino.info)
        if not grafo.dirigido:
            Grafo.agregar_arista(destino.adyacentes,dato,origen.info)

    def agregar_arista(origen,dato,destino):
        nodo = nodoArista(dato,destino)
        if origen.inicio is None or origen.inicio.destino > destino:

            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while act is not None and act.destino > nodo.destino:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        origen.tamanio += 1

    def

class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0



if __name__=='__main__':
    grafo = Grafo()
    Grafo.insertar_vertice(grafo,'Tierra')
    Grafo.insertar_vertice(grafo,'Knowhere')
    Grafo.insertar_vertice(grafo,'Zen-Whoberi')
    Grafo.insertar_vertice(grafo,'Vomir')
    Grafo.insertar_vertice(grafo,'Titán')
    Grafo.insertar_vertice(grafo,'Nidavellir')
    Grafo.insertar_arista(grafo,1, 'Tierra', 'Knowhere')
    Grafo.insertar_arista(grafo,1, 'Tierra', 'Zen-Whoberi')
    Grafo.insertar_arista(grafo,1, 'Tierra', 'Vomir')
    Grafo.insertar_arista(grafo,1, 'Tierra', 'Titán')
    Grafo.insertar_arista(grafo,1, 'Knowhere', 'Nidavellir')
    Grafo.insertar_arista(grafo,1, 'Zen-Whoberi', 'Nidavellir')
    Grafo.insertar_arista(grafo,1, 'Vomir', 'Nidavellir')
    Grafo.insertar_arista(grafo,1, 'Titán', 'Nidavellir')
    Grafo.insertar_arista(grafo,1, 'Knowhere', 'Zen-Whoberi')
    Grafo.insertar_arista(grafo,1, 'Knowhere', 'Vomir')
    Grafo.insertar_arista(grafo,1, 'Knowhere', 'Titán')
    Grafo.insertar_arista(grafo,1, 'Zen-Whoberi', 'Vomir')
    Grafo.insertar_arista(grafo,1, 'Zen-Whoberi', 'Titán')
    Grafo.insertar_arista(grafo,1, 'Vomir', 'Titán')
    Grafo.insertar_arista(grafo,1, 'Nidavellir', 'Tierra')
    Grafo.insertar_arista(grafo,1, 'Nidavellir', 'Knowhere')
    Grafo.insertar_arista(grafo,1, 'Nidavellir', 'Zen-Whoberi')
    Grafo.insertar_arista(grafo,1, 'Nidavellir', 'Vomir')
