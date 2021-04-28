import pygame, sys
from pygame.locals import *
import random, time
from Picky_Chicky_board import *
from Picky_Chicky_view import *

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()




#Setting up Sprites        
chick = Chick()
worm = Worm()

#Creating Sprites Groups
bad_food = pygame.sprite.Group()
bad_food.add(worm)
all_sprites = pygame.sprite.Group()
all_sprites.add(chick)
all_sprites.add(worm)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

view_board = SetupBoard()

#Game Loop



def main():
    while True:
        
        #Cycles through all events occuring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                view_board.SPEED += 0.5      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        view_board.DISPLAYSURF.blit(view_board.background, (0,0))

        scores = view_board.font_small.render(str(view_board.SCORE), True, view_board.BLACK)
        view_board.DISPLAYSURF.blit(scores, (10,10))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            view_board.DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        #To be run if collision occurs between chicky and bad food
        if pygame.sprite.spritecollideany(chick, bad_food):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(1)
                    
            view_board.DISPLAYSURF.fill(RED)
            view_board.DISPLAYSURF.blit(game_over, (30,250))
            
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
            
        pygame.display.update()
        FramePerSec.tick(FPS)
        
main()
