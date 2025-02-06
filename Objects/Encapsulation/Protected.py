#protected : declare as _variable_name 
#protected: It should be accessed inside the same class in which we have declared and inside child class

class Demo1:
    def __init__(self,name):
        self._firstname = name #Protected Variable
    def disp1(self):
        print(self._firstname)
d1 = Demo1('Akash')
print(d1._firstname) #Akash
d1.disp1() #Akash

class Demo2(Demo1):
    def disp2(self):
        print(self._firstname)
d2 = Demo2('Pooja')
print(d2._firstname) #Pooja
d2.disp2() #Pooja

class Demo3:
    def disp3(self):
        print(d1._firstname)
d3 = Demo3()
d3.disp3() # Akash

'''
The variables which are protected, can be accessed inside the same class, outside of any class,
inside the child class,inside non-child class.

The variables which are protected shoud be accessed inside the same class and inside the child class,
this is programmers duty to follow these rules.
'''