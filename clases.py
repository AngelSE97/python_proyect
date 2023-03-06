import clases2
import unittest

class Probar(unittest.TestCase):

    def _test_mayusculas(self):
        palabra = 'buen dia'
        resultados = clases2.texto(palabra)
        self.assertEqual(resultados, 'Buen Dia')


if __name__== '__main__':
    unittest.main()
