class TestFixtures(unittest.TestCase):
  def test_1000(self):
      self.assertFalse(near_thousand(1001))
  def test_900(self):
      self.assertTrue(near_thousand(900))

  def test_800(self):
      self.assertTrue(near_thousand(800))