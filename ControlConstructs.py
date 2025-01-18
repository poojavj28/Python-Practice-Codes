'''
1. Conditional: if-else, ifelif
2. Looping: for ,while
3. Jumping: break, continue, pass
'''

def checkAge(age):
    if (age  > 18):
        print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

# WAP to dispaly 'Child if age is in between below 18, dispaly 'Adult' is age is above 18,
#display senior Citizen if age is above 65.

def dispalyAgeCateg(age):
    if (age < 18):
        print("Child")
    elif (age > 18 and age < 65):
        print('Adult')
    elif(age > 65):
        print("Senior Cetizen")

dispalyAgeCateg(int(input('Enter age')))