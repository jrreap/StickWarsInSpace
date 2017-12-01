import pygame

class Level5Music():

    def playmusic(self):
        file = './Music/level5playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
