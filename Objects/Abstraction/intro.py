
from abc import ABC, abstractmethod
class Demo1(ABC):
    #@abstractmethod
    #def disp1(self):
        #print("Inside disp1")
    pass

d1 = Demo1()

'''
If abstract class doesnot have any method then object for that abstract class can be created.
'''

class Demo2(ABC):
    def disp2(self):
        print("Inside disp2")
d2 = Demo2()
d2.disp2()
'''
If abstract class does have only concreate method then object for that abstract class can be created and concreate method can be invoked.
'''

class Demo3(ABC):
    def info(self):
        print("Inside info")
    @abstractmethod
    def disp3(self):
        print("Inside disp3")

class Demo4(Demo3):
   pass
#d4 = Demo4()
#d4.info()
#d4.disp3()

''''
If parent class as abstract method if u not override in abstract method in child class it will not allow us to create object.
'''

class Demo3(ABC):
    def info(self):
        print("Inside info")
    @abstractmethod
    def disp3(self):
        print("Inside disp3")

class Demo4(Demo3):
    def disp3(Self):
        print("Inside disp3")
d4 = Demo4()
d4.info()
d4.disp3()
