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

import pygame, math, random, sys, Fonctions
from pygame.locals import *


MAX_X = 780
MAX_Y = 580
MIN_X = 0
MIN_Y = 0

ALIENNUMBERS = 50

Fonctions.GameOver()

Fonctions.Menu()

Fonctions.StatusDisplay()

Fonctions.Meteorite()

Fonctions.Ennemis()
            
Fonctions.BaseShip()

Fonctions.Missile()

Fonctions.Explosion()
            
Fonctions.BonusVie()

Fonctions.BonusMunition()

Fonctions.Sounds()


def main():

    GAMEOVER = 0
    missile_missed = 0
    missile_hits = 0
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
    seuil_vie = 2000
    seuil_ammo = 10000
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
    swarm = pygame.mixer.Sound('swarm.wav')

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

    background = pygame.image.load('background.jpg')
    screen.blit(background,(0,0))


    pygame.display.update()

    swarm.play()

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
            seuil-= 1
            statusdisplay.update(0,0,1)
            swarm.play()
            
        if spawn2==0:
            time3=time
            spawn2=1
        delta2=time-time3
        if spawn2==1 and delta2>seuil2:
            ennemis.add(Meteorite())
            spawn2=0
            seuil2-= 1
            statusdisplay.update(0,0,1)
            swarm.play()
   
        if random.randrange(0,500) == 0:
            bonus_vie.add(BonusVie())


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
            explosions.add(Explosion((a-20,b-20)))
            life -=1
            statusdisplay.update(1,0,0)
            basehit.play()
        
        for i in pygame.sprite.groupcollide(baseship, bonus_vie, False, True):
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
            while not GAMEOVER:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and  event.key == K_SPACE:
                        GAMEOVER = 1
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__': main()
