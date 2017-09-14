import pygame
import os
from UnitManagement.Unit import Unit
from ImageCache.ImageLoader import GetImage

pygame.init()
screen = pygame.display.set_mode((1200, 650))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

#Main entry point for the game
#DO NOT RENAME THE FILE OR ELSE PYTHON WILL NOT RUN IT

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        
        screen.blit(GetImage("./Images/background.jpg"), (0,0))
        
        pygame.display.set_caption("Mongolian Space Stick Wars XD Special Day One Edition")
        pygame.display.flip()
        
        #Make sure we stay at 60 frames per second
        clock.tick(60)