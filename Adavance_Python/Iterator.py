li = [10,20,30,40,50]
print(type(li),li) # <class 'list'> [10, 20, 30, 40, 50]
iterator_object = iter(li)
print(type(iterator_object),iterator_object) # <class 'list_iterator'> <list_iterator object at 0x0000020A92BBAFE0>

print(next(iterator_object)) # 10
print(next(iterator_object)) # 20
print(next(iterator_object)) # 30
print(next(iterator_object)) # 40
print(next(iterator_object)) # 50
#print(next(iterator_object)) # StopIteration