import sys
#from pygame.locals import *
import random
import time
import pygame

pygame.init()


class SetupBoard():
    '''
    Contains several key viewing attributes like colors,
    fonts, display surfaces.

    Attributes:
        BLACK: A tuple representing the RGB color code for black
        WHITE:  A tuple representing the RGB color code for white

        SCREEN_WIDTH: An integer representing the width of the screen
        SCREEN_HEIGHT: An integer representing the height of the screen

        font: A Pygame Font representing Verdana size 60
        font_small: A Pygame Font representing Verdana size 20

        start_screen: A Pygame Surface object representing the start screen
        resize_start_screen: The scaled version of the Pygame Surface
                            object representing the start screen

        background: A Pygame Surface object representing the background
        resize_background: The scaled version of the Pygame Surface
                             object representing the start screen

        game_over:  A Pygame Surface object representing the game over screen
        game_over_resize: The scaled version of the Pygame Surface
                             object representing the game over screen

        DISPLAYSURF: A Pygame Surface object representing the overall
                            display screen
    '''

    # Setting up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Setting up dimensions
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # Setting up fonts
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
    game_over_resize = pygame.transform.scale(game_over, (701, 701))

    # Setting up Display Surface
    DISPLAYSURF = pygame.display.set_mode((600, 625))


class PygameDraw():
    """
    A Pygame representation of the Picky Chicky Characters
    """

    def draw_all_characters(all_sprites, speed, score):
        '''
        Moves and Re-draws all Sprites

        Args:
            all_sprites: A Pygame Group object containing all the game
            characters that need to the be drawn
            speed: An integer representing the speed of the falling objects
            score: An integer representing the current score
        '''
        view_board = SetupBoard()

        for entity in all_sprites:
            view_board.DISPLAYSURF.blit(entity.image, entity.rect)
            score = entity.move(speed, score)
