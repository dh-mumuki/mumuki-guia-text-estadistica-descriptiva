class TestFixtures(unittest.TestCase):
   def test_248(self):
      self.assertEquals(stop_248([2, 3, 4, 248]), [2, 4])