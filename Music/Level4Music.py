import pygame

class Level4Music():

    def playmusic(self):
        file = './Music/level4playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
