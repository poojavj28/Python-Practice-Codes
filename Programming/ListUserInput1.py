li = []
num = int(input("Enter Count: ")) 
for i in range(num):
    ele = int(input(f'Enter Element at Index {i}:  '))
    li.append(ele)
print(li)

'''
Output:
Enter Count: 5
Enter Element at Index 0:  10
Enter Element at Index 1:  20
Enter Element at Index 2:  30
Enter Element at Index 3:  40
Enter Element at Index 4:  50
[10, 20, 30, 40, 50]
'''