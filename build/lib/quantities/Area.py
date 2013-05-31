from source.PhysicalQuantity import PhysicalQuantity
from source.UnitOfMeasure import UnitOfMeasure


class Area(PhysicalQuantity):

    def __init__(self, value, unit):
        super(Area, self).__init__(value, unit)

        # Meters squared
        new_unit = UnitOfMeasure(
            'm^2',
            lambda x: x,
            lambda y: y
        )

        new_unit.addAlias('m²')
        new_unit.addAlias('meter squared')
        new_unit.addAlias('meters squared')
        self.registerUnitOfMeasure(new_unit)

        # Millimeter squared
        new_unit = UnitOfMeasure(
            'mm^2',
            lambda x: x / 1e-6,
            lambda y: y * 1e-6,
        )

        new_unit.addAlias('mm²')
        new_unit.addAlias('millimeter squared')
        new_unit.addAlias('millimeters squared')
        self.registerUnitOfMeasure(new_unit)

        # Centimeter squared
        new_unit = UnitOfMeasure(
            'cm^2',
            lambda x: x / 1e-4,
            lambda y: y * 1e-4
        )
        new_unit.addAlias('cm²')
        new_unit.addAlias('centimeter squared')
        new_unit.addAlias('centimeters squared')
        self.registerUnitOfMeasure(new_unit)

        # Decimeter squared
        new_unit = UnitOfMeasure(
            'dm^2',
            lambda x: x / 1e-2,
            lambda y: y * 1e-2
        )
        new_unit.addAlias('dm²')
        new_unit.addAlias('decimeter squared')
        new_unit.addAlias('decimeters squared')
        self.registerUnitOfMeasure(new_unit)

        # Kilometer squared
        new_unit = UnitOfMeasure(
            'km^2',
            lambda x: x / 1e6,
            lambda y: y * 1e6
        )
        new_unit.addAlias('km²')
        new_unit.addAlias('kilometer squared')
        new_unit.addAlias('kilometers squared')
        self.registerUnitOfMeasure(new_unit)

        # Foot squared
        new_unit = UnitOfMeasure(
            'ft^2',
            lambda x: x / 9.290304e-2,
            lambda y: y * 9.290304e-2
        )
        new_unit.addAlias('ft²')
        new_unit.addAlias('foot squared')
        new_unit.addAlias('feet squared')
        self.registerUnitOfMeasure(new_unit)

        # Inch squared
        new_unit = UnitOfMeasure(
            'in^2',
            lambda x: x / 6.4516e-4,
            lambda y: y * 6.4516e-4
        )
        new_unit.addAlias('in²')
        new_unit.addAlias('inch squared')
        new_unit.addAlias('inches squared')
        self.registerUnitOfMeasure(new_unit)

        # Mile squared
        new_unit = UnitOfMeasure(
            'mi^2',
            lambda x: x / 2.589988e6,
            lambda y: y * 2.589988e6
        )
        new_unit.addAlias('mi²')
        new_unit.addAlias('mile squared')
        new_unit.addAlias('miles squared')
        self.registerUnitOfMeasure(new_unit)

        # Yard squared
        new_unit = UnitOfMeasure(
            'yd^2',
            lambda x: x / 8.361274e-1,
            lambda y: y * 8.361274e-1
        )
        new_unit.addAlias('yd²')
        new_unit.addAlias('yard squared')
        new_unit.addAlias('yards squared')
        self.registerUnitOfMeasure(new_unit)
