import pygame
from Scenes.SceneBase import SceneBase
from Scenes.GameScene import GameScene
from ImageCache.ImageLoader import getImage

class SpaceMongolianLorePeter (SceneBase):

    def Update(self):
        pass

    def Render (self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/peterlore.jpg"), (0,0))

