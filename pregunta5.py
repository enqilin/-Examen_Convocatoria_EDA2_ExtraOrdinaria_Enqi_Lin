
"""""
Implementa una función recursiva llamada “hijo sin amor” que le permita a Namor en su último aliento y “con ayuda del dios Kukulcán” realizar las siguientes actividades:


sacar los objetos de la mochila de a uno a la vez hasta encontrar un anillo de poder o que no queden más objetos en la mochila;
 

Determinar si la mochila contiene un anillo de poder y cuantos objetos fueron necesarios sacar para encontrarlo;
 

Utilizar una lista para representar la mochila.

"""

# crea un nodo pila y pila
class Nodopila(object):
    def __init__(self):
        self.info = None
        self.siguiente = None

class pila(object):
    def __init__(self):
        self.cima = None
        self.tamano = 0

    def apilar(pila,dato):
        nodo = Nodopila()
        nodo.info = dato
        nodo.siguiente = pila.cima
        pila.cima = nodo
        pila.tamano += 1

    def desapilar(pila):
        dato = pila.cima.info
        pila.cima = pila.cima.siguiente
        pila.tamano -= 1
        return dato
    
    def cima(pila):
        return pila.cima.info
    
lista = ['anillo de poder','piedra del alma','piedra del tiempo','piedra del espacio','piedra de la mente','piedra del poder']
lista1 = ['piedra del alma','piedra del tiempo','piedra del espacio','piedra de la mente','piedra del poder']


def hijo_sin_amor(mochila):
    for i in mochila:
        Pila = pila()
        Pila.apilar(i)
        numero = 0
        if anillo_de_poder(Pila) == True:
            print('Se encontro el anillo de poder',numero)
            break
        else:
            numero += 1

def anillo_de_poder(mochila):
    if mochila.cima() == 'anillo de poder':
        return True
    else:
        mochila.desapilar()
        return hijo_sin_amor(mochila)
    
if __name__=='__main__':
    mochila = pila()
    for i in lista:
        mochila.apilar(i)
    hijo_sin_amor(mochila)
    
    mochila1 = pila()
    for i in lista1:
        mochila1.apilar(i)
    hijo_sin_amor(mochila1)