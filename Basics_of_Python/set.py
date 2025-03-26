'''
1. In Set we can store Homogeneous as well as Hetrogeneous Data.
2. In Set we can not store Duplicate values.
3. Set is an UnOrdered Collection of Data: Order of insertion will not remain as it is in the output.
4. Set does not support indexing of data.
5. Set are Mutable :Once we declare the Set we can modify it.
'''
s1 = {10,True,'Kodnest',10,20,55.44}
print(s1,type(s1)) # {True, 20, 55.44, 10, 'Kodnest'} <class 'set'>
#print(s1[0]) # Error

#add(): Used to add an element in the set.
s1.add(500)
print(s1) # {True, 20, 500, 55.44, 10, 'Kodnest'}

s1.remove(55.44)
print(s1) # {True, 20, 500, 'Kodnest', 10}

#pop(): Without index will delete and return one ele.
poped_ele = s1.pop()
print(poped_ele) # True
print(s1) # {'Kodnest', 20, 500, 10}

#del s1[2] # Error

del s1
