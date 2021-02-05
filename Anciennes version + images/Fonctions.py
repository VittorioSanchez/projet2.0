# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:25:10 2016

@author: Florian
"""
"""
Class GAMEOVER

"""
import pygame, math, random, sys

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
                self.image=pygame.image.load('vaisseau_2_vies_UP.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie_UP.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies_UP.png')
            self.rect.top -= 5
            direction_tir = 0
            
        elif direction == 1 and self.rect.bottom < MAX_Y:   #DOWN
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies_DOWN.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie_DOWN.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies_DOWN.png')
            self.rect.bottom += 5
            direction_tir=1
            
        elif direction == 2 and self.rect.left > MIN_X:   #LEFT
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies_LEFT.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie_LEFT.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies_LEFT.png')
            self.rect.left -= 5
            direction_tir = 2
            
        elif direction == 3 and self.rect.left < MAX_X:   #RIGHT
            if life == 2:
                self.image=pygame.image.load('vaisseau_2_vies.png')
            elif life == 1:
                self.image=pygame.image.load('vaisseau_1_vie.png')
            elif life == 3:
                self.image=pygame.image.load('vaisseau_3_vies.png')
            self.rect.right += 5
            direction_tir = 3

class Missile(pygame.sprite.Sprite):
    """ the Missile class """
    def __init__(self, initialposition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('munition.png').convert()
        self.image.set_colorkey((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = initialposition
        self.position = direction_tir
        if direction_tir == 0:
            self.position = 0
        elif direction_tir == 1:
            self.position = 1
        elif direction_tir == 2:
            self.position = 2
        elif direction_tir == 3:
            self.position = 3

    def update(self):
        if self.position == 0 and self.rect.top > MIN_Y:
            self.image = pygame.image.load('munition2.png')
            self.rect.top -= 6
        elif self.position == 1 and self.rect.bottom < MAX_Y:
            self.image = pygame.image.load('munition2.png')
            self.rect.bottom +=6
        elif self.position == 2 and self.rect.left > MIN_X:
            self.rect.left -=6
        elif self.position == 3 and self.rect.right < MAX_X:
            self.rect.right +=6
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
        self.image = pygame.image.load('power_up_ammo.jpg')
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
        self.swarm = pygame.mixer.Sound('swarm.wav')

    def playmissile(self):
        self.missile.play()
    def playexplosion(self):
        self.explosions.play()
    def playbasehit(self):
        self.basehit.play()
    def playswarm(self):
        self.swarm.play()

