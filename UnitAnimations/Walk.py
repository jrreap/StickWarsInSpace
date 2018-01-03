import pygame, sys
import os

class Walk():
    def __init__(self,w,nf):
        self.wait = 0
        self.frame = 0
        self.width = w
        self.numframes = nf
    def nextFrame(self):
        if self.wait == 0:
            self.frame += self.width
            if self.frame >= self.width*(self.numframes):
                self.frame = 0
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
    def prevFrame(self):
        if self.wait == 0:
            self.frame -= self.width
            if self.frame <= 0:
                self.frame = self.width*(self.numframes-1)
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
