import unittest
import math
import calculadoracomple

'PRUEBAS DE UNIDAD'
#Nota:Las pruebas de unidad permiten verificar que los resultados obtenidos sean los resultados reales.
class unit_calculadoracomple(unittest.TestCase):
    
    '------------------------Operaciones Básicas--------------------------'
    
    #Prueba para la suma.
    def test_suma(self):
        self.assertEqual(calculadoracomple.suma((3, 1), (2, 1)), [5,2])

    #Prueba para la resta.
    def test_res(self):
        self.assertEqual(calculadoracomple.res((5, 4), (4, -2)),[1, 6])

    #Prueba para la multiplicación.
    def test_multi(self):
        self.assertEqual(calculadoracomple.multi((-3, -1), (1, -2)),[-5, 5])

    #Prueba para la división.
    def test_div(self):
        self.assertEqual(calculadoracomple.div((-2, 1), (1, 2)),[0, 1])

    #Prueba para el conjugado.
        self.assertEqual(calculadoracomple.conju((-2,1)),[-2,-1])

    #Prueba para el módulo.    
    def test_modu(self):
        self.assertEqual(calculadoracomple.modu((4,-3)),5)
        
    #Prueba para la conversión de representación polar a cartesiana.
    def test_pol_carte(self):
        self.assertEqual(calculadoracomple.pol_carte((3, 1.0471975511965)), [1.500000000000254, 2.5980762113531695])

    #Prueba para la conversión de representación cartesiana a polar.
    def test_carte_pol(self):
        self.assertEqual(calculadoracomple.carte_pol((1, -1)), [1.4142135623730951, -0.7853981633974483])

    #Prueba para la fase.
    def test_fase(self):
        self.assertEqual(calculadoracomple.fase((3,2)),(33.690067525979785))
        self.assertEqual(calculadoracomple.fase((-3,2)),(146.30993247402023))
        
    '-------------------------------Vectores----------------------------------'
    
    #Prueba para la suma de vectores.
    def test_adicionvectores(self):
        self.assertEqual(calculadoracomple.adicionvectores([[8,3],[-1,-4],[0,-9]],[[8,-3],[2,5],[3,0]]),[[16,0],[1,1],[3,-9]])

    #Prueba para el inverso aditivo de un vector.
    def test_inversovector(self):
        self.assertEqual(calculadoracomple.inversovector([[-5,2],[3,0],[0,-1]]),[[5,-2],[-3,0],[0,1]])

    #Prueba para la multiplicación escalar de un vector.
    def test_multiescalarvector(self):
        self.assertEqual(calculadoracomple.multiescalarvector([-1,1],[[-2,5],[-1,-1],[2,-9]]),[[-3,-7],[2,0],[7,11]])

    #Prueba para el producto interno de vectores.
    def test_productointerno(self):
        self.assertEqual(calculadoracomple.productointerno([[2,-1],[-8,-5],[-2,-6]],[[6,-3],[5,-1],[-6,-2]]),[4,1])

    #Prueba para la norma de vectores.
    def test_normavector(self):
        self.assertEqual(calculadoracomple.normavector([[4,5],[3,1],[0,-7]]),10)

    #Prueba para la distancia entre vectores.
    def test_distanciaVector(self):
         self.assertEqual(calculadoracomple.distanciaVector([(2,7),(4,-1),(2,-4)],[(7,8),(2,-8),(1,4)]),12)
         self.assertEqual(calculadoracomple.distanciaVector([(9,-7),(-1,-6)],[(7,-8),(5,-9)]),7.0710678118654755)

    '---------------------------------Matrices---------------------------------'

    #Prueba para la suma de matrices.
    def test_adicionmatriz(self):
        self.assertEqual(calculadoracomple.adicionmatriz([[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]],[[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]]),[[[-15,-5],[-10,-6],[7,3]],[[4,17],[6,-7],[14,-10]],[[5,5],[2,-1],[-2,-1]]])

    #Prueba para el inverso aditivo de una matriz.
    def test_inversomatriz(self):
        self.assertEqual(calculadoracomple.inversomatriz([[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]),[[[-7,-3],[1,-7]],[[9,4],[7,9]]])

    #Prueba para la multiplicación escalar de una matriz.  
    def test_multiescalarmatriz(self):
        self.assertEqual(calculadoracomple.multiescalarmatriz([-2,3],[[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]),[[[0,13],[-4,32]],[[22,32],[28,10]]])

    #Prueba para la transpuesta de una matriz.
    def test_matriztranspuesta(self):
        self.assertEqual(calculadoracomple.matriztranspuesta([[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]]),[[[5,9],[8,2]],[[-7,-5],[-3,-7]],[[-1,-4],[7,-8]]])

    #Prueba para la matriz conjugada.
    def test_matrizconjugada(self):
        self.assertEqual(calculadoracomple.matrizconjugada([[[-6,1],[3,8]],[[2,-6],[3,0]]]),[[[-6,-1],[3,-8]],[[2,6],[3,0]]])

    #Prueba para la adjunta o daga de una matriz.
    def test_matrizadjunta(self):
        self.assertEqual(calculadoracomple.matrizadjunta([[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]),[[[7,-7],[5,0]],[[3,-8],[8,6]],[[8,-4],[-10,1]]])

    #Prueba para la multiplicación de matrices.
    def test_multimatriz(self):
        self.assertEqual(calculadoracomple.multimatriz([[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]],[[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]),[[[-33,153],[120,0],[-44,-22]],[[87,0],[-26,-117],[107,70]],[[0,165],[147,26],[69,-36]]])
        self.assertEqual(calculadoracomple.multimatriz([[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]],[[[0,-1],[1,0]],[[0,0],[0,1]]]),'Error. Las matrices no tienen dimensiones compatibles')
        self.assertEqual(calculadoracomple.multimatriz([[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]],[[[1,-3]],[[4,3]],[[-3,1]]]),[[[54,-32]],[[0,17]],[[41,30]]])

    #Prueba para la matriz unitaria.
    def test_matrizunitaria(self):
        self.assertEqual(calculadoracomple.matrizunitaria([[[1/(2)**(1/2),0],[0,1/(2)**(1/2)]],[[0,1/(2)**(1/2)],[1/(2)**(1/2),0]]]),'Es unitaria')
        self.assertEqual(calculadoracomple.matrizunitaria([[[0,1],[1,0],[0,0]],[[0,0],[0,1],[1,0]],[[1,0],[0,0],[0,1]]]),'No es unitaria')

    #Prueba para la matriz hermitiana.
    def test_matrizhermitana(self):
        self.assertEqual(calculadoracomple.matrizhermitaña([[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]]),'Es hermitaña')
        self.assertEqual(calculadoracomple.matrizhermitaña([[[1,0],[3,-1]],[[3,1],[0,1]]]),'No es hermitaña')
        
    #Prueba para el producto tensor.
    def test_productotensor(self):
        self.assertEqual(calculadoracomple.productotensor([[(1,1),(0,0)],[(1,0),(0,1)]],[[(-1,2),(-2,-2),(0,2)],[(2,3),(3,1),(2,2)],[(-2,1),(1,-1),(2,1)]]),
                         [[[-3,1],[0,-4],[-2,2],[0,0],[0,0],[0,0]],[[-1,5],[2,4],[0,4],[0,0],[0,0],[0,0]],[[-3,-1],[2,0],[1,3],[0,0],[0,0],[0,0]],[[-1,2],[-2,-2],[0,2],[-2,-1],[2,-2],[-2,0]],
                          [[2,3],[3,1],[2,2],[-3,2],[-1,3],[-2, 2]],[[-2,1],[1,-1],[2,1],[-1,-2],[1,1],[-1,2]]])
    
if True:
    unittest.main()

