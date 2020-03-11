class TestFixtures(unittest.TestCase):
  def test_unicos(self):
    self.assertEquals(unicos([1,2,3,3,3,3,4,5]), [1,2,3,4,5])
  
  def test_len(self):
    lista = list(range(5)) * 2
    self.assertEquals(len(unicos(lista)), 5)

  def test_disorder(self):
    self.assertEquals(lista_de_unicos([1, 3, 3, 3, 3, 2, 4, 5]), [1, 3, 2, 4, 5])
