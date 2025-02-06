class Calculator:
    def calculate(self,a,b):
        print("Calculate result of a and b")

class Add(Calculator):
    def calculate(self, a, b):
        print("Addition:", a+b)

class Sub(Calculator):
    def calculate(self, a, b):
        print("Subtraction:", a-b)

class Mul(Calculator):
    pass

def permit(ref,a,b):
    if type(ref).__name__ == 'Mul':
        print("Mul class does not have calculate()")
    ref.calculate(a,b)
permit(Add(),10,20) # Addition: 30
permit(Sub(),20,10) # Subtraction: 10
permit(Mul(),10,20) # Mul class does not have calculate()
                    # Calculate result of a and b