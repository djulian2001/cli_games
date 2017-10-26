import unittest

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

  def test_test_abc_interface(self):
    """Example of testing an abstract base class"""
    from app.abc_card_game import ABC_Card_Game
    from app.test_abc import Test_ABC
    
    with self.assertRaises( TypeError ):
      abstract = ABC_Card_Game()
    with self.assertRaises( TypeError ):
      tabs = Test_ABC()
