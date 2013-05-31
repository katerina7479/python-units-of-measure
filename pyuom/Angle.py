from PhysicalQuantity import PhysicalQuantity
from UnitOfMeasure import UnitOfMeasure

from math import pi


class Angle(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Angle, self).__init__(value, unit)

        # Degrees
        new_unit = UnitOfMeasure(
            u"\u00b0",
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('deg')
        new_unit.addAlias('degs')
        new_unit.addAlias('degree')
        new_unit.addAlias('degrees')

        self.registerUnitOfMeasure(new_unit)

        # Radians
        new_unit = UnitOfMeasure(
            'rad',
            lambda x: x * pi / 180,
            lambda y: y / pi * 180
        )
        new_unit.addAlias('rads')
        new_unit.addAlias('radian')
        new_unit.addAlias('radians')
        self.registerUnitOfMeasure(new_unit)
