import pygame

class Level3Music():

    def playmusic(self):
        file = './Music/level3playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
