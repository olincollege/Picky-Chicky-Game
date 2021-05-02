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
    SCREEN_HEIGHT = 700

    # Setting up fonts
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, BLACK)
    
    # Setting up background
    background = pygame.image.load("game_background.png")
    resize_background = pygame.transform.scale(background, (700, 700))    

    # Setting up white screen
    WHITE = (255, 255, 255)
    DISPLAYSURF = pygame.display.set_mode((600,700))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")