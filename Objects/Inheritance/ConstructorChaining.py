class GrandParent:
    def __init__(self):
        self.x = 100
class Parent(GrandParent):
    def __init__(self):
        self.y = 200
        super().__init__()
class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()
        
c = Child()
print("X =",c.x)
print("Y =",c.y)
print("Z =",c.z)

'''
1. Constructor Chaining is the process of calling one Constructor from another constructor.
'''