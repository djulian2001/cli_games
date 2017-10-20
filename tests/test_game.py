import unittest
import copy
from random import shuffle


class Test_Unittest(unittest.TestCase):
  
  # Unittest general 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass
  def tearDown(self):
    """If there was a required clean up."""
    pass
  def test_assert(self):
    assert True
  def test_assertFalse(self):
    self.assertFalse(False)



if __name__=="__main__":
  unittest.main()
