import pygame

class Level1Music():

    def playmusic(self):
        file = './Music/level1playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
