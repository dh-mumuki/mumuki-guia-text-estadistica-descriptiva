class Test(unittest.TestCase):

  def test_description_example(self):
    ls = ["a", "s", "d", "f"]
    self.assertEqual(
      concat_string(ls),
      "asdf",
      "concat_string(['a', 's', 'd', 'f']) != 'asdf'"
    )

  def test_iterable(self):