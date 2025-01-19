print(bool('Kodnest')) #True
#print(int('Kod')) #Error
print(int('11')) #11 ---> IMP Str(int) ---> INt
#print(float('Kodnest')) #Error
print(float(22.22)) #22.22 --->IMP
print(bool('')) #False
print(bool(0)) #False
print(bool(12)) #True
#print(int('12.56')) #Error
print(int(12.56)) #12

#Taking float value from user and converting it into int
value = int(float(input('Enter price : Float value')))
print(value, type(value))

'''
1. reverse, reversed
2. sort(), sorted()
3. map
4. list input: Difference Ways: Normal for loop, split and map
5. Nested List Input and Unpacking nested lists
6. Hackerank que: Find Runner-up score
7. Hackerank Que: Nested List
8. Practice and Homeworks
9. enumerate()
10. * operator
'''
#Pack multiple arguments into a single parameter as a tuple.
def disp(*args):
    print(args)
disp(10,20,30)

#Unpacks a list (or any iterable) into separate arguments.


