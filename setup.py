from distutils.core import setup

setup(name="pyuom",
      version="1.0",
      description="A Units of Measure Library",
      author='K. Hanson',
      url='https://github.com/katerina7479/python-units-of-measure.git',
      package_dir={'':'pyuom'},
      py_modules=['PhysicalQuantity', 'UnitOfMeasure', 'Acceleration', 'Angle',
                  'Area', 'Length', 'ElectricCurrent', 'LuminousIntensity',
                  'Mass', 'Pressure', 'Temperature', 'Time', 'Velocity', 'Volume'])