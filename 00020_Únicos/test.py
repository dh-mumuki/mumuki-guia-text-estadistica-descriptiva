class TestFixtures(unittest.TestCase):
  def test_unicos(self):
    self.assertEquals([1,2,3,4,5], [1,2,3,3,3,3,4,5])