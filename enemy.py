import ship

"""Class representing a player
"""

class Enemy(Ship):
    pass
    '''Direction dir;
    Constructeur par defaut
    Ennemi()
    {
      dir = GAUCHE;
      setPosX(20); //Vaisseau tout à gauche
      setPosY(rand()%15);//setPosY(terrain.gethauteur()/2); //Vaisseau au milieu de la hauteur du terrain
      pt_vie = 1;
    }
    Ennemi(const int &X, const int &Y, const Direction &direc, const int &vie)
    {
      posX = X;
      posY = Y;
      dir = direc;
      pt_vie = vie;
    }

    //Accesseurs
    Direction getDir() const;
    void setDir(const Direction );
    void setPosInit();'''