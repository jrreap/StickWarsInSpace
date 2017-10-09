import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import GetImage


class Level4Defeat (SceneBase):

    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
            
        screen.blit(GetImage("./Images/level4defeat.jpg"), (0,0))

      
