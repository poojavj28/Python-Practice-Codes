'''
1. In List we can stroe Homogeneous as well as Hetrogeneous Data.
2. In List we can stroe Duplicate values.
3. List is an Ordered Collection of Data: Order of insertion will remain as it in the output.
4. Lists are Mutable :Once we declare the list we can modify it.
'''
li1 = [10,20,44.45,True,'Kodnest',20]
print(li1,type(li1))
print(li1[0])

#append(): will add element at the end of the list
li1.append(300)
print(li1) #[10, 20, 44.45, True, 'Kodnest', 20, 300]

#insert(index, element): inserts an ele. at specified index.
li1.insert(1,15)
print(li1) #[10, 15, 20, 44.45, True, 'Kodnest', 20, 300]

#remove(ele): Removes the first occurrance of the specified ele.
li1.remove(20)
print(li1) # [10, 15, 44.45, True, 'Kodnest', 20, 300]

#in and not in Operator:
print(2000 in li1) #False
print('Kodnest' in li1) #True

#pop(): Without argument will delete and return late ele. from the list
removed_ele = li1.pop()
print(removed_ele) # 300
print(li1) # [10, 15, 44.45, True, 'Kodnest', 20]

#pop(): With Argument will delete the ele. at specified index
removed_ele=li1.pop(4)
print(removed_ele) # Kodnest
print(li1) # [10, 15, 44.45, True, 20]

#del keyword:
#li1.pop(1) #it return the deleted ele.
del li1[1] #it not return the deleted ele.
print(li1) # [10, 44.45, True, 20]

del li1
print(li1)  # Error: name 'li1' is not defined