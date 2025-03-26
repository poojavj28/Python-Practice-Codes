'''
Syntax:
for control_variable in iterable_object

'''

for i in 'Kodnest':
    print(i, end=" ") # K o d n e s t
print()

for j in [10,20,30]:
    print(j+5, end=" ") # 15 25 35
print()

for num in range(1,11):
    print(num, end=" ") # 1 2 3 4 5 6 7 8 9 10
print()

for num in range(11,21,2):
    print(num,end=" ") # 11 13 15 17 19
print()

for i in range(5):
    print(i,end=" ") # 0 1 2 3 4
print()

# WAP to print all even numbers from 1-10
for i in range(1,11):
    if(i%2==0):
        print(i,end=" ") # 2 4 6 8 10
print()

i = 0
while(i < 10):
    print(i + 100, end=" ") # 100 101 102 103 104 105 106 107 108 109
    i = i + 1
print()

#WAP to print numbers from 1-10 but if number is 6 then skip printing.
for i in range(1,11):
    if(i == 6):
        continue
    print(i,end=" ") # 1 2 3 4 5 7 8 9 10
print()
#WAP to print numbers from 1-10 but if number is 5 then stop printing.
for i in range(1,11):
    if(i == 5):
        break
    print(i,end=" ") # 1 2 3 4
print()

def disp():
    pass

class Demo:
    pass