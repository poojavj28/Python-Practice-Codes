class Student:
    college_name = 'Kodnest'

    def get_info(self):
        print("College Name is :",Student.college_name)
    @classmethod
    def change_name(cls,newName):
        cls.college_name = newName
s1 = Student()
s1.get_info() # College Name is : Kodnest
Student.change_name('Code')
s1.get_info() # College Name is : Code
