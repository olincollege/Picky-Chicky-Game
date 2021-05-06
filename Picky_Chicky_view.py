import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

class SetupBoard():
    # Setting up colors
    BLUE  = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Setting up dimensions
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # Setting up fonts
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    
    # Setting up Start Screen 
    start_screen = pygame.image.load("start_screen.png")
    resize_start_screen = pygame.transform.scale(start_screen, (720, 700))    

    # Setting up background
    background = pygame.image.load("game_background.png")
    resize_background = pygame.transform.scale(background, (700, 700))    
    
    # Setting up Game over screen
    game_over = pygame.image.load("game_over.png")
    game_over_resize = pygame.transform.scale(game_over, (700, 700))    

    # Setting up Display Surface
    DISPLAYSURF = pygame.display.set_mode((600,700))
