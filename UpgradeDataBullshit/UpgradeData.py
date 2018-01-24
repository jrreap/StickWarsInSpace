import pygame
import random

class UpgradeData():

    economy = False
    defense = False
    speed = False
    health = False
    damage = False

    @classmethod
    def EconomyUpgrade(cls, x):
        cls.economy = x
    @classmethod
    def DefenseUpgrade(cls, x):
        cls.defense = x
    @classmethod
    def HealthUpgrade(cls, x):
        cls.health = x
    @classmethod
    def DamageUpgrade(cls, x):
        cls.damage = x


        
    
        

    

    
