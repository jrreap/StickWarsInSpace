import pygame
import os
from Scenes.MenuScene import MenuScene


#MAIN METHOD
def Start(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    done = False
    x = 30
    y = 30
    
    clock = pygame.time.Clock()
    
    active_scene = starting_scene
    
    #Main entry point for the game
    #DO NOT RENAME THE FILE OR ELSE PYTHON WILL NOT RUN IT
    
    while active_scene != None:
            pressed_keys = pygame.key.get_pressed()
            
            filtered_events = []
            for event in pygame.event.get():
                quit_attempt = False
                
                #Check if the input is a EXIT command or key
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:
                    alt_pressed = pressed_keys[pygame.K_LALT]
                    if event.key == pygame.K_ESCAPE:
                        quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True                            
                
                #Check if we are quitting
                if quit_attempt:
                    active_scene.Terminate()
                else:
                    filtered_events.append(event)
                    
            active_scene.ProcessInput(filtered_events, pressed_keys)
            active_scene.Update()
            active_scene.Render(screen)
            
            #Change the scene if the scene has changed
            active_scene = active_scene.next
            
            pygame.display.set_caption("Mongolian Space Stick Wars XD Special Day One Edition")
            pygame.display.flip()
            clock.tick(fps)
  
#Start the game
Start(1200, 650, 60, MenuScene())
                   