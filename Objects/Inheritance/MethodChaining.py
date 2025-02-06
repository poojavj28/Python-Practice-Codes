class GrandParent:
    def cook(self):
        print("Grand Parent can cook Biriyani..")
class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Maggi..")
class Child(Parent):
    def cook(self):
        print("Child wont cook..")
        super().cook()
        super(Parent,self).cook()
c = Child()
c.cook()
''''
Method Chaining is the process of calling one method from another method.
'''