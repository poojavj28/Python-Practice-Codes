print('Kodnest123*+'.isalnum()) # False
print('Kodnest'.isalpha()) #True

print('Kodnest12'.isalpha()) #False
print('code'.isalpha()) #True

print('1234'.isdigit()) #True
print('12AB'.isdigit()) #False

print('APPLE'.isupper()) #True
print('apple'.islower()) #True

print('Apple'.isupper()) #False
print('Apple'.islower()) #False

print(any([True,False,False])) #True #it will take iterator_object as a input
print(any([False,False,False])) #True



s = input() #qA2
print(any([i.isalnum() for i in s])) #True
print(any([i.isalpha() for i in s])) #True
print(any([i.isdigit() for i in s])) #True
print(any([i.islower() for i in s])) #True
print(any([i.isupper() for i in s])) #True