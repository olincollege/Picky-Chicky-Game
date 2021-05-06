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

#Creating Sprites Groups
bad_food = pygame.sprite.Group()
bad_food.add(spider)
good_food = pygame.sprite.Group()
good_food.add(worm)

all_sprites = pygame.sprite.Group()
all_sprites.add(chick)
all_sprites.add(spider)
all_sprites.add(worm)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000) # every 1 sec increase speed

# Create a view instance 
view_board = SetupBoard()

def start_screen():
    '''
    Creates the start screen for the Picky Chicky Game. 
    If the enter key is pressed, the start screen would quit 
    and the main game would be run. 
    '''
    end_it=False
    while (end_it==False):
        view_board.DISPLAYSURF.blit(view_board.resize_start_screen, (-50,-75))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end_it = True
        pygame.display.flip()


def main():
    '''
    The main game loop for the Picky Chicky Game. 
    '''
    
    SPEED = 5
    SCORE = 0
    while True:
        # Cycles through all events occuring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.1      
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Display the Background 
        view_board.DISPLAYSURF.blit(view_board.resize_background, (0,-60))
        scores = view_board.font_small.render(str(SCORE), True, view_board.BLACK)
        view_board.DISPLAYSURF.blit(scores, (10,10))
    

        # Moves and Re-draws all Sprites
        for entity in all_sprites:
            view_board.DISPLAYSURF.blit(entity.image, entity.rect)
            SCORE = entity.move(SPEED, SCORE)

        # render a score to show for the Game over screen 
        scores_2 = view_board.font.render(str(SCORE), True, view_board.WHITE)

        #To be run if collision occurs between chicky and bad food (spiders)
        if pygame.sprite.spritecollideany(chick, bad_food):
            time.sleep(1)  
            view_board.DISPLAYSURF.blit(view_board.game_over_resize, (0,-40))
            view_board.DISPLAYSURF.blit(scores_2, (340,472))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(3)
            pygame.quit()
            sys.exit() 

        #To be run if collision occurs between chicky and good food (worms)
        if pygame.sprite.spritecollideany(chick, good_food):
            SCORE += 1 
            worm.rect.top = 0
            worm.rect.center = (random.randint(40, view_board.SCREEN_WIDTH - 40), 0)
            pygame.display.update()  

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    start_screen()     
    main()