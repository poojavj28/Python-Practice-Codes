#without input and without return statement
def add():
    a = 10
    b = 20
    print('Addition is:', a+b)
add()

#with input and without return statement
def sub(a,b):
    print('Subtraction is:',a-b)
sub(20,10)

#without input and with return statement
def mul():
    return 10*20
print('Multiplication is:',mul())

#with input and with return statement
def div(a,b):
    return a/b
print('Divition is:',div(20,10))