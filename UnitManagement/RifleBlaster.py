import pygame
from UnitManagement.Unit import Unit

class RifleBlaster (Unit):

   def __init__(self):
        unitclass = "Space Rifle Blaster"
        damage = 100
        speed = 1
        health = 200
        unitcost = 200
        buildtime = 2
        attackrate = 1
        unitrange = 6
