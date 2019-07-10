class TestFixtures(unittest.TestCase):
  def test_primos(self):
    self.assertTrue(primos(7))
  def test_no_primo(self):
    self.assertFalse(primos(9))
    