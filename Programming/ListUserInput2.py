li = input('Enter space sepeated Elements ')
print(li,type(li))
li = li.split()
print(li,type(li))
li = list(map(int,li))
print(li)


'''
Enter space sepeated Elements 10 20 30 40 50
10 20 30 40 50 <class 'str'>
['10', '20', '30', '40', '50'] <class 'list'>
[10, 20, 30, 40, 50]
'''

tup = tuple(map(int,input('Enter Space seperated Elements ').split())) # 10 20 30
print(tup) # (10, 20, 30)

li = list(map(int,input().split())) # 10 11 12 13
print([i for i in li if i%2 == 0]) # [10, 12]

