from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class ElectricCurrent(PhysicalQuantity):

    def __init__(self, value, unit):
        super(ElectricCurrent, self).__init__(value, unit)

        # Ampere
        new_unit = UnitOfMeasure(
            'A',
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('amp')
        new_unit.addAlias('amps')
        new_unit.addAlias('ampere')
        new_unit.addAlias('amperes')
        self.registerUnitOfMeasure(new_unit)
