import pygame

class GameEndMusic():

    def playmusic(self):
        file = './Music/gameendmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
