import pygame

class LevelVictoryMusic():

    def playmusic(self):
        file = './Music/levelvictorymusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(1)
        
