import pygame

class Level6Music():

    def playmusic(self):
        file = './Music/level6playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
