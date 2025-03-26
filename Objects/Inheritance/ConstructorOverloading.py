class Demo1:
    def __init__(self):
        self.x = 100
    def __init__(self):
        self.x = 200
d3 = Demo1()
print(d3.x) #200
'''
When we create multiple constructors in same class then only 
last declared constructor we will be invoked at the time of object creation.
'''
