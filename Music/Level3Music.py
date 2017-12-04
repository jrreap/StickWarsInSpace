import pygame

<<<<<<< HEAD:Music/GameEndMusic.py
class Boombox():
    def playmusic(self,path,repeat = -1):
        pygame.mixer.music.stop()
        file = ('Music/'+path+'.mp3')
=======
class Level3Music():

    def playmusic(self):
        file = './Music/level3playmusic.mp3'
        pygame.init()
        pygame.mixer.init()
>>>>>>> 45cc8f52dba3a06e974536be57510162dbafccd6:Music/Level3Music.py
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(repeat)
