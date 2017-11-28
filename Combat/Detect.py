from UnitManagement import*
from Combat import AttackDefend
class Detect:
  @classmethod
  def InRange(cls, Unit1, Unit2):
    detect = False
    UnitRange = Unit1.unitrange
    print Unit2.xpos
    print Unit1.xpos
    print UnitRange
    if Unit2.xpos-Unit1.xpos<=UnitRange/100:
      detect = True
    else:
      detect = False
    return detect
