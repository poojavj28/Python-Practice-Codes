class Demo1:
    def __str__(self):
        return 'Hello'
    def __add__(self, other):
        self.a = 20
        other.b = 30
        return self.a + other.b
    def __sub__(self, other):
        self.a = 20
        other.b = 30
        return self.a - other.b
    def __mul__(self, other):
        self.a = 20
        other.b = 30
        return self.a * other.b
class Demo2:
    def __str__(self):
        return 'Hii'
d1 = Demo1()
d2 = Demo2()
'''
1. In python if print reference variable then internally python will invoke __str__() which always return string reperentation of an address of an object.
2. In the above examples we have overridden __str__ methods in their respective classes.
'''

print(d1)  
print(d2) 
print(d1+d2)
print(d1-d2)
print(d1*d2)
#Dunder Methods: The methods which has suffix and prefix as __ these dunder methods can be called as Magic methods because as programmer we no need to call any methods, automatically methods will be invoked.