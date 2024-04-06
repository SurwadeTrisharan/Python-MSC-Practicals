
class Student:                      #outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:                   #inner Class
        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'RYZEN 5'
            self.ram = 16
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('Trisharan',48)
s2=Student('Himanshu',24)
s1.show()
s2.show()

