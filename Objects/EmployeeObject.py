class Employee:
    company_name = 'code' #class based variables
    def __init__(self,name,age,desig):
        self.name = name
        self.age = age
        self.desig =desig

    def login(self,time):
        print(f"{self.name} logged in at {time}")

    def logout(self,time):
        print(f"{self.name} logged out at {time}")

    def work(self,hours):
        print(f"{self.name} worked for {hours}")

    def getDetails(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Designation:",self.desig)

#Creating Objects:
e1 = Employee('Pooja',25,'Developer')
e2 = Employee('Deepa',34,'Tester')
e3 = Employee('Sushma',24,'SDE')

e1.getDetails()
e2.getDetails()
e3.getDetails()

e1.login(12)
e2.login(2)
e3.login(5)

e1.logout(5)
e2.logout(9)
e3.logout(12)

e1.work(12)
e2.work(6)
e3.work(7)