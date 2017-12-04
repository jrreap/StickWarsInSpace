import pygame

class Boombox():

    @classmethod
    def playmusic(self,path,repeat = -1):
        pygame.mixer.music.stop()
        file = ('Music/'+path+'.mp3')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(repeat)
        
