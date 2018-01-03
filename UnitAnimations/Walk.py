import pygame, sys
import os

class Walk():
    def __init__(self):
        self.wait = 0
        self.frame = 0
    def nextFrame(self):
        if self.wait == 0:
<<<<<<< HEAD
            self.frame += self.width
            if self.frame >= self.width*(self.numframes):
=======
            self.frame += 90
            if self.frame >= 90*7:
>>>>>>> 2411354fe0f543767192c8452e7f15a394ceb793
                self.frame = 0
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
    def prevFrame(self):
        if self.wait == 0:
<<<<<<< HEAD
            self.frame -= self.width
            if self.frame <= 0:
                self.frame = self.width*(self.numframes-1)
=======
            self.frame -= 90
            if self.frame <= 0:
                self.frame = 90*6
>>>>>>> 2411354fe0f543767192c8452e7f15a394ceb793
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
