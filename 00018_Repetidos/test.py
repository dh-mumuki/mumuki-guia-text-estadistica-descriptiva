class TestFixtures(unittest.TestCase):
   def test_repetidos(self):
      self.assertEquals(repetidos([1,1, 2]), True)