class TestRepetidos(unittest.TestCase):
   def test_repetidos(self):
      self.assertTrue(repetidos([1, 1, 2]))
      self.assertTrue(repetidos([1, 2, 3, 4, 2]), "repetidos([1, 2, 3, 4, 2]) != True")

    def test_nonrep(self):
      self.assertFalse(repetidos([1, 2, 3]), "repetidos([1, 2, 3]) != False")