

class UnitOfMeasure(object):

    def __init__(self, name, fnu, tnu):
        """
        name = The canonical name for this unit of measure.
        Typically this is the official way the unit is abbreviated.
        """
        self._name = name

        """
        aliases = A collection of alias names that map to this unit of measure
        """
        self._aliases = []

        """
        A callable function that can convert a value in this quantity's
        native unit to this unit of measure.
        """
        self.from_native_unit = fnu

        self.to_native_unit = tnu

    def addAlias(self, alias):
        self._aliases.append(alias)

    def getName(self):
        return self._name

    def isAliasOf(self, unit):
        return unit in self._aliases

    def convertValueFromNativeUnitOfMeasure(self, value):
        result = self.from_native_unit(value)
        return result

    def convertValueToNativeUnitOfMeasure(self, value):
        result = self.to_native_unit(value)
        return result
