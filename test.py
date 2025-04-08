from Car.car import Car #import package -> 
from Car.function import checkEngine
# from car import Car #import module


Toyota = Car("Toyota",4)
# print(Toyota.name)
# print(Toyota.wheel)

# Toyota.drive()

# suzuki = Car("SUZUKI",4)
# suzuki.drive()

print(Car.SterringWheel)
# print(Car.common())

print(Toyota.SterringWheel)
Toyota.common()

checkEngine()