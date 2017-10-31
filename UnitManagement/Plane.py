import pygame
from UnitManagement.Unit import Unit

class Plane (Unit):

   def __init__(self, uid):
        unitclass = "Space Plane"
        damage = 100
        speed = 1
        health = 200
        unitcost = 500
        buildtime = 5
        attackrate = 1
        unitrange = 7
        imagepath = "Images/StickSoldier.jpg"
        Unit.__init__(self, unitclass, uid, damage, speed, health, unitcost, buildtime, attackrate, unitrange, imagepath)


