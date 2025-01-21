#list_name[start:end-1:steps]
li1 = [10,20,30,40,50,60]

sub_list = li1[0:4:1]
print(sub_list) # [10, 20, 30, 40]

sub_list1 = li1[::]
print(sub_list1) # [10, 20, 30, 40, 50, 60]

sub_list2 = li1[1::]
print(sub_list2) # [20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) # [10, 30, 50]

reversed_list = li1[::-1]
print(reversed_list) # [60, 50, 40, 30, 20, 10]

sub_list4 = li1[-1::]
print(sub_list4) # [60]

'''
Q: What is List Slicing?
It is used to create sublist from main list.
It does not modified the original list
Syntax: list_name[start:end-1:steps]

reverse list: [::-1]
last ele: [-1::]
'''
