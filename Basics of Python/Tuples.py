'''
1. In Tuples we can stroe Homogeneous as well as Hetrogeneous Data.
2. In Tuples we can stroe Duplicate values.
3. Tuples are Ordered Collection of Data: Order of insertion will remain as it in the output. 
4. Tuples are Immutable :Once we declare the Tuples we can not modify it.
'''

tup1 = (10,22.55,'Kodnest',True,10)
print(tup1) # (10, 22.55, 'Kodnest', True, 10)
# tup1.append(300)
#tup1.remove(10)
#tup1.pop()
#del tup1[2]
print(tup1[2]) # Kodnest

#Deletes the complete tup1 object
del tup1
#print(tup1) #Error

t1 = (1,2,3)
t2 = (4,5,6)
t3  = t1 + t2
print(t3) # (1,2,3,4,5,6)


#create a singleton Tuple:
tup = (10,)
print(tup,type(tup)) # (10,) <class 'tuple'>

new_tup = (10,20,30,40)
# ele1 = new_tup[0]
#ele2  = new_tup[1]

#Unpacking of tuple
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1',ele1) # Value of ele1 10

