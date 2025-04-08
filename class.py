# name = "hmmk"

# print(type(name))
# print(name.upper())

class Car:
    def __init__(self,name,wheels):
        self.name = name
        self.wheel = wheels

    def drive(self):
        print(f'{self.name} is driving')


Toyota = Car("Toyota",4)
print(Toyota.name)
print(Toyota.wheel)

Toyota.drive()

suzuki = Car("SUZUKI",4)
suzuki.drive()


