'''
Picky Chicky Board Class
'''

import pygame
from pygame.locals import *
import random
import time
from Picky_Chicky_view import *

pygame.init()
view_board = SetupBoard()


class Chick(pygame.sprite.Sprite):
    '''
    Chick Character Class. Keeps track of the movements and positions
    of Chicky.
    '''
    def __init__(self):
        """
        Initializes Chicky's image, surface, and starting location
        within the game.
        """
        super().__init__()
        self.flipped = False
        self.image = pygame.image.load("chick.png")
        self.image = pygame.transform.scale(self.image, (180,180))
        self.surf = pygame.Surface((80, 120))
        self.rect = self.surf.get_rect(center = (160, 520))

    def move(self, speed, score):
        '''
        Chick move function.

        Args:
            speed: The current speed of movement
            Score: The current score of the game

        Returns:
            The current score of the game.
        '''

        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > -60:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < (view_board.SCREEN_WIDTH - 20):
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        return score

class Worm(pygame.sprite.Sprite):
    '''
    Worm Character Class. Keeps track of the movements and positions 
    of the worm.
    '''
    def __init__(self):
        """
        Initializes Wormy's image, surface, and starting location
        within the game.
        """
        super().__init__()
        self.image = pygame.image.load("worm.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.surf = pygame.Surface((8, 45))
        self.rect = self.surf.get_rect(center = (random.randint(40,view_board.SCREEN_WIDTH-40)
                                                 , 0))

    def move(self,speed, score):
        '''
        Worm move function. Moves the worm at current speed
        and when the worm hits the ground, places it at a random
        location on the top of the screen.

        Args:
            speed: Current speed of the falling objects
            score: Current score
        '''
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 700:
            self.rect.top = 0
            self.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 20), 0)
        return score

class Spider(pygame.sprite.Sprite):
    '''
    Spider Character Class. Keeps track of the movements and positions
    of the Spider.
    '''
    def __init__(self):
        """
        Initializes Spidey's image, surface, and starting location
        within the game.
        """
        super().__init__()
        self.image = pygame.image.load("spider.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.surf = pygame.Surface((25, 30))
        self.rect = self.surf.get_rect(center = (random.randint(40,view_board.SCREEN_WIDTH-40)
                                                 , 0))

    def move(self, speed, score):
        '''
        Spider move function. Moves the spider at current speed
        and when the spider hits the ground, places it at a random
        location on the top of the screen.

        Args:
            speed: Current speed of the falling objects
            score: Current score
        '''
        self.rect.move_ip(0,speed)
        if self.rect.bottom > 700:
            self.rect.top = 0
            self.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 20), 0)

        return score
