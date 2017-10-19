# from abc import abc, ABCMeta, abstractmethod
from abc import ABC, ABCMeta, abstractmethod

class ABC_Card_Game( ABC ):
  __metaclass__ = ABCMeta

  def __init__(self):
    super().__init__()
  
  @abstractmethod
  def turn(self):
    pass

  @abstractmethod
  def deal_cards(self):
    pass

  @abstractmethod
  def win(self):
    pass
  
  @abstractmethod
  def status(self):
    pass
