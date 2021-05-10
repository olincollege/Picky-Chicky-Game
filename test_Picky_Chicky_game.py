import pytest
import pygame
from Picky_Chicky_game import *

@pytest.fixture(scope="module")
def test_SetupBoard():
    return SetupBoard()


def test_screen_width(test_SetupBoard):
    '''
    Test that SetupBoard() returns the correct screen width
    '''
    assert test_SetupBoard.SCREEN_WIDTH == 600

def test_screen_height(test_SetupBoard):
    '''
    Test that SetupBoard() returns the correct screen height
    '''
    assert test_SetupBoard.SCREEN_HEIGHT == 600

def test_black_rgb(test_SetupBoard):
    '''
    Test that SetupBoard() returns the correct RBG color for black
    '''
    assert test_SetupBoard.BLACK == (0, 0, 0)

def test_white_rgb(test_SetupBoard):
    '''
    Test that SetupBoard() returns the correct RGB color for white
    '''
    assert test_SetupBoard.WHITE == (255, 255, 255)
