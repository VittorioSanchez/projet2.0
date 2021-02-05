#####################################################################
#
#Projet d'ISN:      XXXXXX
#
#Créateurs:         Bryan CURT, Florian VIE et Vittorio SANCHEZ
#
#Principe:          Shoot'em up, munitions et vies limitées, flèches
#                   directionnelles pour se déplacer, W pour tirer.
#
#####################################################################

import pygame, math, random, sys, bd
from pygame.locals import *


MAX_X = 780
MAX_Y = 580
MIN_X = 0
MIN_Y = 0

ALIENNUMBERS = 50

class Menu:
    liste = []
    champ = []
    taille_police = 32
    police = pygame.font.SysFont
    dest_surface = pygame.Surface
    ilosc_pol = 0
    couleur_fond = (51,51,51)
    couleur_text =  (255, 255, 153)
    select_couleur = (153,102,255)
    select_element = 0
    position = (0,0)
    menu_width = 0
    menu_height = 0

    class Champ:
        text = ''
        champ2 = pygame.Surface
        champ_rect = pygame.Rect
        select_rect = pygame.Rect

    def move_menu(self, top, left):
        self.position = (top,left) 

    def set_colors(self, text, selection, background):
        self.couleur_fond = background
        self.couleur_text =  text
        self.select_couleur = selection
        
    def set_fontsize(self,font_size):
        self.taille_police = font_size
        
    def get_position(self):
        return self.select_element
    
    def init(self, liste, dest_surface):
        self.liste = liste
        self.dest_surface = dest_surface
        self.ilosc_pol = len(self.liste)
        #self.structure()        
        
    def draw(self,przesun=0):
        if przesun:
            self.select_element += przesun 
            if self.select_element == -1:
                self.select_element = self.ilosc_pol - 1
            self.select_element %= self.ilosc_pol
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.couleur_fond)
        select_rect = self.champ[self.select_element].select_rect
        pygame.draw.rect(menu,self.select_couleur,select_rect)

        for i in range(self.ilosc_pol):
            menu.blit(self.champ[i].champ2,self.champ[i].champ_rect)
        self.dest_surface.blit(menu,self.position)
        return self.select_element

    def structure(self):
        decalage = 0
        self.menu_height = 0
        self.police = pygame.font.SysFont("arial", self.taille_police)
        for i in range(self.ilosc_pol):
            self.champ.append(self.Champ())
            self.champ[i].text = self.liste[i]
            self.champ[i].champ2 = self.police.render(self.champ[i].text, 1, self.couleur_text)

            self.champ[i].champ_rect = self.champ[i].champ2.get_rect()
            decalage = int(self.taille_police * 0.2)

            height = self.champ[i].champ_rect.height
            self.champ[i].champ_rect.left = decalage
            self.champ[i].champ_rect.top = decalage+(decalage*2+height)*i

            width = self.champ[i].champ_rect.width+decalage*2
            height = self.champ[i].champ_rect.height+decalage*2            
            left = self.champ[i].champ_rect.left-decalage
            top = self.champ[i].champ_rect.top-decalage

            self.champ[i].select_rect = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.position
        self.position = (x+mx, y+my)


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("arial", 30)
        self.image = pygame.image.load('Game_over.jpeg')
        self.text = "GAME OVER!! press SPACE to exit"
        #self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        #self.rect.top = 100
        #self.rect.left = 25
    def update(self):
        #self.font = pygame.font.SysFont("arial", 30)
        #self.text = "GAME OVER!! press SPACE to exit"
        self.image2 = self.font.render(self.text,1,(255,255,0))
        self.rect2 = self.image.get_rect()
        
        self.rect2.top = 100
        self.rect2.left = 25
        bd.Interface()



"""
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init___(self)
"""

