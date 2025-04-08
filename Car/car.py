# name = "hmmk"

# print(type(name))
# print(name.upper())

class Car:
    SterringWheel = 1
    def __init__(self,name,wheels):
        self.name = name
        self.wheel = wheels

    def drive(self):
        print(f'{self.name} is driving')

    @classmethod
    def common(cls):
        print(f'all car has only {cls.SterringWheel} wheels')


# Toyota = Car("Toyota",4)
# # print(Toyota.name)
# # print(Toyota.wheel)

# # Toyota.drive()

# # suzuki = Car("SUZUKI",4)
# # suzuki.drive()

# print(Car.SterringWheel)
# # print(Car.common())

# print(Toyota.SterringWheel)
# Toyota.common()

