import pygame
from UnitManagement.Unit import Unit

class Tank(Unit):

   def __init__(self, uid):
        unitclass = "Space Tank"
        damage = 500
        speed = .5
        health = 1600
        unitcost = 500
        buildtime = 5
        attackrate = 5
        unitrange = 2
        imagepath = "Images/StickSoldier.jpg"
        Unit.__init__(self, unitclass, uid, damage, speed, health, unitcost, buildtime, attackrate, unitrange)

