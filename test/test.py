import unittest
import armaduras as ar
import pregunta3 as pr
import pregunta4 as p


class test(unittest.TestCase):
    def setUp(self):
        ar.Armadura.lista = [ar.Armaduras("MIcher",'9')]
        ar.Armadura.lista[0].clasificacion('MK-',8,8,8,8)

    
    def test_clasificacion(self):
        exite = ar.Armadura.buscar("Micher")
        no_exito = ar.Armadura.buscar("Amda")
        self.assertNotNone(exito)
        SELF.assertIsNone(no_exito)

    def test_mostrar(self):
        arm = pr.Armaduras('Micher','9')
        arm.clasificacion('MK-',4,4,2,5)
        self.assertEqual(arm,"Micher tiene el rango 9.")

    def 