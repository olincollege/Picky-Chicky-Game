'''
Board.py test file
'''

import pytest
import pygame
from board import *


@pytest.fixture(scope="module")
def test_chick():
    return Chick()


@pytest.fixture(scope="module")
def test_worm():
    return Worm()


@pytest.fixture(scope="module")
def test_spider():
    return Spider()


def test_chick_x_start_position(test_chick):
    '''
    Test that the chick starts at the right x coordinate
    '''
    assert test_chick.rect.centerx == 160


def test_chick_y_start_position(test_chick):
    '''
    Test that the chick starts at the correct y coordinate
    '''
    assert test_chick.rect.centery == 520


def test_worm_start_position(test_worm):
    '''
    Test that the worm starts at the top of the screen
    '''
    assert test_worm.rect.centery == 0


def test_spider_start_position(test_spider):
    '''
    Test that the spider starts at the top of the screen
    '''
    assert test_spider.rect.centery == 0
