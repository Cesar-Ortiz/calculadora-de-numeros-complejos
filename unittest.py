import unittest
import calculadoracomple

class unit_calculadoracomple(unittest.TestCase):
  
  def test_suma(self):
    self.asserEqual(calculadoracomple.suma((3,1),(2,1)),(5,3))

  def test_resta(self):
    self.asserEqual(calculadoracomple.resta((5,4),(4,-2)),(1,6))

  def test_multi(self):
    self.asserEqual(calculadoracomple.multi((-3,-1),(1,-2)),(-5,5))

  def test_div(self):
    self.asserEqual(calculadoracomple.div((-2,1),(1,2)),(0,1))

  def test_modu(self):
    self.asserEqual(calculadoracomple.modu((4,-3),5))

  def test_pol_carte(self):
    self.asserEqual(calculadoracomple.pol_carte((3,1.0471975511965)),(1.500000000000254, 2.5980762113531695))

  def test_carte_pol(self):
    self.asserEqual(calculadoracomple.carte_pol((1,-1)),(1.4142135623730951, -0.7853981633974483))


if True:
  unittest.main()
