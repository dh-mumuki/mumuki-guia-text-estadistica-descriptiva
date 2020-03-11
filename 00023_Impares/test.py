import inspect

class TestImpares(unittest.TestCase):

  def test_description_example(self):
    self.assertEqual(impares(21), [1,3,5,7,9,11,13,15,17,19])
    self.assertEqual(impares(18), [1,3,5,7,9,11,13,15,17])
    
  def test_listcomp(self):
    self.assertRegex(inspect.getsource(impares), r"\[.*for.*in.*\]")