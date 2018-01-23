import pygame
import random

class UpgradeData():

    economy = False
    defense = False
    speed = False
    rage = False
    damage = False

    @classmethod
    def EconomyUpgrade(cls, x):
        cls.economy = x
    @classmethod
    def DefenseUpgrade(cls, x):
        cls.defense = x
    @classmethod
    def SpeedUpgrade(cls, x):
        cls.speed = x
    @classmethod
    def RageUpgrade(cls, x):
        cls.rage = x
    @classmethod
    def DamageUpgrade(cls, x):
        cls.damage = x


        
    
        

    

    
