'''
1. In dict we can stroe Homogeneous as well as Hetrogeneous Data.
2. In dict we can stroe Duplicate values.
3. dict is an Ordered Collection of Data: Order of insertion will remain as it in the output.
4. dict are Mutable :Once we declare the list we can modify it.
'''


#dict is mutable
d1 = {'name':'Priya','age':27,'phone':7338066754,'age':29}
print(d1,type(d1)) # {'name': 'Priya', 'age': 29, 'phone': 7338066754} <class 'dict'>

#In dict we cannot store duplicate keys.
#
d1['name'] ='Pooja'
print(d1) # {'name': 'Pooja', 'age': 27, 'phone': 7338066754}

# In dict we can store duplicate values.
marks = {'Sci': 85,'Maths':85} # Allowed

for i in d1.keys():
    print(i)
#name age phone

for i in d1.values():
    print(i)
# Pooja 29 7338066754

for i in d1.items():
    print(i)
#('name', 'Pooja') ('age', 29) ('phone', 7338066754)
 