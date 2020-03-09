class TestPrimos(unittest.TestCase):
  def test_primos(self):
    self.assertTrue(primos(1))
    self.assertTrue(primos(2))
    self.assertTrue(primos(3))
    self.assertTrue(primos(5))
    self.assertTrue(primos(7))
    self.assertTrue(primos(11))
    self.assertTrue(primos(13))
    self.assertTrue(primos(17))
    self.assertTrue(primos(19))

  def test_no_primo(self):
    self.assertFalse(primos(4))
    self.assertFalse(primos(6))
    self.assertFalse(primos(8))
    self.assertFalse(primos(9))
    self.assertFalse(primos(10))
    self.assertFalse(primos(15))
