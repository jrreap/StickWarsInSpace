import pygame

class LevelDefeatMusic():

    def playmusic(self):
        file = './Music/leveldefeatmusic.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(1)
        
