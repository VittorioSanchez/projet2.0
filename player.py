import ship

"""Class representing a player
"""

class Player(Ship):
    """Class representing a player
    """
    def __init__(self, max_life_pt: int = 3):
        self._max_life_pt = max_life_pt

        self._life_pt = max_life_pt

    def post_init(self):
        self._x = 0
        self._y = 0

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
