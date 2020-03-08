class TestFixtures(unittest.TestCase):
  def test_1001(self):
      self.assertFalse(near_thousand(1001), "El 1001 NO debe pasar.")

  def test_900(self):
      self.assertTrue(near_thousand(900), "El 900 debe pasar.")

  def test_100(self):
      self.assertTrue(near_thousand(100), "El 100 debe pasar.")

  def test_50(self):
      self.assertFalse(near_thousand(50), "El 50 NO debe pasar.")

  def test_values(self):
    function = lambda x: x >= 100 and x <= 1000
    correct_values = [function(value) for value in range(0, 2000, 100)]
    tested_values = [near_thousand(value) for value in range(0, 2000, 100)]
    self.assertEqual(correct_values, tested_values)