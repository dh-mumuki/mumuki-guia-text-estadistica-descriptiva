class Test(unittest.TestCase):

  def test_description_example(self):
    ls = ["a", "s", "d", "f"]
    self.assertEqual(concat_string(ls), "asdf")
