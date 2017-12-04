from UnitManagement import*
from UnitManagement.UnitLoader import UnitLoader
from UnitManagement.UnitSpawner import UnitSpawner
from CurrencyManagement.CurrencyManagement import CurrencyManagement
import pygame

##SOME KINKS NEED TO WORKED OUT. I (Addison) WILL DO IT SOON SO PLS DONT FUCK TOO MUCH UP
class AttackDefend():
    @classmethod
    def InRange(cls, Unit1, Unit2):
        detect = False
        UnitRange = Unit1.unitrange
        if abs(Unit2.xpos-Unit1.xpos)<=UnitRange*10:
            detect = True
        else:
            detect = False
        return detect

    @classmethod
    def Attack(cls, Friendlies, Enemies, AttackRate):
        x = 0
        y = 0
        Rate = AttackRate
        while(x<len(Friendlies)):
              Unit1 = Friendlies[x]
              x = x+1
              y = 0
              while(y<len(Enemies)):
                  Unit2 = Enemies[y]
                  y = y+1
                  detected = AttackDefend.InRange(Unit1,Unit2)
                  if(Unit2.health>0):
                      if(detected == True):
                          Unit1.speed = 0
                          if(Rate == 30):
                              Unit1.speed = 0
                              print Unit2.health
                              Unit2.DamageUnit(Unit1.damage)                         
                              print Unit2.health
                              if Unit2.health<1:
                                  UnitSpawner.DeleteUnit(Unit2)
                                  CurrencyManagement.AddMoonCrystals(100)
                                  Unit1.speed = 2
                      if(Unit2.health<1):
                          Unit1.speed = 2

    @classmethod
    def EAttack(cls, Enemies, Friendlies, EAttackRate):
        x = 0
        y = 0
        ERate = EAttackRate
        while(x<len(Enemies)):
              Unit1 = Enemies[x]
              x = x+1
              y = 0
              while(y<len(Friendlies)):
                  Unit2 = Friendlies[y]
                  y = y+1
                  detected = AttackDefend.InRange(Unit1,Unit2)
                  if(Unit2.health>0):
                      if(detected == True):
                          Unit1.speed = 0
                          if(ERate == 30):
                              Unit1.speed = 0
                              print Unit2.health
                              Unit2.DamageUnit(Unit1.damage)                         
                              print Unit2.health
                              if Unit2.health<1:
                                  UnitLoader.DeleteUnit(Unit2)
                                  Unit1.speed = 2
                      if(Unit2.health<1):
                          Unit1.speed = 2

    
"""@classmethod
    def Attack(cls, Friendlies, Enemies):
        x = 0
        y = 0
        while x<len(Friendlies):
            x = x+1
            Unit1 = Friendlies[x-1]
            print Unit1.attacking
            if(Unit1.attacking == False):
                UnitTarget = None
            while y<len(Enemies):
                y = y+1
                if(Unit1.attacking == False):
                    Unit2 = Enemies[y-1]
                    print Unit2
                    detected = AttackDefend.InRange(Unit1, Unit2)
                if(Unit1.attacking == True):
                    detected = True
                #print detected
                if(detected == True):
                    Unit1.attacking = True
                    UnitTarget = Unit2
                    print Unit2
                if(detected == True and UnitTarget == Unit2):
                    if(Unit2.health >0):
                        Unit1.attacking = True
                        Unit1.speed = 0
                        print Unit2.health
                        print "health"
                        Unit2.health = Unit2.health - Unit1.damage
                        print Unit2.health
                        print "health"
                        if Unit2.health<1:
                            UnitSpawner.DeleteUnit(Unit2)
                            Unit1.speed = 2
                            UnitTarget = None
                            Unit.attacking = False
"""