class StatusDisplay(pygame.sprite.Sprite):
    """ this class is used to display the score etc at the top of the screen"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 0
        self.score = 0
        self.wave = 1
        self.points = 0
        self.munition = munitions
        self.font = pygame.font.SysFont("arial", 24)
        self.text = "SHIELD HITS: %d   MISSILE HITS: %d  WAVE NUMBER: %d MUNITIONS: %d SCORE %d" % (self.lives, self.score, self.wave, self.munition, self.points)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.seconds = 0
        
    
    def update(self,lives,score,wave):
        self.munition = munitions
        points = self.points
        if lives > 0:
            self.lives += 1
        elif score > 0:
            self.score += 1
        elif wave > 0:
            self.wave += 1
        milliseconds = time
        if milliseconds > 1000:
            #global seconds
            self.seconds += 1
            milliseconds -= 1000
        self.points = (self.score)*10 + self.seconds            
        self.text = "SHIELD HITS: %d   MISSILE HITS: %d  WAVE NUMBER: %d MUNITIONS: %d SCORE: %d" % (self.lives, self.score, self.wave,self.munition, self.points)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()


class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Meteor.png').convert_alpha()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topright = [780,random.randrange(0,MAX_Y)]
        self.direction = [random.randrange(-4,-1),random.randrange(-4,4)]
        self.movement_ticks = 0
        self.animation_ticks = 0

    def update(self,timer):
        if self.movement_ticks < timer:
            self.movment_ticks = timer
            if self.rect.left < MIN_X:
                self.kill()
            if self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]
            if time%10 == 0:
                self.image = pygame.transform.rotate(self.image,90)
            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]
            self.movement_ticks += 20
            

class Ennemis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animation = random.randrange(0,2)
        if self.animation == 0:
            self.image = pygame.image.load('vaisseau_rouge.png')
        else:
            self.image = pygame.image.load('vaisseau_gris.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [780,random.randrange(0,MAX_Y)]
        self.direction = [random.randrange(-4,-1),random.randrange(-4,4)]
        self.movement_ticks = 0
        
    def update(self,timer):
        if self.movement_ticks < timer:
            self.movment_ticks = timer
            if self.rect.left < MIN_X:
                self.kill()
            if self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]
            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]
            self.movement_ticks += 20


class BaseShip(pygame.sprite.Sprite):
    """ the BaseShip class """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('vaisseau_3_vies.png').convert_alpha()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 200]
        self.direction_ship = [0,0]

    def update(self,direction,life):
        if direction == 0 and self.rect.top > MIN_Y:  #UP
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies.png')
            self.rect.top -= 5
            
        elif direction == 1 and self.rect.bottom < MAX_Y:   #DOWN
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies.png')
            self.rect.bottom += 5

        elif direction == 2 and self.rect.left > MIN_X:   #LEFT
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies.png')
            self.rect.left -= 5
            
        elif direction == 3 and self.rect.left < MAX_X:   #RIGHT
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies.png')
            self.rect.right += 5          
        

class Missile(pygame.sprite.Sprite):
    """ the Missile class """
    def __init__(self, initialposition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('munition.png').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = initialposition

    def update(self):
        if self.rect.right < MAX_X:
            self.rect.right += 6
        else:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    """  Explosion class - the explosions on screen obviously """
    def __init__(self, initialposition):
        pygame.sprite.Sprite.__init__(self)
        self.imagearray=[]
        self.images = pygame.image.load('explosion.bmp').convert()
        self.images.set_colorkey((255,0,255))
        for i in range(0,240,60):
            self.imagearray.append(self.images.subsurface((i,0,60,60)))
        self.image = self.imagearray[0]
        self.rect = self.imagearray[0].get_rect()
        self.animation_ticks = 0
        self.animationcounter = 0
        self.rect.topleft = initialposition

    def update(self,timer):
        if self.animation_ticks < timer:
            self.animation_ticks = timer
            self.image = self.imagearray[self.animationcounter]
            self.animationcounter += 1
            if self.animationcounter > 3: self.kill()
            self.animation_ticks += 50
            
            
class BonusVie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animation = random.randrange(0,2)
        self.image = pygame.image.load('power_up_vie.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [780,random.randrange(0,MAX_Y)]
        self.direction = [random.randrange(-4,-1),random.randrange(-4,4)]
        self.movement_ticks = 0
        
    def update(self,timer):
        if self.movement_ticks < timer:
            self.movment_ticks = timer
            if self.rect.left < MIN_X:
                self.kill()
            if self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]
            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]
            self.movement_ticks += 20


class BonusMunition(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animation = random.randrange(0,2)
        self.image = pygame.image.load('power_up_ammo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [780,random.randrange(0,MAX_Y)]
        self.direction = [random.randrange(-4,-1),random.randrange(-4,4)]
        self.movement_ticks = 0
        
    def update(self,timer):
        if self.movement_ticks < timer:
            self.movment_ticks = timer
            if self.rect.left < MIN_X:
                self.kill()
            if self.rect.left > MAX_X:
                self.direction[0] = -self.direction[0]
            if self.rect.top < MIN_Y or self.rect.top > MAX_Y:
                self.direction[1] = -self.direction[1]
            self.rect.left = self.rect.left + self.direction[0]
            self.rect.top = self.rect.top + self.direction[1]
            self.movement_ticks += 20


class Sounds():
    """ play all the sounds in the game """
    def __init__(self):
        pygame.mixer.pre_init(44000, 16, 2, 4096)
        self.missile = pygame.mixer.Sound('missile.wav')
        self.explosion = pygame.mixer.Sound('explosion.wav')
        self.basehit = pygame.mixer.Sound('basehit.wav')
        self.alerte = pygame.mixer.Sound('alerte.wav')
        self.bonus = pygame.mixer.Sound('power-up.wav')

    def playmissile(self):
        self.missile.play()
    def playexplosion(self):
        self.explosions.play()
    def playbasehit(self):
        self.basehit.play()
    def playalerte(self):
        self.alerte.play()
    def playbonus(self):
        self.bonus.play()

"""
def menu():
    WINSIZE = [800,600]
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    background = pygame.image.load('background.jpg')
    screen.blit(background,(0,0))
    pygame.display.update()
    """

def game():
    GAMEOVER = 0
    missileticks = 0
    global time
    global direction_tir
    global munitions
    life = 3
    direction = 4
    munitions = 50
    delta = 50
    delta2 = 100
    points = 0
    
    WINSIZE = [800,600]
    pygame.init()

    pygame.mixer.pre_init(44000, 16, 2, 4096)
    missile = pygame.mixer.Sound('missile.wav')
    explosion = pygame.mixer.Sound('explosion.wav')
    basehit = pygame.mixer.Sound('basehit.wav')
    alerte = pygame.mixer.Sound('alerte.wav')
    bonus = pygame.mixer.Sound('power-up.wav')
    pygame.mixer.music.load('space.mp3')
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINSIZE)
    
    statusdisplay = pygame.sprite.RenderUpdates()
    statusdisplay.add(StatusDisplay())

    baseship = pygame.sprite.RenderUpdates()
    baseship.add(BaseShip())

    missiles = pygame.sprite.RenderUpdates()

    explosions = pygame.sprite.RenderUpdates()
    gameover = pygame.sprite.RenderUpdates()
    
    bonus_vie = pygame.sprite.RenderUpdates()
    bonus_ammo = pygame.sprite.RenderUpdates()

    background = pygame.image.load('background.jpg')
    screen.blit(background,(0,0))

    pygame.display.update()

    pressed_keys = pygame.key.get_pressed()
    
    ennemis = pygame.sprite.RenderUpdates()
    ennemis.add(Ennemis())
    ennemis.add(Meteorite())
    
    while not GAMEOVER:
        
        time = pygame.time.get_ticks()
        seuil = time % 900
        if seuil == 0:
            delta -= 1
            delta2 -= 1
        
        if random.randrange(0,delta) == 0:
            ennemis.add(Ennemis())
            statusdisplay.update(0,0,1)
            
        if random.randrange(0,delta2) == 0:
            ennemis.add(Meteorite())
            statusdisplay.update(0,0,1)            
   
        if random.randrange(0,700) == 0:
            bonus_vie.add(BonusVie())
            bonus.play()

        if random.randrange(0,700) == 0:
            bonus_ammo.add(BonusMunition())
            bonus.play()

        for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]: 
            direction = 0
        elif pressed_keys[K_DOWN]: 
            direction = 1
        elif pressed_keys[K_LEFT]: 
            direction = 2
        elif pressed_keys[K_RIGHT]: 
            direction = 3
        else: direction =4

        if pressed_keys[K_z]: fired = 1
        else: fired = 0

        if fired == 1 and time > missileticks and munitions > 0:
            missileticks = time + 100
            munitions -= 1
            a,b,c,d = rectlistbaseship[0]
            missiles.add(Missile((a+35,b+23)))
            missile.play()

        baseship.clear(screen,background)
        ennemis.clear(screen,background)
        missiles.clear(screen,background)
        explosions.clear(screen,background)
        statusdisplay.clear(screen,background)
        bonus_vie.clear(screen,background)
        bonus_ammo.clear(screen,background)
        
        baseship.update(direction,life)
        missiles.update()     
        bonus_vie.update(time)   
        bonus_ammo.update(time)            
        ennemis.update(time)
        explosions.update(time)

        for i in pygame.sprite.groupcollide(ennemis, missiles, True, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a-20,b-20)))
            statusdisplay.update(0,1,0)
            explosion.play()

        for i in pygame.sprite.groupcollide(baseship, ennemis, False, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a,b)))
            life -=1
            statusdisplay.update(1,0,0)
            if life == 1:
                alerte.play()
            basehit.play()
        
        for i in pygame.sprite.groupcollide(baseship, bonus_vie, False, True):
            if life < 3:
                life +=1
            statusdisplay.update(1,0,0) 
        
        for i in pygame.sprite.groupcollide(baseship, bonus_ammo, False, True):
            munitions +=25
            
        for i in pygame.sprite.groupcollide(bonus_vie, missiles, True, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a,b)))
        
        for i in pygame.sprite.groupcollide(bonus_ammo, missiles, True, True):
            a,b,c,d = i.rect
            explosions.add(Explosion((a,b)))

        rectlistbaseship = baseship.draw(screen)
        rectlistmissiles = missiles.draw(screen)
        rectlistennemis = ennemis.draw(screen)
        rectlistexplosions = explosions.draw(screen)
        rectliststatusdisplay = statusdisplay.draw(screen)
        rectlistbonusvie = bonus_vie.draw(screen)
        rectlistbonusammo = bonus_ammo.draw(screen)
        
        pygame.display.update(rectlistbonusvie)
        pygame.display.update(rectlistbaseship)
        pygame.display.update(rectlistmissiles)
        pygame.display.update(rectlistennemis)
        pygame.display.update(rectlistexplosions)
        pygame.display.update(rectliststatusdisplay)
        pygame.display.update(rectlistbonusammo)
    
        if life == 0:
            gameover.add(GameOver())
            rectgameover = gameover.draw(screen)
            pygame.display.update(rectgameover)
            gameover.update()
            pygame.mixer.music.stop()
            while not GAMEOVER:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and  event.key == K_SPACE:
                        GAMEOVER = 1
                        
        clock.tick(60)
    #pygame.quit()


def main():
    pygame.init()       
    surface = pygame.display.set_mode((800,600)) #0,6671875 and 0,(6) of HD resoultion
    menu = Menu()
    pygame.key.set_repeat(199,69)#(delay,interval)
    n = 0
    while True:
        pygame.font.init()
        surface.fill((51,51,51))
        menu.init(['Start','Options','Quit'], surface)
        if n == 0:
            menu.structure()
        menu.draw()
        pygame.display.update() 
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menu.draw(-1) #here is the Menu class function
                    if event.key == K_DOWN:
                        menu.draw(1) #here is the Menu class function
                    pygame.display.update()
                    if event.key == K_RETURN:
                        if menu.get_position() == 2:#here is the Menu class function
                            pygame.display.quit()
                            sys.exit()
                        if menu.get_position() == 0:
                            game()  
                            continuer = 0
                            n = 1
                elif event.type == QUIT:
                    pygame.display.quit()
                    sys.exit()
            pygame.time.wait(20)

if __name__ == '__main__': main()
