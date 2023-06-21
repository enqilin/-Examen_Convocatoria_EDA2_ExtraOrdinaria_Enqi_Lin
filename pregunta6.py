
"""
IronHeart maestra ladrona del multiverso, ha robado de las manos de una armadura una mochila 
con muchos artefactos valiosos (Pensamos que era de un poderoso dios Azteca.). 
Pero, llegando a la nave Wakandiana se da cuenta que para escapar de las garras del malvado 
Ultrón debe desprenderse de algunos artefactos valiosos ya que su nave debe ser más ligera 
que la de ultrón y debe contener una cantidad limitada de peso. 
Su objetivo es salir con el valor combinado más alto de artefactos que quepan en la mochila, 
pero ¿cómo elige estos artículos y cuál es el valor óptimo?


Ahora vamos a ser un poco más precisos y dados los siguientes valores:

precio = [103, 60, 70, 5, 15] 

pesos = [12, 23, 11, 15, 7]

peso_maximo = 100

 

¿Cuál es el valor máximo de los artículos que se pueden agregar a la mochila de manera que el peso no exceda el límite de peso W?

SI LA MOCHILA NO ESTA LLENA SE PUEDE AGREGAR UN ARTICULO MAS
"""

def mochila(precio,peso,peso_max):
    if peso_max == 0 or len(peso) == 0 or len(precio) == 0:
        return 0
    if peso[0] > peso_max:
        return mochila(precio[1:],peso[1:],peso_max)
    return max(precio[0] + mochila(precio[1:],peso[1:],peso_max - peso[0]),mochila(precio[1:],peso[1:],peso_max))


if __name__=='__main__':
    precio = [103, 60, 70, 5, 15] 
    peso = [12, 23, 11, 15, 7]
    peso_max = 100
    a = (mochila(precio,peso,peso_max))
    print(a)