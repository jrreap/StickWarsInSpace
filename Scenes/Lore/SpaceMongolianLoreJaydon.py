import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import getImage

class SpaceMongolianLoreJaydon (SceneBase):

    def Update(self):
        pass

    def Render (self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/jaydonlore.jpg"), (0,0))
