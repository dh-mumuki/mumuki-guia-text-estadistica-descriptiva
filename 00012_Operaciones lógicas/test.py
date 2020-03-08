class TestFixtures(unittest.TestCase):
  def test_1000(self):
      self.assertFalse(near_thousand(1001))

  def test_900(self):
      self.assertTrue(near_thousand(900))

  def test_800(self):
      self.assertTrue(near_thousand(800))

  def test_values(self):
    function = lambda x: x >= 100 and x <= 1000
    correct_values = [function(value) for value in range(0, 2000, 100)]
    tested_values = [near_thousand(value) for value in range(0, 2000, 100)]
    self.assertEqual(correct_values, tested_values)