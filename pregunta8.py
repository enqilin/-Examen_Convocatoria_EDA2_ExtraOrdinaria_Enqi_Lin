
class Nodo(object):
    def __init__(self,valor,frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    
class Arbol(object):
    def __init__(self):
        self.raiz = None

    def insertar(self,valor,frecuencia):
        if self.raiz ==None:
            self.raiz = Nodo(valor,frecuencia)
        else:
            self.insertar_aux(self.raiz,valor,frecuencia)

 def insertar_aux(self,nodo,valor,frecuencia):
        if nodo.valor > valor:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(valor,frecuencia)
            else:
                self.insertar_aux(nodo.izquierda,valor,frecuencia)
        else:
            if nodo.derecha == None:
                nodo.derecha = Nodo(valor,frecuencia)
            else:
                self.insertar_aux(nodo.derecha,valor,frecuencia)

     def buscar_codigo(self,valor):
        return self.buscar_codigo_aux(self.raiz,valor,"")

    def buscar_codigo_aux(self,nodo,valor,codigo):
        if nodo == None:
            return ""
        elif nodo.valor == valor:
            return codigo
        elif nodo.valor > valor:
            return self.buscar_codigo_aux(nodo.izquierda,valor,codigo+"0")
        else:
            return self.buscar_codigo_aux(nodo.derecha,valor,codigo+"1")
        
    def comprimir(self,mensaje):
        codigo = ""
        for letra in mensaje:
            codigo += self.buscar_codigo(letra)
        self.codigo = codigo

    def descomprimir(self,codigo):
        mensaje = ""
        nodo = self.raiz
        for bit in codigo:
            if bit == "0":
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
            if nodo.izquierda == None and nodo.derecha == None:
                mensaje += nodo.valor
                nodo = self.raiz
        return mensaje
    
    def __str__(self):
        return self.codigo



if __name__=='__main__':
    arbol = Arbol()
    arbol.insertar('A',0.2)
    arbol.insertar('F',0.17)
    arbol.insertar('1',0.13)
    arbol.insertar('3',0.21)
    arbol.insertar('0',0.05)
    arbol.insertar('M',0.09)
    arbol.insertar('T',0.15)
    arbol.comprimir("A1F3M0T")