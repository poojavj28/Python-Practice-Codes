#private : declare as __variable_name  
#private: It should be accessed inside the same class in which we declared.

class Demo1:
    def __init__(self,name):
        self.__name = name #private Variable
    def getName(self):
        return self.__name
    def setName(self,newName):
        self.__name = newName
d1 = Demo1('Akash')
#print(d1.__name) #Error
print(d1.getName()) # Akash

d1.setName('Pooja')
print(d1.getName()) # Pooja