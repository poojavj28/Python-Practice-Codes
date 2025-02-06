class Student:
    def cook(self):
        print("Student is cooking...")
    def play(self):  
        print("playing cricket...")
class Employee(Student):
    def work(self):
        print("Employee is working")
    def cook(self):
        print("Employee is cooking")

e = Employee()
e.play()
e.cook()
e.work()

'''
Method which is inherited from parent class and that is used as it is in child class is called as Inherited method.   example: play() method
Method which is change from parent method to child method is called as Overridden Method.   example: cook() method
The method only parent in Child class is called Special Method.   example: work() method

'''