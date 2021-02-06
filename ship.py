import projectile

"""Class representing a vessel (mother of player and enemy)
"""

class Ship:
    """Class representing a vessel (mother of player and enemy)
    """
    #//Peut accéder aux "private" de :
    #friend class Jeu;
    #friend class Terrain;

    def __init__(self, x: int = 0, y: int = 0):
        #Location
        self._x = x
        self._y = y
        
        #Hit box => TO MODIFY
        self._width = 0
        self._height = 0

        #Life point
        self._max_life_pt #Maximum life points the ship can have
        self._life_pt #Ship's remaining life

        #Attack
        self._attack_speed; #Rate of fire
        self._bullet #Type of projectile => class projectile

    def damage(damage: int = 0):
        """Inflict damage due to enemies or player

        Args:
            damage (int, optional): "Amount" of damage. Defaults to 0.
        """        
        self.life = self.life - damage

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

    @property
    def width(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._width is not None:
            return self._width

    @width.setter
    def width(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._width = value

    @width.deleter
    def width(self):
        """Attribute "destructor"
        """
        self._width = None
    
    @property
    def height(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._height is not None:
            return self._height

    @height.setter
    def height(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._height = value

    @height.deleter
    def height(self):
        """Attribute "destructor"
        """
        self._height = None

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

    @property
    def attack_speed(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._attack_speed is not None:
            return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._attack_speed = value

    @attack_speed.deleter
    def attack_speed(self):
        """Attribute "destructor"
        """
        self._attack_speed = None

    @property
    def bullet(self):
        """Attribute getter

        Returns:
            (Type of attribute): Value of attribute (Position, int...)
        """
        if self._bullet is not None:
            return self._bullet

    @bullet.setter
    def bullet(self, value):
        """Attribute setter

        Args:
            value (Type of attribute): Value of attribute (Position, int...)
        """
        self._bullet = value

    @bullet.deleter
    def bullet(self):
        """Attribute "destructor"
        """
        self._bullet = None
