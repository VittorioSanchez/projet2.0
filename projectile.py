"""Class representing a projectile / bullet in game
"""

import app_logger

class Direction(Enum):
    """Class representing the direction enumeration

    Args:
        Enum (Class): Inherits from class enum
    """    
    LEFT = 0
    DOWN = 1
    UP = 2
    RIGHT = 3

class Type_bullet(Enum):
    """Class representing the type of bullet enumeration

    Args:
        Enum (Class): Inherits from class enum
    """    
    STANDARD = 0
    STRONG = 1

class Projectile:
    """Class representing a projectile / bullet in game
    """
    _logger = app_logger.get_logger(__name__)
    #friend class Jeu;
    def __init__(self,
    x: int = 0,
    y: int = 0,
    direction: Direction = RIGHT,
    bullet_type: Type_bullet = STANDARD,
    attack_pt: int = 1,
    p_speed: int = 0):
        """Projectile class constructor

        Args:
            x (int, optional): Coordinate along the x axis. Defaults to 0.
            y (int, optional): Coordinate along the y axis. Defaults to 0.
            direction (Direction, optional): Direction of projectile movement. Defaults to RIGHT.
            bullet_type (Type_bullet, optional): Type of projectile (standard, strong, ...). Defaults to STANDARD.
            attack_pt (int, optional): Damage the projectile can inflict. Defaults to 1.
            p_speed (int, optional): Projectile speed. Defaults to 0.
        """    
        #Location
        self._position = Positiion(x, y)

        self._direction = direction

        self._bullet_type = bullet_type

        self._attack_pt = attack_pt

        self._projectile_speed = p_speed

    @property
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

    @property
    def direction(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._direction is not None:
            return self._direction

    @direction.setter
    def direction(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._direction = value

    @direction.deleter
    def direction(self):
        """Attribute "destructor"
        """
        self._direction = None

    @property
    def bullet_type(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._bullet_type is not None:
            return self._bullet_type

    @bullet_type.setter
    def bullet_type(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._bullet_type = value

    @bullet_type.deleter
    def bullet_type(self):
        """Attribute "destructor"
        """
        self._bullet_type = None

    @property
    def attack_pt(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._attack_pt is not None:
            return self._attack_pt

    @attack_pt.setter
    def attack_pt(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._attack_pt = value

    @attack_pt.deleter
    def attack_pt(self):
        """Attribute "destructor"
        """
        self._attack_pt = None

    @property
    def projectile_speed(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._projectile_speed is not None:
            return self._projectile_speed

    @projectile_speed.setter
    def projectile_speed(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._projectile_speed = value

    @projectile_speed.deleter
    def projectile_speed(self):
        """Attribute "destructor"
        """
        self._projectile_speed = None
