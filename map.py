"""Class representing the map of the game
"""

import app_logger
import player
import enemy
import projectile

class Cell(Enum):
    """Class representing the cell enumeration

    Args:
        Enum (Class): Inherits from class enum
    """
    VIDE = 0
    MUR = 1

class Enemy(Ship):
    """Class representing the map of the game
    """
  
    _logger = app_logger.get_logger(__name__)

    def __init__(self, x: int = 0, y: int = 0, direction: direction: Direction = LEFT, life_pt: int = 1):
        #Enemy class constructor

        self._width = 0
        self._height = 0

        #self.power_up
        #int power_up,power_upX,power_upY;   #Variable for the use of power Up

        #Definition of the map
        self.map = list(Case())

        #Definition of elements that move on the map
        self.player = Player()
        self.enemies = list(Ennemy)
        self.projectiles = list(Projectile())
        self.enemy_projectiles = list(Projectile())

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

    



'''

class Terrain
{

  
    // Initialise le terrain
    bool Init();

    // Initialise le joueur
    void setPosPlayeurInit();

    /*
      Transforme les vagues d'ennemis defini
      sur le terrain comme de vrai ennemis
      (ajout dans la liste d'ennemis)
    */
    void transfo_vague_en_ennemi(const char *);

    void vague_predef(const int );          //Choix d'une des vagues d'ennemis predefinie
    void vague_predef_chiffre(const int );  //Vague aleatoire d'ennemis sans nombre max d'ennemis

    void vauge_aleatoire(const int & , const int & , const int & );

    //Recupere le numero de la vague actuelle et le renvoie sous forme de vague d'ennemi
    void num_vague(const int &);

    //Methode pour la gestion du power up sur le terrain
    void creation_power_up();
    void suppr_power_up();

    //Changement du terrain/map (position asteroides)
    void nouveauMap();'''
