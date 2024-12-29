# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
#module imports
from constants import *
from player import Player

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                #quit()
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        #final steps
        pygame.display.flip()
        dt = gameClock.tick(60)/1000


    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
