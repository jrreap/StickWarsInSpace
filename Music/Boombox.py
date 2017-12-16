import pygame

class Boombox():

    def PlayMusic(self, path, repeat=-1):
        pygame.mixer.music.fadeout(1000)
        file = ('Music/'+path+'.mp3')

        pygame.mixer.music.load(file)
        pygame.mixer.music.play(repeat)

    def MusicStatus(self):
        return pygame.mixer.music.get_busy()
        
