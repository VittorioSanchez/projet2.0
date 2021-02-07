"""Class representing a ennemy
"""

import app_logger
import ship

class Enemy(Ship):
  """Class representing a ennemy
  """
  
  _logger = app_logger.get_logger(__name__)

  def __init__(self, x: int = 0, y: int = 0, direction: direction: Direction = LEFT, life_pt: int = 1):
    """Enemy class constructor

    Args:
        x (int): Coordinate along the x axis. Defaults to 0.
        y (int): Coordinate along the y axis. Defaults to 0.
        direction (direction, optional): Direction of enemy movement. Defaults to LEFT.
        life_pt (int, optional): Number of enemy life points. Defaults to 1.
    """

    self._position = Positiion(x, y) #May be change the default starting position

    self._direction = direction

    self._life_pt = life_pt #Ship's remaining life
