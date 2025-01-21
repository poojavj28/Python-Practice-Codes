'''li1 = [1,2,3,4,5]
print(li1) # [1, 2, 3, 4, 5]
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(sq_li) # [1, 4, 9, 16, 25] '''

li1 = [1,2,3,4,5]

new_li1 = [i for i in li1]
print(new_li1) # [1, 2, 3, 4, 5]

sq_li = [i**2 for i in li1]
print(sq_li) # [1, 4, 9, 16, 25]

new_li = [ele+2 for ele in li1]
print(new_li) # [3, 4, 5, 6, 7]

#When we have only if part then write it after for loop.
even = [i for i in li1 if i%2==0]
print(even) # [2, 4]

#When we have if-else both write it before for loop.
even_odd= ['Even' if i%2==0 else 'Odd' for i in li1]
print(even_odd) # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

#Multiple for loop inside list comprehension
li = [[10,20],[30,40],[50,60]]
print(li) # [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li) #[10, 20, 30, 40, 50, 60]

li4 = [[1,2],[3,4]]
li5= [ele if ele%2==0 else 'no' for i in li4 if len(i)>2 for ele in i]
print(li5)

