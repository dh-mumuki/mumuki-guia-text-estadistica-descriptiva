class Test248(unittest.TestCase):
  def test_248(self):
    self.assertEquals(stop_248([2, 3, 4, 248]), [2, 4])
    self.assertEquals(stop_248([2, 3, 4, 248, 6, 8, 10]), [2, 4])
      
  def test_no_evens(self):
    self.assertEquals(stop_248([3, 5, 7]), [])
