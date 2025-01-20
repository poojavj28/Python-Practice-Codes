li = [10,20,30]
for idx,ele in enumerate(li):
    print(f"Index of {ele} is {idx}") 

'''
Index of 10 is 0
Index of 20 is 1
Index of 30 is 2
'''

#WAP to print all even idex element 
li1 = [10,20,30]
for idx,ele in enumerate(li1,start=1):
    if idx%2==0:
        print("Even Index Element",ele) # Even Index Element 20
