import pygame
import random

class LevelData():

    mars = False
    mercury = False
    saturn = False
    uranus = False
    neptune = False

    @classmethod
    def Mars(cls, x):
        cls.mars = x

    @classmethod
    def Saturn(cls, x):
        cls.saturn = x

    @classmethod
    def Neptune(cls, x):
        cls.neptune = x

    @classmethod
    def Uranus(cls, x):
        cls.uranus = x

    @classmethod
    def Mercury(cls, x):
        cls.mercury = x

