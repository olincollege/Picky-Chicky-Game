import pygame, sys
from pygame.locals import *
import random, time
from Picky_Chicky_view import *
#from Picky_Chicky_game import *


pygame.init()

view_board = SetupBoard()

class Spider(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("spider.png")
        self.image = pygame.transform.scale(self.image, (200, 200)) 
        self.surf = pygame.Surface((25, 50))
        self.rect = self.surf.get_rect(center = (random.randint(40,view_board.SCREEN_WIDTH-40)
                                                 , 0))

      def move(self,SPEED, SCORE):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 40), 0)
        return SCORE
        

class Worm(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("worm.png")
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.surf = pygame.Surface((42, 45))
        self.rect = self.surf.get_rect(center = (random.randint(40,view_board.SCREEN_WIDTH-40)
                                                 , 0))

      def move(self,SPEED, SCORE):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 40), 0)
        return SCORE


class Chick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("chick.png")
        self.image = pygame.transform.scale(self.image, (180,180)) 
        self.surf = pygame.Surface((90, 120))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self, SPEED, SCORE):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < view_board.SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)   
        return SCORE
                  
