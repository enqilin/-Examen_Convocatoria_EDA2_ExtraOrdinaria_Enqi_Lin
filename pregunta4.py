
import csv

class Artefactovaliosos:
    def __init__(self,peso,nombre,precio,fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print('Ha creado con exito')

    def __str__(self):
        return f'{self.nombre} pesa {self.peso}'

    def to_dict(self):
        return {'nombre':{self.nombre},'peso':{self.peso},'precio':{self.precio},'fecha':{self.fecha}}

class Artefactovalioso:
    lista = []

    with open('artefactos.csv','r') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for nombre , peso, precio,fecha in reader:
            arte = Artefactovaliosos(nombre , peso, precio,fecha)
            lista.append(arte)


    @staticmethod
    def buscar():
        for arte in Artefactovalioso.lista:
            factor = sorted(arte.fecha)
        return factor

    @staticmethod
    def crear(nombre , peso, precio,fecha):
        arte =  Artefactovaliosos(nombre , peso, precio,fecha)
        Artefactovalioso.lista.append(arte)
        return arte
    @staticmethod
    def modificar(nombre , peso, precio,fecha):
        for indice, arte in enumerate(Artefactovalioso.lista):
            a = input("Modificar")
    




