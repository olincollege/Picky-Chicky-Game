import pygame, sys
from pygame.locals import *
import random, time
from Picky_Chicky_board import Spider, Chick, Worm
from Picky_Chicky_view import *

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Setting up Sprites        
chick = Chick()
spider = Spider()
worm = Worm()
spider2 = Spider()
worm2 = Worm()

#Creating Sprites Groups
bad_food = pygame.sprite.Group()
bad_food.add(spider)
bad_food.add(spider2)

good_food = pygame.sprite.Group()
good_food.add(worm)
good_food.add(worm2)

all_sprites = pygame.sprite.Group()
all_sprites.add(chick)
all_sprites.add(spider)
all_sprites.add(worm)
all_sprites.add(spider2)
all_sprites.add(worm2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


view_board = SetupBoard()

#Game Loop
def main():
    SPEED = 5
    SCORE = 0
    while True:
        #Cycles through all events occuring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.1      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        view_board.DISPLAYSURF.blit(view_board.resize_background, (0,0))
        scores = view_board.font_small.render(str(SCORE), True, view_board.BLACK)
        view_board.DISPLAYSURF.blit(scores, (10,10))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            view_board.DISPLAYSURF.blit(entity.image, entity.rect)
            SCORE = entity.move(SPEED, SCORE)

        #To be run if collision occurs between chicky and bad food (spiders)
        if pygame.sprite.spritecollideany(chick, bad_food):
            time.sleep(1)  
            view_board.DISPLAYSURF.fill(view_board.RED)
            view_board.DISPLAYSURF.blit(view_board.game_over, (30,250))
            view_board.DISPLAYSURF.blit(scores, (50,200))
           
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit() 

        #To be run if collision occurs between chicky and good food (worms)
        if pygame.sprite.spritecollideany(chick, good_food):
            SCORE += 1 
            worm.rect.top = 0
            worm.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 40), 0)
            worm2.rect.top = 0
            worm2.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 40), 0)     
            pygame.display.update()        
            
        pygame.display.update()
        FramePerSec.tick(FPS)
        
main()
