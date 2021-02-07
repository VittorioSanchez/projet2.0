"""Class representing a position in the map of the game
"""
import app_logger

class Position:
    """Class representing a position in the map of the game
    """

    _logger = app_logger.get_logger(__name__)

    def __init__(self, x: int = 0, y: int = 0):
        """Position class constructor

        Args:
            x (int): Coordinate along the x axis. Defaults to 0.
            y (int): Coordinate along the y axis. Defaults to 0.
        """
        
        self._x = int(x) #Coordinate along the x axis
        self._y = int(y) #Coordinate along the y axis

    @property
    def x(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._x is not None:
            return self._x

    @x.setter
    def x(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._x = value

    @x.deleter
    def x(self):
        """Attribute "destructor"
        """
        self._x = None
    
    @property
    def y(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._y is not None:
            return self._y

    @y.setter
    def y(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._y = value

    @y.deleter
    def y(self):
        """Attribute "destructor"
        """
        self._y = None

    def __str__(self):
        """User-friendly representation of Position

        Returns:
            string: User-friendly representation of Position
        """
        try:
            return f'({self._x},{self._y})'
        except:
            self._logger.error("Error during user-friendly Position display")

    def __repr__(self):
        """Formal representation of Position

        Returns:
            string: Formal representation of the Position
        """
        try:
            return f'Position(x={self._x}, y={self._y})'
        except:
            self._logger.error("Error during formal Position display")



    def __add__(self, other):
        """Operator overload + for Position

        Args:
            other (Position): The other Position to add

        Returns:
            Position: Sum of 2 Position
        """
        if not other.__class__ is Position:
            self._logger.error("Error: Argument is not a Position")
            return NotImplemented
        res = Position()
        res.x = self._x + other.x
        res.y = self._y + other.y
        return res
    
    def __sub__(self, other):
        """Operator overload - for Position

        Args:
            other (Position): The other Position to add

        Returns:
            Position: Subtraction of 2 Position
        """
        if not other.__class__ is Position:
            self._logger.error("Error: Argument is not a Position")
            return NotImplemented
        res = Position()
        res.x = self._x - other.x
        res.y = self._y - other.y
        return res
    
    def __eq__(self, other):
        """Operator overload == for Position

        Args:
            other (Position): The other Position to compare

        Returns:
            Position: Comparison of equality of 2 positions
        """
        if not other.__class__ is Position:
            self._logger.error("Error: Argument is not a Position")
            return NotImplemented
        if((self._x == other.x) and (self._y == other.y)):
            return True
        else:
            return False
