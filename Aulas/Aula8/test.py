import unittest

def soma(a,b):
    return a + b

def div(a,b):
    if b ==0:
        return "Não é possivel dividir por zero"
    
    return a/b

class TestSoma(unittest.TestCase):

    def testsomaValores(self):
        result = soma(1,2)
        self.assertEqual(result, 3)

    def testDivCerto(self):
        result = div(1,2)
        self.assertEqual(result, 0.5)

    def testDivCerto(self):
        result = div(1,0)
        err= "Não é possivel dividir por zero"
        self.assertEqual(result, err)
    


unittest.main()