#MRO Method Resolution Order

class A:
    def __init__(self):
        print('In constructor of class A')
    def feature1(self):
        print('Feature 1 Working')


class B(A):
    def feature3(self):
        print('Feature 3 Working')

a1=A()
print('----')
b1=B()

