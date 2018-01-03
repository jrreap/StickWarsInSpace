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
            self.frame += width
            if self.frame >= width*(numframes):
                self.frame = 0
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
    def prevFrame(self):
        if self.wait == 0:
            self.frame -= width
            if self.frame <= 0:
                self.frame = width*(numframes-1)
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
