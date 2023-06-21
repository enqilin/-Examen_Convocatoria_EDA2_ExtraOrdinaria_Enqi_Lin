


import csv

class Armaduras:
    def __init__(self,nombre,rango):
        self.nombre = nombre
        self.rango = rango
        print('ha creado con exito')

    def clasificacion(self):
        self.codigo = None
        self.ciherente = None
        self.siglo = None
        self.armadura = None
        self.escuadra = None

    def __str__(self):
        return f'{self.nombre} tiene el range {self.rango}.'
    def to_dict(self):
        return {'nombre':{self.nombre},'rango':{self.rango},'codigo':{self.codigo},'ciherente':{self.ciherente},
        'siglo':{self.siglo},'armadura':{self.armadura},'escuadra':{self.escuadra}}


class Armadura:
    lista = []
    
    with open('arma.csv','r') as fichero:
        reader = csv.reader(fichero, delimiter = ';')
        for nombre, rango, codigo,ciherente,siglo,armadura,escuadra in reader:
            armadura = Armaduras(nombre,rango)
            armadura.clasificacion(codigo,ciherente,siglo,armadura,escuadra)
            lista.append(armadura)

    
    @staticmethod
    def buscar(nombre):
        for armadura in Armadura.lista:
            if armadura.nombre == nombre:
                return nombre

    @staticmethod
    def crear(nombre, rango, codigo,ciherente,siglo,armadura,escuadra):
        armadura = Armaduras(nombre,rango)
        armadura.clasificacion(codigo,ciherente,siglo,armadura,escuadra)
        Armadura.lista.append(armadura)
        Armadura.guardar()
        return armadura
    
    @staticmethod
    def guardar():
        with open('arma.csv','w', newline='\n') as fichero:
            writer = csv.writer(fichero,delimiter=';')
            for armadura in Armadura.lista:
                writer.writerow(armadura.to_dict.values())



if __name__=='__main__':
    arm = Armaduras('Jose', 9)
    arm.clasificacion('Mk',9,9,9,6)
    print(arm)