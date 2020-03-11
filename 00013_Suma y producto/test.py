class TestFixtures(unittest.TestCase):
  def test_suma_distintos(self):
    self.assertEquals(suma_tres(1, 2, 3), 6)

  def test_suma_iguales(self):
    self.assertEquals(suma_tres(4, 4, 4), 36)

  def test_n_args(self):
    with self.assertRaises(TypeError):
      suma_tres()
      print("asd")
    with self.assertRaises(TypeError):
      suma_tres(1, 2, 3, 4)