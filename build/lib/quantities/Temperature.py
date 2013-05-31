from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class Temperature(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Temperature, self).__init__(value, unit)

        # Degree Kelvin
        new_unit = UnitOfMeasure(
            u"\u212A",
            lambda x: x,
            lambda y: y
        )
        new_unit.addAlias('K')
        new_unit.addAlias('kelvin')
        self.registerUnitOfMeasure(new_unit)

        # Degree Celsius
        new_unit = UnitOfMeasure(
            u"\u2103",
            lambda x: x - 273.15,
            lambda y: y + 273.15
        )
        new_unit.addAlias('C')
        new_unit.addAlias('celsius')
        self.registerUnitOfMeasure(new_unit)

        # Degree Fahrenheit
        new_unit = UnitOfMeasure(
            u"\u2109",
            lambda x: x * (9.0 / 5.0) - 459.67,
            lambda y: (y + 459.67) * (5.0 / 9.0)
        )
        new_unit.addAlias('F')
        new_unit.addAlias('fahrenheit')
        self.registerUnitOfMeasure(new_unit)
