from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class Length(PhysicalQuantity):
    def __init__(self, value, unit):
        super(Length, self).__init__(value, unit)
        # Meter
        new_unit = UnitOfMeasure(
            'm',
            lambda x: x,
            lambda y: y)
        new_unit.addAlias('meter')
        new_unit.addAlias('meters')
        self.registerUnitOfMeasure(new_unit)

        # Millimeter
        new_unit = UnitOfMeasure(
            'mm',
            lambda x: x / 0.001,
            lambda y: y * 0.001,
        )
        new_unit.addAlias('millimeter')
        new_unit.addAlias('millimeters')
        self.registerUnitOfMeasure(new_unit)

        # Centimeter
        new_unit = UnitOfMeasure(
            'cm',
            lambda x: x / 0.01,
            lambda y: y * 0.01,
        )
        new_unit.addAlias('centimeter')
        new_unit.addAlias('centimeters')
        self.registerUnitOfMeasure(new_unit)

        # Decimeter
        new_unit = UnitOfMeasure(
            'dm',
            lambda x: x / 0.1,
            lambda y: y * 0.1,
        )
        new_unit.addAlias('decimeter')
        new_unit.addAlias('decimeters')
        self.registerUnitOfMeasure(new_unit)

        # Kilometer
        new_unit = UnitOfMeasure(
            'km',
            lambda x: x / 1000,
            lambda y: y * 1000,
        )
        new_unit.addAlias('kilometer')
        new_unit.addAlias('kilometers')
        self.registerUnitOfMeasure(new_unit)

        # Foot
        new_unit = UnitOfMeasure(
            'ft',
            lambda x: x / 0.3048,
            lambda y: y * 0.3048,
        )
        new_unit.addAlias('foot')
        new_unit.addAlias('feet')
        self.registerUnitOfMeasure(new_unit)

        # Inch
        new_unit = UnitOfMeasure(
            'in',
            lambda x: x / 0.0254,
            lambda y: y * 0.0254,
        )
        new_unit.addAlias('inch')
        new_unit.addAlias('inches')
        self.registerUnitOfMeasure(new_unit)

        # Mile
        new_unit = UnitOfMeasure(
            'mi',
            lambda x: x / 1609.344,
            lambda y: y * 1609.344,
        )
        new_unit.addAlias('mile')
        new_unit.addAlias('miles')
        self.registerUnitOfMeasure(new_unit)

        # Yard
        new_unit = UnitOfMeasure(
            'yd',
            lambda x: x / 0.9144,
            lambda y: y * 0.9144,
        )
        new_unit.addAlias('yard')
        new_unit.addAlias('yards')
        self.registerUnitOfMeasure(new_unit)
