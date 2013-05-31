from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class LuminousIntensity(PhysicalQuantity):

    def __init__(self, value, unit):
        super(LuminousIntensity, self).__init__(value, unit)

        # Candela
        new_unit = UnitOfMeasure(
            'cd',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('candela')
        self.registerUnitOfMeasure(new_unit)
