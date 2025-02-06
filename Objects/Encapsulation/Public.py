#Access Modifier/ Access Specifier: Access modifiers are used to determine  the accessibility of data members and member function.
#public : declare as variable_name 
#public: It should be accessed inside the class, outside the class
#protected : declare as _variable_name 
#protected: It should be accessed inside the same class in which we have declared and inside child class
#private : declare as __variable_name  
#private: It should be accessed inside the same class in which we declared.

class Demo1:
    def __init__(self,name):
        self.firstname = name
    def disp1(self):
        print(self.firstname)
d1 = Demo1('Akash')
print(d1.firstname) #Akash
d1.disp1() #Akash

class Demo2(Demo1):
    def disp2(self):
        print(self.firstname)
d2 = Demo2('Pooja')
print(d2.firstname) #Pooja
d2.disp2() #Pooja

'''
The variables which are public, can be accessed inside the same class, outside of any class,
inside the child class,inside non-child class.
'''