import pygame

class MenuMusic():

    def playmusic(self):
        file = './Music/menumusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
