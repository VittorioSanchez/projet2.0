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

import pygame, math, random, sys
from pygame.locals import *
from tkinter import *
from tkinter.messagebox import *



MAX_X = 780
MAX_Y = 580
MIN_X = 0
MIN_Y = 0

ALIENNUMBERS = 50

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.font = pygame.font.SysFont("arial", 30)
        self.image = pygame.image.load('Game_over.jpeg')
        #self.text = "GAME OVER!! press SPACE to exit"
        #self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        #self.rect.top = 100
        #self.rect.left = 25
        #input("Entrer votre pseudo: ")
    def update(self):
        self.font = pygame.font.SysFont("arial", 30)
        self.text = "GAME OVER!! press SPACE to exit"
        self.image2 = self.font.render(self.text,1,(0,255,0))
        self.rect2 = self.image.get_rect()
        self.rect2.top = 100
        self.rect2.left = 25


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init___(self)


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
        self.image = self.font.render(self.text, 1, (0, 0, 255))
        self.rect = self.image.get_rect()
        self.seconds = 0
        
    
    def update(self,lives,score,wave):
        self.munition = munitions
        if lives > 0:
            self.lives += 1
        elif score > 0:
            self.score += 1
        elif wave > 0:
            self.wave += 1
        milliseconds = time
        if milliseconds > 1000:
            global seconds
            self.seconds += 1
            milliseconds -= 1000
        self.points = (self.score)*10 + self.seconds            
        self.text = "SHIELD HITS: %d   MISSILE HITS: %d  WAVE NUMBER: %d MUNITIONS: %d SCORE: %d" % (self.lives, self.score, self.wave,self.munition, self.points)
        self.image = self.font.render(self.text, 1, (0, 0, 255))
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
#random.randrange(0,780)        
#random.randrange(1,5) random.randrange(1,5)

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
        self.image = pygame.image.load('power_up_ammo.png').convert_alpha()
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
        #self.swarm = pygame.mixer.Sound('swarm.wav')
        self.alerte = pygame.mixer.Sound('alerte.wav')
        self.bonus = pygame.mixer.Sound('power-up.wav')

    def playmissile(self):
        self.missile.play()
    def playexplosion(self):
        self.explosions.play()
    def playbasehit(self):
        self.basehit.play()
    #def playswarm(self):
     #   self.swarm.play()
    def playalerte(self):
        self.alerte.play()
    def playbonus(self):
        self.bonus.play()


def main():

    GAMEOVER = 0
    missileticks = 0
    global time
    global direction_tir
    global munitions
    time = 0
    time2 = 0
    time3 = 0
    spawn = 0
    spawn2 = 0
    seuil = 800
    seuil2 = 2000
    life = 3
    direction = 4
    direction_tir = 3 
    munitions = 100
    
    WINSIZE = [800,600]
    pygame.init()

    pygame.mixer.pre_init(44000, 16, 2, 4096)
    missile = pygame.mixer.Sound('missile.wav')
    explosion = pygame.mixer.Sound('explosion.wav')
    basehit = pygame.mixer.Sound('basehit.wav')
    alerte = pygame.mixer.Sound('alerte.wav')
    #swarm = pygame.mixer.Sound('swarm.wav')
    bonus = pygame.mixer.Sound('power-up.wav')
    pygame.mixer.music.load('space.wav')
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

    #swarm.play()

    pressed_keys = pygame.key.get_pressed()
    
    ennemis = pygame.sprite.RenderUpdates()
    ennemis.add(Ennemis())
    ennemis.add(Meteorite())
    
    
    while not GAMEOVER:
        
        time = pygame.time.get_ticks()
        
        if spawn==0:
            time2=time
            spawn=1
        delta=time-time2
        if spawn==1 and delta>seuil:
            ennemis.add(Ennemis())
            spawn=0
            seuil-= 5
            statusdisplay.update(0,0,1)
            #swarm.play()
            
        if spawn2==0:
            time3=time
            spawn2=1
        delta2=time-time3
        if spawn2==1 and delta2>seuil2:
            ennemis.add(Meteorite())
            spawn2=0
            seuil2-= 2
            statusdisplay.update(0,0,1)
            #swarm.play()
   
        if random.randrange(0,600) == 0:
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
            direction_tir = 0
        elif pressed_keys[K_DOWN]: 
            direction = 1
            direction_tir = 1
        elif pressed_keys[K_LEFT]: 
            direction = 2
            direction_tir = 2
        elif pressed_keys[K_RIGHT]: 
            direction = 3
            direction_tir = 3
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
        
        baseship.update(direction,life)
        missiles.update()     
        bonus_vie.update(time)               
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
        

        rectlistbaseship = baseship.draw(screen)
        rectlistmissiles = missiles.draw(screen)
        rectlistennemis = ennemis.draw(screen)
        rectlistexplosions = explosions.draw(screen)
        rectliststatusdisplay = statusdisplay.draw(screen)
        rectlistbonusvie = bonus_vie.draw(screen)
        
        pygame.display.update(rectlistbonusvie)
        pygame.display.update(rectlistbaseship)
        pygame.display.update(rectlistmissiles)
        pygame.display.update(rectlistennemis)
        pygame.display.update(rectlistexplosions)
        pygame.display.update(rectliststatusdisplay)
    
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
    pygame.quit()


if __name__ == '__main__': main()
