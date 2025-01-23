class Student:
    def learn(self):
        print("Inside learn Method")
        print(self.name,'is Learning')
    def play():
        print("Inside Play Method")
s1 = Student()
s1.name = 'Pooja'
print("Name is", s1.name)
s1.learn()
#s1.play() # TypeError: Student.play() takes 0 positional arguments but 1 was given