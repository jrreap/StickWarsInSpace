import pygame, sys
import os

class Walk():
    def __init__(self):
        self.wait = 0
        self.frame = 0
    def nextFrame(self):
        if self.wait == 0:
            self.frame += 90
            if self.frame >= 90*7:
                self.frame = 0
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
    def prevFrame(self):
        if self.wait == 0:
            self.frame -= 90
            if self.frame <= 0:
                self.frame = 90*6
        self.wait += 1
        if self.wait == 4:
            self.wait = 0
