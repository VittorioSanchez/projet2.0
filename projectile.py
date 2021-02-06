
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

class Projectile

    #friend class Jeu;
    def __init__(self,
    x: int = 0,
    y: int = 0,
    direction: Direction = RIGHT,
    bullet_type: Type_bullet = STANDARD,
    attack_pt: int = 1,
    p_speed: int = 0):
        #Location
        self._x = x
        self._y = y

        self._direction = direction

        self._bullet_type = bullet_type

        self._attack_pt = attack_pt

        self._projectile_speed = p_speed

    #TO DO : Add property