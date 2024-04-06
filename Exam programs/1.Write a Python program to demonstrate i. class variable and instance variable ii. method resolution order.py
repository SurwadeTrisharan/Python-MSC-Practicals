#class variable and a instance variable

class Car:
    wheels=4
    
    def __init__(self):
        self.mil = 10
        self.make = "BMW"


c1=Car()
c2=Car()

print(c1.mil,c1.make,c1.wheels)
print(c2.mil,c2.make,c1.wheels)
