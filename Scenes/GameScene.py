import pygame
from SceneBase import SceneBase
from ImageCache.ImageLoader import GetImage
from UI.Text import Text
import pygame

class GameScene(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)

        self.text = Text(225, 600, "GAME VIEW", bold=True, color=(45, 185, 255))

    def ProcessInput(self, events, pressed_keys):
        mousepos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Blah")

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(GetImage("./Images/background.jpg"), (0, 0))

        self.text.DrawCenter(screen)
