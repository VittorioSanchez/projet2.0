"""Class representing a player
"""

import app_logger
import ship

class Player(Ship):
    """Class representing a player
    """

    _logger = app_logger.get_logger(__name__)

    def __init__(self, max_life_pt: int = 3):
        """Player class constructor

        Args:
            max_life_pt (int, optional): Maximum life points the player can have. Defaults to 3.
        """
        #self._position = Position(0, 0) (already initialize in mother class)
            
        self._max_life_pt = max_life_pt

        self._life_pt = max_life_pt

    '''@property
    def position(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._position is not None:
            return self._position

    @position.setter
    def position(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._position = value

    @position.deleter
    def position(self):
        """Attribute "destructor"
        """
        self._position = None
    '''
    @property
    def life_pt(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._life_pt is not None:
            return self._life_pt

    @life_pt.setter
    def life_pt(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._life_pt = value

    @life_pt.deleter
    def life_pt(self):
        """Attribute "destructor"
        """
        self._life_pt = None

    @property
    def max_life_pt(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._max_life_pt is not None:
            return self._max_life_pt

    @max_life_pt.setter
    def max_life_pt(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._max_life_pt = value

    @max_life_pt.deleter
    def max_life_pt(self):
        """Attribute "destructor"
        """
        self._max_life_pt = None
