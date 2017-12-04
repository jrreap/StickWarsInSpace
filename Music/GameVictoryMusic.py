import pygame

class GameVictoryMusic():

    def playmusic(self):
        file = './Music/gamevictorymusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        
