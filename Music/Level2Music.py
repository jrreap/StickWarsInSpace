import pygame

class Level2Music():

    def playmusic(self):
        file = './Music/level2playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
