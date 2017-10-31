import pygame
from UnitManagement.Unit import Unit

class SpaceRaider (Unit):

   def __init__(self, uid):
        unitclass = "Space Raider"
        damage = 50
        speed = 1.5
        health = 100
        unitcost = 100
        buildtime = 1
        attackrate = 1
        unitrange = 1
        imagepath = "Images/StickSoldier.jpg"
        Unit.__init__(self, unitclass, uid, damage, speed, health, unitcost, buildtime, attackrate, unitrange, imagepath)
